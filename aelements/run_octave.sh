#!/bin/bash

# run.sh: This script is intended to be used as the starting point for grading
# Octave-based visualizations in a container. "Grading" refers to producing
# the plot/image since the visualizations are not graded with points.
# This script assumes that the student inputs zero or more parameters
# (usually at least one) and the grader program is an Octave script named draw.m
# that writes one PNG image file named plot.png.
# The draw.m script receives the input parameters as command-line arguments and
# it must also validate the input, e.g., that they are valid numbers or
# matrix definitions.
#
# Arguments to this run.sh script:
# run.sh exercisedir [inputfile1 inputfile2 ...]
# exercisedir is the name of the exercise directory under the mount directory.
# It must contain the exercise-specific Octave script draw.m.
# The rest of the arguments are file paths to the parameters given by the student.
# run.sh reads the contents of the files and passes them to the draw.m script
# as command-line arguments.
#
# The exercise config.yaml defines this script as the starting point by using
# the container/cmd field. The path to this script is given in the form that
# is visible inside the container, i.e., the directory mounted from the course
# repository becomes /exercise inside the container. Do not forget to supply
# the command-line parameters required by this run.sh script.
# The work directory in the container is /submission/user and it already contains
# the student's submission in a file before this script is run.
# The /exercise directory in the container is mounted to the directory defined in
# the container/mount field of config.yaml inside the course repository.

# parameter $1: name of the exercise directory that contains the specific draw.m
# Octave script for this visualization
exercisedir="$1"
shift
# Any following parameters: file path(s) to the student's input
params=()
for filepath in "$@"
do
    if [ ! -f "$filepath" ]; then
        # The file does not exist. Is the exercise config.yaml container/cmd field
        # correct and have the input keys been given correctly?
        >&2 echo "run.sh was called with invalid arguments. The path to the student's input file is invalid: \"$filepath\"."
        exit 1
    fi
    read param < "$filepath"
    params+=("$param")
done

if [ ! -f /exercise/"$exercisedir"/draw.m ]; then
    # The draw.m script was not found. The parameter defined in the exercise config.yaml
    # may be incorrect under the container/cmd field.
    >&2 echo "run.sh was called with invalid arguments. The given exercise directory does not contain a draw.m file: \"$exercisedir\"."
    exit 1
fi

# Run the Octave script that produces the image file plot.png.
# Redirect stdout and stderr. The default values of capture are /feedback/out and
# /feedback/err. The Octave script should read the student's parameter(s) from its
# command-line arguments. It may print input validation errors to stdout and
# exit with error code 1 if there are errors.
capture -o /feedback/out -e /feedback/grading-script-errors octave-cli --no-window-system --no-gui --quiet \
    /exercise/"$exercisedir"/draw.m "${params[@]}"
# Check for errors.
drawexitval=$?
if [ "$drawexitval" -ne 0 ]; then
    read errormsg < /feedback/out
    echo "<div id=\"feedback\"><div class=\"alert alert-danger\">$errormsg</div></div>" > /feedback/out
    grade 0/0
    exit 0
fi
# Clear the feedback file.
> /feedback/out
# Base64 encode the PNG image and make an img HTML element from the encoded string.
# Capture redirects stdout to /feedback/out (i.e., the HTML image with base64-encoded data).
capture echo '<div id="feedback"><img src="data:image/png;base64, '$(base64 plot.png)'"/></div>'

# Visualizations grant no points to the students.
# Send the feedback (base64-encoded image) to the grader platform.
grade 0/0

exit 0
