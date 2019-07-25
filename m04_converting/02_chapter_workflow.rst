The workflow for converting a chapter
=====================================

This section proposes a workflow for converting a chapter (or "module") in a
non-Docker A+ course for the Docker version. It assumes that the initialisation
described in `the previous chapter <01_virtualenv_to_docker.html>`_ is
completed. See the earlier chapter `Instructions
<../m02_programming_exercises/01_instructions>`_ in the Programming exercises
module for more information.

Add the RST files of the module
-------------------------------

1.  Move the RST directory of the next module that is not yet converted
    from **old** to the main directory. For example:

    .. code-block:: none

        git mv old/python1 python1

2.  Add the index file of that module to the main **index.rst**.
    In the example below, the module is **python1** and its index file is
    **kierros.rst**. Delete the A+ manual course modules in that file, or
    comment them.

    .. code-block:: rst

        The actual name of the course
        =============================

        This index lists an entry for each learning module on course.
        Other content is not visible in A+.

        .. toctree::
          :maxdepth: 2

          python1/kierros

        ..
          m01_introduction/index
          m02_programming_exercises/index
          m03_acos/index
          m04_converting/index

3.  Update the ``:open-time:``, ``:close-time:``, and ``:late-time:`` for the
    round in the index file of the module in order to be able to test th
    exercises. You might want to save the actual deadlines of the last course
    by commenting them out.

    .. code-block:: rst

      Ohjelmointi 1
      ^^^^^^^^^^^^^

      .. toctree::
        :maxdepth: 1

        kurssin_esittely
        python-tutorial-1
        unittest
        python-harjoitukset-1

      .. aplusmeta::
        :open-time: 2018-06-01 14:00:00
        :close-time: 2018-08-31 16:00:00
        :late-time: 2018-08-31 23:59:59

      ..
        .. aplusmeta::
          :open-time: 2018-01-02 14:00:00
          :close-time: 2018-01-12 16:00:00
          :late-time: 2018-02-28 23:59:59

4.  Test the course material: compile RST, then run A+ and mooc-grader.

    .. code-block:: none

      ./docker-compile.sh && rm -rf _data && ./docker-up.sh

    Check possible compilation errors in the terminal. Then view the course
    at http://127.0.0.1:8000 in your web browser the usual way. The exercises
    coded directly in the RST files should work. If they don't work, the
    problem is likely either a typo in your RST code or something with the
    related Sphinx directive in the ``extensions`` directory.


Modify exercise grading files
-----------------------------

The following is an example of a real Python programming exercise. Notice that
you do not need to modify the RST file for updating the exercise for the
Docker version of your course.

First, rename current **config.yaml** file of the exercise to
**config_old.yaml**.

config_old.yaml
...............

.. code-block:: yaml

  view_type: access.types.stdasync.acceptFiles
  files:
    - field: file1
      name: laskesumma.py

  feedback_template: access/task_direct.html

  actions:
    - type: grader.actions.prepare
      charset: UTF-8
      cp_exercises: |
        python1/laskesumma/grader_tests.py->user
        python1/laskesumma/test_config.yaml->user
      expect_success: True

    - type: grader.actions.sandbox_python_test
      cmd: [ "virtualenv.sh", "graderutilsenv", "python3", "-m", "graderutils.main", "test_config.yaml"]
      time: 20
      memory: 500m
      disk: 0
      html: True

Then, create a new **config.yaml** file. Copy the ``view_type`` and ``files``
sections from **config_old.yaml** to this file. **NOTE**: you don't need to
define a ``feedback_template`` anymore if it is a typical template. If you
need a specific template, see `pull request 19 of mooc-grader
<https://github.com/Aalto-LeTech/mooc-grader/pull/19>`_.

Write also a new part ``container``:

config.yaml
...........

