#!/bin/bash

git submodule init
git submodule update

# the course key in the production server grader.cs
export COURSE_KEY='aplus-manual'

# touchrst ensures that all changes in the RST or config YAML files
# are always taken into account in the compilation (make html).
make touchrst html
