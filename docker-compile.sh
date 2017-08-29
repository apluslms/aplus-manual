#!/bin/bash
docker run --rm -v $(pwd):/compile apluslms/compile-rst make touchrst
docker run --rm -v $(pwd):/compile -e "STATIC_CONTENT_HOST=http://localhost:8080/static/default" apluslms/compile-rst make html
