Writing programming exercises
=============================

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

The file ``programming_exercises/hello_world.rst`` is a sample page
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

config.yaml
-----------
This file has the exercise configuration for Mooc-grader. The following is
a copy of ``exercises/hello_python/config.yaml``.

.. code-block:: yaml

  ---
  title: Hello Python!
  description: A simple grading example with Python code
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
    image: apluslms/grade-python:3.6-2.7
    mount: exercises/hello_python
    cmd: /exercise/run.sh

Explanation of the settings:

- title
    The title of the exercise. The RST file having a reference to the
    exercise may override this when using the "aplus-submit" directive.

- description
    This is not actually shown anywhere.

- instructions
    The HTML code for the instructions for the student.

- view_type
    value "access.types.stdasync.acceptFiles" defines that the
    student must submit one or more files to complete the exercise.

- files
    This defines each file that the student can submit. Each file might have
    different name at student's computer, but they are renamed by the "name"
    field.

- container
    This specifies the Docker container which is used for grading.

    **image** is the container image. The value ``apluslms/grade-python:3.6-2.7`` means
    that the container is grade-python made by organisation apluslms. The container
    has Python version 3.6 installed and it is based on version 2.7 of the
    "grading-base" container. For full documentation, see the repositories for
    `grading-base <https://github.com/apluslms/grading-base>`_ and
    `grade-python <https://github.com/apluslms/grade-python>`_.

    **mount** is the relative path of the directory which will be mounted to the directory
    ``/exercise`` inside the container (read only). This directory should contain
    the files required to run the grader program.
    (The student's submission files will be mounted separately by the platform
    to the path ``/submission/user``.)
    If Python graderutils are used (covered later in this page), the mount directory
    would contain, for example, the files config.yaml, run.sh,
    test_config.yaml and various Python files (model solution, unit tests).

    **cmd** describes what command is run inside the container. run.sh is the
    actual grading script. The command may include parameters and it is not
    required to be a shell script named run.sh.

`The documentation of grading-base
<https://github.com/apluslms/grading-base/blob/master/README.md>`_ is a good
starting point for understanding the grading system.

- https://github.com/apluslms/grading-base/blob/master/README.md
- https://github.com/apluslms/grade-python/blob/master/README.md
- https://hub.docker.com/r/apluslms/grade-python/


run.sh
------

This is the shell script which is run inside the grading container.

.. code-block:: bash

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

    err-to-out
    grade

Note! run.sh must have executing rights. That is, if you create the file from
scratch, you must do the following:to

1. Open the terminal.
2. ``cd`` to the directory of the exercise.
3. ``chmod a+x run.sh``


Python-grader-utils
-------------------

Python-grader-utils (just "Graderutils") is a Python library for test suite
management, file validation and test feedback formatting. It is used with
Python programming exercises. The source code and
documentation is here: https://github.com/Aalto-LeTech/python-grader-utils

By default, Graderutils uses the configuration file **test_config.yaml** in the
exercise directory. A simple test_config.yaml looks like this:

.. code-block:: yaml

    test_modules_data:
      - module: tests
        description: Local tests
      - module: grader_tests
        description: Grader tests

    validation:
      - type: python_import
        file: primes.py
      - type: python_syntax
        file: primes.py


**test_modules_data** defines which Python unit test files are executed.

**module** is the name of the Python file (without .py)

**description** is the purpose of the file.

Typically there is file **tests.py** which is given to the student. It has some
very basic unit tests. Typically some points are given for passing these
tests. Another file is typically **grader_tests.py** which has the secret, more
complex and thorough unit tests. Most of the exercise points are obtained
by passing these grader tests.

**validation** instructs Graderutils to make a syntax analysis tests of the
submitted files before the unit tests are executed.

In the example above, Graderutils checks two items according to the validation settings:

1. Attempt to import the file as a Python module and catch all exceptions
   during import. Show exceptions with the error template if there are any.

2. Read the contents of file, attempt to parse the contents using ast.parse
   and catch all exceptions. Show exceptions with the error template if
   there are any.

With Graderutils, it is possible to forbid some Python syntax or libraries in
some particular exercise, for example, deny using the default sort function of Python
in an exercise where the student must implement their own sorting method.



Debugging Python exercise graders
=================================

General instructions
--------------------

If one needs to find out why a grader for some particular Python exercise
does not work, here are general tips.

- Add ``exec >> /feedback/err`` as the second line of **run.sh**. This should
  print some error messages.

- Add ``echo`` to **run.sh**. Then log into A+ as root and inspect the exercise
  submission. You should see all the error messages.

- Add ``ls -l`` to **run.sh** to show the contents of the grading directory
  inside the grading container.

If all these fail, one can run a shell `inside the grading container
<debugging_in_container>`_.

Error messages and probable causes
----------------------------------


A+ "No grader feedback available for this submission."
......................................................

Probable cause: the *run.sh* file of this exercise does not have execution
rights.

1. Open the terminal.
2. ``cd`` to the directory of the exercise.
3. ``chmod a+x run.sh``


A+: "Something went wrong with the grader tests..."
...................................................

Probable causes:

- *config.yaml* is misconfigured: it cannot find some unit test module
- *config.yaml* cannot render feedback_template
- error on some Python file in the ``/submission/user`` directory (syntax error,
  exception, or trying to `import` some library or function which does not
  exist anymore).


If that does not help, debug the exercise grader inside the grading container.

