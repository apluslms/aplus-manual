#!/bin/bash

# The uploaded user files are always in /submission/user
# and named identically to config.yaml regardless of the uploaded file names.

# The mount directory from config.yaml is in /exercise.
# Append the required support files to test user solution.
cp /exercise/*.js .

# "capture" etc description in https://github.com/apluslms/grading-base

capture nodejs tests.js

err-to-out
grade
