#!/bin/bash

# The mount directory from config.yaml is in /exercise.
# Append the required support files to test user solution.
cp /exercise/check.py check.py

# copy the personalized instance file (file named "name")
cp /personalized_exercise/name name

# run the exercise grader program
# "capture" etc description in https://github.com/A-plus-LMS/grading-base
capture pre python3 check.py

exit 0
