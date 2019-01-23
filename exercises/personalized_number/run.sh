#!/bin/bash

# The student's submission is in /submission/user and
# it is the working directory as well.
# Append the required support files to test the user's solution.
# Copy the personalized instance file (file named "number").
cp /personalized_exercise/number number

# run the exercise grader program
# "capture" etc description in https://github.com/apluslms/grading-base
capture pre python3 /exercise/check_number.py

exit 0
