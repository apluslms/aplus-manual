#!/bin/bash

docker run --rm \
  -v "$(pwd):/compile" \
  -u $(id -u):$(id -g) \
  -e "STATIC_CONTENT_HOST=http://localhost:8080/static/default" \
  -e "COURSE_KEY=default" \
  apluslms/compile-rst:1.6 \
  make html