.. code-block:: yaml

  view_type: access.types.stdasync.acceptFiles
  files:
    - field: file1
      name: laskesumma.py

  container:
    image: apluslms/grade-python:3.6-2.7
    mount: python1/laskesumma/
    cmd: graderutils

- The ``image`` setting defines the grading container and its version to be
  used.

- The ``mount`` setting must have the same relative directory path than the
  ``actions: cp_exercises`` setting in **config_old.yaml**.

- The ``cmd`` setting describes what command is run inside the grading
  container. By default, use ``cmd: graderutils``, which calls a shell script
  that does the same than the ``cmd`` setting in **config_old.yaml**.
  You can also create a **run.sh** script file (see below); then the line will
  be ``cmd: /exercise/run.sh``.

You cannot define resource limits, such as execution time and memory, anymore
in **config.yaml**. These must be set in the **run.sh** script.

run.sh
......

This is an optional Unix shell script which can be created in the same
directory as the exercise **config.yaml** file and other files. It allows all
kinds of additional setup inside the container. Below is a real example from
a Python programming exercise "Hunt" from the course Data Structures and
Algorithms Y.

The exercise is located at directory ``exercises/programming/hunt`` in the
course directory. The directory listing in UNIX shell is the following:

.. code-block:: none

  t31300-lr124 hunt 1016 % ls -l
  total 36
  -rw-r--r-- 1 atilante domain users  328 Aug 31 16:22 config.yaml
  -rw-r--r-- 1 atilante domain users 3272 May 31 11:22 grader_tests.py
  -rw-r--r-- 1 atilante domain users 1518 May 31 11:22 hunt.py
  -rw-r--r-- 1 atilante domain users 1615 May 31 11:22 level_generator.py
  -rw-r--r-- 1 atilante domain users 2054 May 31 11:22 model.py
  -rwxr-xr-x 1 atilante domain users  683 Oct 29 16:19 run.sh*
  -rw-r--r-- 1 atilante domain users  521 May 31 11:22 test_config.yaml
  drwxr-xr-x 2 atilante domain users 4096 May 31 11:22 testdata/
  -rw-r--r-- 1 atilante domain users 1408 May 31 11:22 tests.py
  t31300-lr124 hunt 1017 % ls -l testdata
  total 28
  -rw-r--r-- 1 atilante domain users 2555 May 31 11:22 eldorado.txt
  -rw-r--r-- 1 atilante domain users   56 May 31 11:22 gamble.txt
  -rw-r--r-- 1 atilante domain users 2554 May 31 11:22 large.txt
  -rw-r--r-- 1 atilante domain users   34 May 31 11:22 small2.txt
  -rw-r--r-- 1 atilante domain users   62 May 31 11:22 small3.txt
  -rw-r--r-- 1 atilante domain users   56 May 31 11:22 small.txt
  -rw-r--r-- 1 atilante domain users 2552 May 31 11:22 trapped.txt

As you can see, there are several files.

- **config.yaml** is the main configuration file for A+ and mooc-grader.
- **grader_tests.py** contains the secret Python unit tests run on the grader.
- **hunt.py** is the exercise code template given to the student.
- **level_generator.py** is an extra tool used by **grader_tests.py**.
- **model.py** is the model solution for the exercise, used by **grader_tests.py**.
- **run.sh** is the grading script
- **test_config.yaml** is the configuration file for Python-grader-utils
- **testdata** is a directory containing test inputs given to the student.
- **tests.py** has Python unit tests both given to the student and run on the grader.

File **config.yaml** looks like this:

.. code-block:: none

  ---
  :title: Hunt
  description: Ohjelmointitehtävä / Programming exercise

  view_type: access.types.stdasync.acceptFiles
  files:
    - field: file1
      name: hunt.py
  template_files:
    - exercises/programming/hunt/hunt.py

  container:
    image: apluslms/grade-python:3.5-2.2
    mount: exercises/programming/hunt
    cmd: /exercise/run.sh

