Hello Worlds
============

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

The sequence begins from the client side.

1. The student submits the file **functions.py** to A+.

The following occurs in the server side.

2. A+ requests mooc-grader to grade a Hello Python exercise with the
   submitted file. Information about the student is not sent to the mooc-grader.

3. Mooc-grader knows from **exercises/hello_python/config.yaml** that it must
   start a new instance of Docker container **apluslms/grade-python:3.9-4.4-4.0**.

4. Docker reads the `grade-python <https://github.com/apluslms/grade-python>`_
   container image and starts it. A minimal Debian GNU/Linux operating system
   starts inside it. Because the aforementioned **config.yaml** has a
   ``container: mount:`` subsection, the directory **exercises/hello_python**
   in the aplus-manual directory is set visible inside the grade-python
   container in the directory **/exercise** (read-only).

5. The file **functions.py** is copied inside the grade-python container into
   ``/submission/user/functions.py``.

The directory structure inside the grade-python container is now essentially
this:

::

  /
  ├── bin
  |   ├── _prewrap
  |   ├── bash
  |   ├── capture
  |   ├── err-to-out
  |   ├── grade
  |   ├── sh
  ├── exercise
  |   ├── config.yaml
  |   ├── grader_tests.py
  |   ├── model.py
  |   ├── run.sh
  |   └── solution_wrong.py
  ├── feedback
  |   └── grading-script-errors
  ├── gw
  ├── submission
  |   └── user
  |       └── functions.py
  └── usr
      ├── bin
      |   └── python3
      └── local
          └── lib
              └── python3.9
                  └── dist-packages
                      └── graderutils
                          └── graderunittest.py


The following steps are executed inside the grade-python container.

6. Docker runs the command ``/gw`` insinde the grade-python container. This
   is the main grading script, "grade wrapper", and it comes from the
   grading-base container. The script is run in Dash (/bin/sh). The wrapper
   script will take care of redirecting output (stdout and stderr;
   see `standard streams`_ on Wikipedia) from the programs it
   calls to the file ``/feedback/grading-script-errors``. In addition, the
   ``gw`` script will make sure that the working directory is set correctly.

   That is, **gw** changes the current working directory
   to ``/submission/user`` .

   (Reference: `README.md <https://github.com/apluslms/grading-base>`_ and the
   `gw script <https://github.com/apluslms/grading-base/blob/master/rootfs/gw>`_
   in grading-base.)

7. Because the config.yaml file has the subsection
   ``container: cmd``, the command ``/exercise/run.sh`` is given to the ``gw``
   script as a command line parameter. In this case, ``gw`` executes the
   run.sh file.

8. The first line of **/exercise/run.sh** is ``#!/bin/bash``, therefore
   a BASH shell is invoked to interpret the script.

9. run.sh line ``export PYTHONPATH=/submission/user`` is executed. The
   environment variable `PYTHONPATH <https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH>`_
   is set.

10. run.sh line ``capture python3 /exercise/grader_tests.py`` is executed. Because the
    `Dockerfile of the container apluslms/grade-python
    <https://github.com/apluslms/grade-python/blob/master/Dockerfile>`_ has
    ``FROM apluslms/grading-base:$BASE_TAG``, it is based on another container
    `apluslms/grading-base <https://github.com/apluslms/grading-base>`_.

11. BASH finds the ``capture`` command at ``/bin/capture``. It is another BASH
    script which is coming from the grading-base container. (`contents of the
    script
    <https://github.com/apluslms/grading-base/blob/master/bin/capture>`_).

12. The first line of **/bin/capture** is the hashbang ``#!/bin/sh``, therefore
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

13. Now the Python intepreter is called with the parameter ``/exercise/grader_tests.py``.
    The current working directory is still ``/submission/user``.

14. Inside **grader_tests.py**, the main level script is executed:

    ::

      if __name__ == '__main__':
          # Run tests from the test case and get result
          loader = unittest.defaultTestLoader
          suite = loader.loadTestsFromTestCase(TestHelloPython)
          runner = graderunittest.PointsTestRunner(verbosity=2)
          result = runner.run(suite)
          # Points are read from stdout and saved
          print("TotalPoints: {}\nMaxPoints: {}".format(result.points, result.max_points))

    The `Python unit testing framework <https://docs.python.org/3/library/unittest.html>`_
    is invoked. However, the *test runner* is set to
    ``graderunittest.PointsTestRunner``. This is from the `Python-grader-utils
    <https://github.com/apluslms/python-grader-utils>`_, which is included
    in the apluslms/grade-python container. The class *PointsTestRunner* is
    in the file `graderunittest.py <https://github.com/apluslms/python-grader-utils/blob/master/graderutils/graderunittest.py>`_.
    For the details, Graderutils is inside the grade-python container at
    ``/usr/local/lib/python3.9/dist-packages/graderutils``.

