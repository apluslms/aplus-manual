#!/bin/bash

# The working directory is /submission/user which has the user-submitted files
# defined in config.yaml.

# The mount directory from config.yaml is in /exercise (read only) .
# Copy files related to unit testing to /submission/user.
cp /exercise/feedback_plot_png.html .

# Run python-grader-utils with settings file test_config.yaml
graderutils
