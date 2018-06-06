#!/bin/bash

# The mount directory from config.yaml is in /exercise.
# Append the required support files to test user solution.
cp /exercise/check_number.py check_number.py

# copy the personalized instance file (file named "number")
cp /personalized_exercise/number number

# run the exercise grader program
# "capture" etc description in https://github.com/A-plus-LMS/grading-base
capture pre python3 check_number.py

exit 0