The student must submit one file, which will be saved as
``/submission/user/hunt.py`` inside the grading container.
``template_files`` tells
`Radar (plagiarism detector) <../m02_programming_exercises/05_radar>`_
what parts of code is similar in all student submissions. The ``cmd`` setting
under ``container`` instructs to run the **run.sh** file, which is located
under directory ``/exercise`` inside the container.

The contents of **run.sh** looks like this:

.. code-block:: none

  #!/bin/bash

  # The working directory is /submission/user which has the user-submitted files
  # defined in config.yaml.

  # The mount directory from config.yaml is in /exercise (read only).
  # Copy files related to unit testing to /submission/user.
  cp -r /exercise/testdata .

  # 60 seconds of CPU time, 500 MB of virtual memory
  ulimit -t 60 -v 524288

  # Run python-grader-utils with settings file test_config.yaml.
  # The output will be in /feedback/err and /feedback/out
  # https://github.com/aalto-letech/python-grader-utils
  # https://github.com/apluslms/grade-python
  # 120 seconds of wall clock time
  timeout 120 graderutils

The comments in the file are quite self-explanatory. The script uses the
well-known `Bash Unix shell <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_.
Essentially, inside the grading container the directory ``/exercise`` is the
same as the directory ``exercises/programming/hunt`` outside the container, and
its files are exactly as in the directory listings above. The student has
submitted their solution, which is now at ``/submission/user/hunt.py``. When
the **run.sh** begins, the current working directory is ``/submission/user``.

Because this exercise needs test data, those test data files are copied from
``/exercise/testdata`` to ``/submission/user``.

``ulimit`` is BASH command; see ``man bash`` for details. It sets the *CPU
time* and amount of virtual memory that Python, Python-grader-utils and the
student's program can together use when they are executed.

``timeout`` is part of `GNU coreutils <http://www.gnu.org/software/coreutils/>`_
and also availabe inside the container. It sets the *wall clock time limit*
for the exercise grading.

As a whole, the script copies test data files to the user submission directory
and then executes the `graderutils script <https://github.com/apluslms/grade-python>`_
with 120 seconds of wall clock time, 60 seconds of CPU time and 500 MB of
virtual memory.

One should set both the CPU time and wall clock time. The CPU time limits the
actual amount of computation that the student's solution can use. The wall clock
time prevents the grading from sleeping forever, like by calling `time.sleep()
<https://docs.python.org/3/library/time.html#time.sleep>`_ inside the Python
program. A rule of thumb is that the wall clock time should be double the CPU
time, and the CPU time should be 60 seconds. Note that if you run A+ and
mooc-grader on your own computer and test grading of a model solution, the
execution time is likely less than on the production server. Moreover, some
student solutions which produce valid result might take longer time than the
model solution, therefore one minute is a good rule of thumb.

The resource limits are set for extra security. The A+ and mooc-grader running
on the servers of Aalto Department of Computer Science have wall clock time
limit of *some hours* for each exercise submission, which is still a limit, but
too much in most cases.

Also note that currently, if the CPU or wall clock time limits are hit, the
student will only see a message "No grader feedback available for this
submission". This likely causes confusion.

Note that **if you create a run.sh file, set the executing permissions**.
That is, after first time saving the file, give the following command in the
exercise directory:

.. code-block:: none

  chmod a+x run.sh

If you forget that, when you finally test the exercise, you will see the
surprising "No grader feedback available for this submission" error message.
Furthermore, if you then inspect the exercise submission in A+, you will see
that mooc-grader has given the following **feedback**:

.. code-block:: none

  gw: 18: /gw: /exercise/run.sh: Permission denied
  Received exit code 126 from: /exercise/run.sh r2p01
  Points '' is not a valid number.
  Max points '' is not a valid number."

The "/exercise/run.sh: Permission denied" indicates exactly that you must
enable the execution rights for **run.sh**. See ``man chmod`` for details.