15. The Python module *graderutils* runs a *PointsTestRunner* instance. First it
    uses the Python unit test framework to run the methods
    ``test_function()``, ``test_import()``, and ``test_return()`` from the
    class ``TestHelloPython`` in the **grader_tests.py**. These test methods are
    recognized as unit tests and run in alphabetical order, because their name
    begins with ``test``. (Reference: `Python unittest library
    <https://docs.python.org/3/library/unittest.html#organizing-test-code>`_)

16. The Python unit testing framework will print a typical unit test output
    into standard error stream. In the following snippet the solution was correct.

    ::

      test_function (__main__.TestHelloPython)
      Check hello function exists (1p) ... ok
      test_import (__main__.TestHelloPython)
      Import the functions module (1p) ... ok
      test_return (__main__.TestHelloPython)
      Check hello function return value (3p) ... ok

      ----------------------------------------------------------------------
      Ran 3 tests in 0.001s

      OK

17. Because ``test_function`` has the docstring
    ``"""Check hello function exists"""``, Graderutils will show this
    as the title of the test. The decorator ``@points(1)`` grants five points
    if the test passes. Similarly, ``test_import`` also
    yields one point if it passes and ``test_return`` will yield three points if
    it passes.

18. The points data is printed into standard output stream:

    ::

      TotalPoints: 5
      MaxPoints: 5

19. The ``capture`` script will redirect the output. This results in two files
    as promised.

    **/feedback/err**:

    ::

      test_function (__main__.TestHelloPython)
      Check hello function exists (1p) ... ok
      test_import (__main__.TestHelloPython)
      Import the functions module (1p) ... ok
      test_return (__main__.TestHelloPython)
      Check hello function return value (3p) ... ok

      ----------------------------------------------------------------------
      Ran 3 tests in 0.001s

      OK

    **/feedback/out**:

    ::

      TotalPoints: 5
      MaxPoints: 5

20. Now ``capture`` exits. The execution continues in **run.sh**, which will
    next call ``err-to-out`` (in /bin/err-to-out; `source here <https://github.com/apluslms/grading-base/blob/master/bin/err-to-out>`_).
    This uses the ``_prewrap`` to add HTML <pre> tags and append the standard
    error output after the standard output. Result:

    **/feedback/out**:

    ::

      TotalPoints: 5
      MaxPoints: 5

      <pre>
      test_function (__main__.TestHelloPython)
      Check hello function exists (1p) ... ok
      test_import (__main__.TestHelloPython)
      Import the functions module (1p) ... ok
      test_return (__main__.TestHelloPython)The
      Check hello function return value (3p) ... ok

      ----------------------------------------------------------------------
      Ran 3 tests in 0.001s

      OK
      </pre>


21. After the grading script has been executed, the grade wrapper script
    ``/gw`` will execute script **grade** (in ``/bin/grade``). This will parse
    the data in **/feedback/out**: first points, then the text feedback.

22. The exit code from the grade wrapper script ``/gw`` is stored in
    ``/feedback/grading-script-errors``. The grade wrapper always exits with
    code 0.

The rest is executed outside the grade-python container.

23. The container grade-python shuts down. Points and feedback are sent to
    mooc-grader.

24. Mooc-grader forwards the data to A+.

25. A+ records the points and feedback as new exercise submission, which is
    unique for this particular user, course, exercise and submission attempt.
    A+ scales the points according to the maximum points setting in the
    **config.yaml** of the exercise (if the maximum score given by the grader
    differs from that).

The rest is executed at the client side.

26. The JavaScript at the web browser gets a response from A+ that the grading
    is ready. Thus the JavaScript shows the points and the feedback. The feedback
    is just interpreted as HTML. This is why it had to be wrapped into HTML
    <pre> tags.

.. _standard streams: https://en.wikipedia.org/wiki/Standard_streams
