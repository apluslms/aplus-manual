Exercises with Python grader utils
==================================

This chapter includes exercises that utilise the
`Python-grader-utils <https://github.com/apluslms/python-grader-utils>`_
framework, which is recommended if you are creating Python exercises.

.. submit:: hello 10
  :config: exercises/hello_python_graderutils/config.yaml
  :title: Hello Python with Python grader utils

  In this exercise you must implement a function ``hello``
  that returns a string ``"Hello Python!"``.

The following is an example of a graderutils exercise, where the problem is to implement a simple prime number checker ``primes.is_prime``.
An incorrect solution can be found in **primes.py**, which is compared against the reference solution **model.py**.

Run the tests to get test results in JSON (use develop mode to generate all errors and warnings):
``python3 -m graderutils.main test_config.yaml --develop-mode > results.json``
Convert the JSON results into HTML:
``cat results.json | python3 -m graderutils_format.html --full-document > results.html``
You can now view **results.html** in a browser.

If you don't want to render the `base template <https://github.com/apluslms/python-grader-utils/blob/master/graderutils_format/templates/base.html>`_, you can omit `--full-document`.
This renders only the feedback body using the default `feedback template <https://github.com/apluslms/python-grader-utils/blob/master/graderutils_format/templates/feedback.html>`_.


.. submit:: primes 10
  :config: exercises/primes/config.yaml
  :submissions: 99
  :title: Primes with Python grader utils

  In this exercise, you must implement the function ``is_prime``
  that returns ``True`` if the argument (integer) is a prime number,
  ``False`` otherwise.

Paths to custom Jinja2 HTML templates that extend or replace the default
template at `graderutils_format/templates/feedback.html
<https://github.com/apluslms/python-grader-utils/blob/master/graderutils_format/templates/feedback.html>`_
can be defined in the **test_config.yaml** as follows:

::

  feedback_template: my_feedback_template.html

.. submit:: template 10
  :config: exercises/template_extension/config.yaml

The following example shows how to embed arbitrary JavaScript into the feedback template, and make data from grader tests available for the scripts.

.. figure:: /images/embedded_plot.png
  :align: center

.. submit:: plot 10
  :config: exercises/embedded_plot/config.yaml
  :title: Embedding a plot

  Notice that this exercise uses the Docker image ``apluslms/grade-python:math-3.7-4.2-3.5`` because it includes the plotting library Bokeh.

  You can submit the file **solution_wrong.py** to see the feedback.
