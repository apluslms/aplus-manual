Writing programming exercises
=======================================================

.. styled-topic::

  Main questions:
      How to create a programming exercise and its grading.

  Topics?
      YAML files, shell scripts, Docker containers for grading

  What you are supposed to do?
      Read the documentation.

  Difficulty:
      ?

  Laboriousness:
      ?

This section is an introduction to creating programming exercises
in A+.

Writing a base code and unit tests
----------------------------------

We will use the "Hello Python" exercise on this course as an example.
The files related to this exercise are in directory ``exercises/hello_python``.

Defining the exercise in an RST file
....................................

The file ``m02_programming_exercises/02_hello_world.rst`` is a sample page
which contains two programming exercises: the classic "Hello world!" program
for Python and Scala programming languages. Let's look at the "Hello Python!"
exercise. It requires two lines:

.. code-block:: rst

  .. submit:: python 10
    :config: exercises/hello_python/config.yaml

The exercise is included with the ``submit`` Sphinx directive, which is from the
*A+ RST tools* package. That directive
places exercise submission forms. The number ``10`` is the maximum score that
the student will get from this exercise. The exercise has a configuration
file ``exercises/hello_python/config.yaml`` which is defined with the
``:config:`` option. As was mentioned in the *Docker* chapter, the definition
of this directive is in the file ``a-plus-rst-tools/directives/submit.py``,
but you don't need to understand the contents of that file.

Next, let's look at the actual configuration file,
``exercises/hello_python/config.yaml``.

.. code-block:: yaml

  ---
  title: Hello Python!
  description: An example of grading with Python code
  instructions: |
      <p>
          In this exercise you must implement a function <var>hello</var>
          that returns a string "<samp>Hello Python!</samp>".
      </p>
  view_type: access.types.stdasync.acceptFiles
  files:
    - field: file1
      name: functions.py

  container:
    image: apluslms/grading-python:3.5
    mount: exercises/hello_python
    cmd: /exercise/run.sh

TODO

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
