Hello programming
=================

This chapter includes three exercises on one page. Questionnaires and
submission forms can exist anywhere and as many on one page as required.
The automatic assessment of a submission is defined in the referenced
YAML file.

This is the configuration file ``docker-compose.yml``:

.. include:: ../docker-compose.yml
  :code: yaml

Note: acos is an optional component used for interactive exercises.

.. submit:: python 10
  :config: exercises/hello_python/config.yaml

.. submit:: scala 10
  :config: exercises/hello_scala/config.yaml

.. submit:: javascript 10
  :config: exercises/hello_javascript/config.yaml

Be careful with the RST and YAML syntaxes. They are too easy to break
with blank space and indentations.


Hello Python: grading steps in detail
-------------------------------------

The following description is targeted for people who develop automatically
assessed exercises. Details on how A+ and mooc-grader work are omitted.

#. The student submits the file **functions.py** to A+.

#. A+ requests mooc-grader to grade a Hello Python exercise with the
   submitted file. Information about the student is not sent to the mooc-grader.

#. Mooc-grader knows from **exercises/hello_python/config.yaml** that it must
   start a new instance of Docker container **apluslms/grade-python:3.6-2.7**.

#. Docker reads the `grade-python <https://github.com/apluslms/grade-python>`_
   container image and starts it. A minimal Debian GNU/Linux operating system
   starts inside it. Because the aforementioned **config.yaml** has a
   ``container: mount:`` subsection, the directory **exercises/hello_python**
   in the aplus-manual directory is set visible inside the grade-python
   containes in the directory **/exercise** (read-only).

#. The file **functions.py** is copied inside the grade-python container into
   ``/submission/user/functions.py``.

The following steps are executed inside the grade-python container.

#. Docker runs the command ``/exercise/run.sh`` inside the grade-python
   container, because the config.yaml file has the subsection
   ``container: cmd``. That is, the **run.sh** script inside the exercise
   directory - outside ``exercises/hello_python/run.sh``, inside
   ``/exercise/run.sh`` - is executed.

#. The first line of **/exercise/run.sh** is the hashbang ``#!/bin/bash``, therefore
   a BASH shell is invoked to interpret the script.

#. run.sh line ``export PYTHONPATH=/submission/user`` is executed. The
   environment variable `PYTHONPATH <https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH>`_
   is set.

#. run.sh line ``capture python3 /exercise/tests.py`` is executed. Because the
   `Dockerfile of the container apluslms/grade-python
   <https://github.com/apluslms/grade-python/blob/master/Dockerfile>`_ has
   ``FROM apluslms/grading-base:$BASE_TAG``, it is based on another container
   `apluslms/grading-base <https://github.com/apluslms/grading-base>`_.

#. BASH finds the ``capture`` command at ``/bin/capture``. It is another BASH
   script which is coming from the grading-base container (`source here
   <https://github.com/apluslms/grading-base/blob/master/bin/capture>`_).

#. The first line of **/bin/capture** is the hashbang ``#!/bin/sh``, therefore
   a Dash shell is invoked to interpret the script. This script defines two
   variables:

   ::

     out = /feedback/out
     err = /feedback/err

   The **capture** script sets up to redirect the output from the Python
   intepreter (command ``python3``): `standard output stream
   <https://en.wikipedia.org/wiki/Standard_streams>`_ to the file
   **/feedback/out** and the standard error stream to the file
   **/feedback/err**. Both streams must be saved, because when Python is
   running unit tests, it prints into both the standard output and standard
   error streams.
