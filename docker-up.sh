#!/bin/bash

OS=$(uname -s)
COMPOSE_PROJECT_NAME=aplus
DOCKER_SOCK=/var/run/docker.sock
[ -e "$DOCKER_SOCK" ] || { echo "ERROR: docker socket $DOCKER_SOCK doesn't exists. Do you have docker-ce installed?." >&2; exit 1; }
USER_ID=$(id -u)
USER_GID=$(id -g)

if [ $USER_ID -eq 0 ] || [ "$OS" = 'Darwin' ]; then
    DOCKER_GID=0
    if ! [ -e $DOCKER_SOCK ]; then
        echo "No docker socket detected in $DOCKER_SOCK. Is docker installed and active?" >&2
    fi
else
    DOCKER_GID=$(stat -c '%g' $DOCKER_SOCK)
    if ! [ -w $DOCKER_SOCK ]; then
        echo "Your user does not have write access to docker." >&2
        echo "It is recommended that you add yourself to that group (sudo adduser $USER docker; and then logout and login again)." >&2
        echo "Alternatively, you can execute this script as sudo." >&2
        exit 1
    fi
fi

if [ -z $(which docker-compose) ]; then
    echo "ERROR: Unable to find docker-compose. Are you sure it is installed and on your path?" >&2
    exit 1
fi

DATA_PATH=_data
has_data=$(grep -F "$DATA_PATH" docker-compose.yml|grep -vE '^\s*#')
[ "$has_data" ] && mkdir -p "$DATA_PATH"

ACOS_LOG_PATH=_data/acos
has_acos_log=$(grep -F "$ACOS_LOG_PATH" docker-compose.yml|grep -vE '^\s*#')
[ "$has_acos_log" ] && mkdir -p "$ACOS_LOG_PATH"

export COMPOSE_PROJECT_NAME USER_ID USER_GID DOCKER_GID

pid=
keep=
onexit() {
    trap - INT
    # send SIGINT (^C) to childs of the docker-compose and to the process itself
    [ "$pid" ] && { pkill -2 -P $pid; kill -2 $pid; } || true
    wait
    if [ "$keep" = "" ]; then
        clean
    else
        echo "Data was not removed. You can remove it with: $0 --clean"
    fi
    rm -rf /tmp/aplus || true
    while read -rs -t 0; do read -rs -t 0.1; done # flush input
    exit 0
}

clean() {
    echo " !! Removing persistent data !! "
    docker-compose down --volumes --remove-orphans
    if [ "$DATA_PATH" -a -e "$DATA_PATH" ]; then
        echo "Removing $DATA_PATH"
        rm -rf "$DATA_PATH" || true
    fi
}

update() {
    docker-compose pull
    res=$?
    [ $res -eq 0 ] && touch docker-compose.yml
    return $res
}

while [ "$1" ]; do
    case "$1" in
        -c|--clean)
            clean
            exit 0
            ;;
        -u|--update)
            update
            exit $?
            ;;
        *)
            echo "Invalid option $1" >&2
            exit 1
            ;;
    esac
    shift
done

docker-compose --version

if [ $(($(date +%s) - $(date -r docker-compose.yml +%s))) -gt 604800 ]; then
    # pull updates weekly
    echo "Checking for updates to the service images..."
    update
    echo
fi

mkdir -p /tmp/aplus
trap onexit INT
docker-compose up & pid=$!

help_n=4 # show first info after 24 seconds
while kill -0 $pid 2>/dev/null; do
    while read -rs -t 0; do read -rs -t 0.1; done # flush input
    read -rsn1 -t 6 i # read a byte
    # (1 or 142) -> timeout (6s). Show help every 50 times (every 5 minutes)
    [[ $? != 0 ]] && { ((--help_n > 0)) && continue || help_n=50; }
    case "$i" in
        q|Q) break ;;
        s|S) keep="x" ; break ;;
        $'\e') # escape (ESC or ANSI code)
            read -rsn1 -t 0.01 i # try to read a second byte
            [ $? -eq 142 ] && { keep="x"; break; } # timeout -> no second byte -> plain ESC
            ;;
    esac

    # print status and help
    echo
    echo "  List of alive containers:"
    { docker container ls --filter "name=^${COMPOSE_PROJECT_NAME}_"  --format "{{.ID}}" | xargs docker container inspect --format '	{{.Name}}	{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}	{{range $p, $conf := .NetworkSettings.Ports}}{{$p}} {{end}}'; } 2>/dev/null || true
    echo
    echo "  Press Q or ^C to stop all and to remove data"
    echo "  Press S or ESC to stop all and to keep data"
    echo
done
onexit
