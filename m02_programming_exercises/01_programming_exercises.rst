Writing programming exercises
=======================================================

This section is an introduction to creating programming exercises
in A+.

Writing a base code and unit tests
----------------------------------

We will use the "Hello Python" exercise on this course as an example.
The files related to this exercise are in directory ``exercises/hello_python``.

Defining the exercise in an RST file
....................................

The file ``m02_introduction/chapter02.rst

A docker container that includes a stable Debian Linux and convenience commands for grading a student submission. Commands include tools from capturing the test output to submitting a feedback back to the grading service.

- https://github.com/apluslms/grading-base/blob/master/README.md
- https://hub.docker.com/r/apluslms/grade-python/


config.yaml
-----------
This file has the exercise configuration for Mooc-grader.

 TODO: example of this file

run.sh
------
This is a shell script which is run inside the grading container.

TODO: example of this file

test_config.yaml
----------------
This is a specific setting file for
`Python grader utils <https://github.com/aalto-letech/python-grader-utils>`_,
which is a tool package for grading programming exercises in Python language.

TODO: example of this file
