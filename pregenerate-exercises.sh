#!/bin/bash

# This script is used for generating personalized exercise instances.
# Run ./pregenerate-exercises.sh --help for instructions.

args=""
keep_old=false
exercise_key=""
while [ "$1" ]; do
    case "$1" in
        --instances)
            # Check if the next argument exists
            if [ -z "$2" ] || [ "${2:0:1}" = "-" ] || ! [[ "$2" =~ ^[0-9]+$ ]]; then
                echo "ERROR: --instances requires an integer argument" >&2
                exit 1
            fi
            args="${args}${1} ${2} "
            shift 2
            ;;
        --keep-old) keep_old=true; shift ;;
        --gen-if-none-exist) args="${args}${1} "; shift ;;
        --help)
            echo "Usage: $0 [--instances <integer>] [--keep-old] [--gen-if-none-exist] [<exercise-key>]"
            echo "--instances: Number of instances to generate for an exercise (default: 10)"
            echo "--keep-old: Keep existing generated instances instead of deleting them first"
            echo "--gen-if-none-exist: Only generate new instances for an exercise if no instances exist yet"
            echo "<exercise-key>: Exercise key for which new instances should be generated." \
                 "By default all personalized exercises in the course are generated." \
                 "The possible keys are the directory names under '<course-root>/personalized_exercises/'" \
                 "after the initial exercise instances have been generated without using the argument."
            exit 0
            ;;
        -*)
            echo "ERROR: Invalid option '$1' for $0" >&2
            echo "Usage: $0 [--instances <integer>] [--keep-old] [--gen-if-none-exist] [<exercise-key>]" >&2
            exit 1
            ;;
        *) args="${args}${1} "; exercise_key="${1}"; shift ;;
    esac
done

if [ ! -d "./_build" ]; then
  echo "ERROR: Course must be built before personalized exercise instances can be pregenerated."
  exit 1
fi

if [ -n "$exercise_key" ] && [ "$keep_old" = false ]; then
    rm -rf "./personalized_exercises/$exercise_key"
elif [ "$keep_old" = false ]; then
    rm -rf ./personalized_exercises/*
fi

docker run \
    --name aplus-grader-pregen \
    --volume ".:/srv/courses/default:ro" \
    -it apluslms/run-mooc-grader:latest \
    /bin/sh -c "python3 manage.py pregenerate_exercises default $args"

docker cp aplus-grader-pregen:/local/grader/ex-meta/default/pregenerated/. ./personalized_exercises

docker container rm aplus-grader-pregen

echo -e "\nPersonalized exercises generated!"
