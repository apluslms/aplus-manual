The workflow for converting a chapter
=====================================

This section proposes a workflow for converting a chapter (or "module") in a
non-Docker A+ course for the Docker version. It assumes that the initialisation
described in `the previous chapter <01_virtualenv_to_docker.html>`_ is
completed.

Add the RST files of the module
-------------------------------

1.  Move the RST directory of the next module that is not yet converted
    from ``old`` to the main directory. For example:

    .. code-block:: none

        git mv old/python1 python1

2.  Add the index file of that module to the main ``index.rst``.
    In the example below, the module is ``python1`` and its index file is
    ``kierros.rst``. Delete the A+ manual course modules in that file, or
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
    coded directly in the RST files should work.


Modify exercise grading files
-----------------------------
