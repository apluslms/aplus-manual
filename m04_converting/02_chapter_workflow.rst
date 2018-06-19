The workflow for converting a chapter
=====================================

This section proposes a workflow for converting a chapter (or "module") in a
non-Docker A+ course for the Docker version. It assumes that the initialisation
described in `the previous chapter <01_virtualenv_to_docker.html>`_ is
completed. See the earlier chapter ``Instructions
<../m02_programming_exercises/instructions.html>``_ in the Programming exercises
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

    Check possible compilation errors in the reminal. Then view the course
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
    image: apluslms/grading-python:3.5
    mount: python1/laskesumma/
    cmd: graderutils

- The ``image`` setting defines the grading container and its version to be
  used.

- The ``mount`` setting must have the same relative directory path than the
  ``actions: cp_exercises`` setting in **config_old.yaml**.

- The ``cmd`` setting describes what command is run inside the grading
  container. By default, use ``graderutils``, which is a shell script that
  does the same than the ``cmd`` setting in **config_old.yaml**.

You cannot define resource limits, such as execution time and memory, anymore
in **config.yaml**. TODO: grading-containers-resurssirajat.txt.
