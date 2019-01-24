#!/bin/bash

# The mount directory from config.yaml is in /exercise.
# The submission in is /submission/user and it is the working directory.
# Append the required support files to test user's solution.
# Copy the personalized instance file (file named "name").
cp /personalized_exercise/name name

# Modify PYTHONPATH so that the student's submission may be imported easily.
export PYTHONPATH=/submission/user

# run the exercise grader program
# "capture" etc description in https://github.com/apluslms/grading-base
capture pre python3 /exercise/check.py

exit 0
