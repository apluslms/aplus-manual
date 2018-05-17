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

DATA_PATH=_data
has_data=$(grep -F "$DATA_PATH" docker-compose.yml|grep -vE '^\s*#')
[ "$has_data" ] && mkdir -p "$DATA_PATH"

export COMPOSE_PROJECT_NAME USER_ID USER_GID DOCKER_GID

pid=
clean() {
    trap clean2 INT
    [ "$pid" ] && kill $pid || true
    wait
    clean2
}
clean2() {
    trap - INT
    docker-compose down --volumes
    rm -rf /tmp/aplus || true
    exit 0
}

mkdir -p /tmp/aplus
trap clean INT
docker-compose up & pid=$!

while kill -0 $pid 2>/dev/null; do
    echo "  Press q, ESC or ^C to quit."
    read -rsn1 i
    [ "$i" = 'q' -o "$i" = 'Q' -o "$i" = $'\e' ] && break
done
clean
