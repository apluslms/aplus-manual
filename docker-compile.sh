#!/bin/bash

docker run --rm \
  -v $(pwd):/compile \
  -u $(id -u):$(id -g) \
  -e "STATIC_CONTENT_HOST=http://localhost:8080/static/default" \
  apluslms/compile-rst \
  make touchrst html
