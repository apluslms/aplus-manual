#!/bin/bash

# The uploaded user files are always in /submission/user
# and named identically to config.yaml regardless of the uploaded file names.
# The directory /submission/user is also the default working directory
# in the container.

# The mount directory from config.yaml is in /exercise.
# Append the required support files to test user solution.

# Add the working directory to the PYTHONPATH so that the grader
# can import the student's submission. The grader program is started
# under the path /exercise since there is no need to copy it to
# the working directory.
export PYTHONPATH=/submission/user

# "capture" etc description in https://github.com/apluslms/grading-base
capture python3 /exercise/tests.py

# Python unit tests write output both to standard output stream and to
# standard error output stream. The command 'err-to-out' appends the contents
# of the error stream to the output stream so that the student can see all the
# output the tests have created.
err-to-out
