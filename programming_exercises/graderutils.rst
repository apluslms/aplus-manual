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

The following example shows how to embed arbitrary JavaScript into the feedback template,
and make data from grader tests available for the scripts.

.. figure:: /images/embedded_plot.png
  :align: center

.. submit:: plot 10
  :config: exercises/embedded_plot/config.yaml
  :title: Embedding a plot

  Notice that this exercise uses the Docker container image
  ``apluslms/grade-python:math-3.7-4.2-3.5`` because it includes the plotting library Bokeh.

  You can submit the file **solution_wrong.py** to see the feedback.


IOTester
--------

Input and output of a program can be compared against the input and output of a model program by
using the test methods provided by
`IOTester <https://github.com/apluslms/python-grader-utils/blob/master/graderutils/iotester.py>`_,
which is part of Graderutils.

``IOTester`` can be used to feed inputs and/or parameters to a program/function. The output of the
student program and model program are captured and compared in different ways depending on
the used tests (``text_test``, ``numbers_test``, etc.) and colored feedback showing the differences
is given. Google's ``diff_match_patch`` is used for the detection and coloring of the differences.
Tools for testing things like return values and classes/objects are also available, among
other things.

Below are some examples of the useful tests/tools:

- **text_test**

    Run the model program and the student program and compare the text outputs.
    Ignore numbers, whitespace and characters specified in ``self.settings["ignored_characters"]``.

    Parameters:

    - ``func_name`` (default: ``""``)

        Name of the function to be tested. This is shown in the feedback.

        If ``func_name`` is an empty string, the program is imported and the code on the
        module-level is executed. If the program contains function ``main()`` but it has not been
        called, the test fails with an error message ``Function main() was found but it was not
        called. Make sure that you remember to call the main() function
        and that the function call is correctly indented.``

    - ``args`` (default: ``()``)

        Tuple or list of positional arguments that are passed to the function with name
        ``func_name``. This is shown in the feedback.

    - ``kwargs`` (default: ``{}``)

        Dictionary of keyword arguments that are passed to the function with name
        ``func_name``. This is shown in the feedback.

    - ``inputs`` (default: ``[]``)

        List of strings that are fed to the program as input when prompted. This is shown in the
        feedback.

        Each string acts as if the user would have typed it and pressed Enter. To simulate a user
        not typing anything and only pressing Enter, import and use the ``ENTER`` variable from
        ``IOTester`` as the string.

    - ``prog`` (default: ``None``)

        Function that is run instead of a Python module. This is useful in cases where you want
        to do something before/after running the function that is being tested. For example, if
        the student submits a Python class, you might want to create an instance of the class with
        some specific initial values and then call the object's method to see if it returns the
        correct value.

        Note that ``func_name`` is shown in the feedback as the name of the function
        that was tested, ``args`` and ``kwargs`` are shown as the used parameter values, and
        ``inputs`` is shown as the used input. This is so that the function ``prog`` can have
        different (hidden) args, kwargs and inputs than the actual function that is tested.

    - ``prog_args`` (default: ``()``)

        Tuple or list of positional arguments that are passed to the function ``prog`` if it is
        defined.

    - ``prog_kwargs`` (default: ``{}``)

        Dictionary of keyword arguments that are passed to the function ``prog`` if it is defined.

    - ``prog_inputs`` (default: ``[]``)

        List of strings that are fed to the function ``prog`` if it is defined.

    - ``desc`` (default: ``""``)

        String with a custom description/hint for the test. This is shown in the feedback.

    - ``compare_capitalization`` (default: ``False``)

        Boolean variable stating if capitalization differences in the output should trigger an
        AssertionError or not.

- **numbers_test**

    Run the model program and the student program and compare the numbers in the outputs.
    Ignore everything except numbers.
    Match integers, decimals and numbers such as +1, 2e9, +2E+09, -2.0e-9.

    Parameters (some of them already explained earlier):

    - ``func_name`` (default: ``""``)

    - ``args`` (default: ``()``)

    - ``kwargs`` (default: ``{}``)

    - ``inputs`` (default: ``[]``)

    - ``prog`` (default: ``None``)

    - ``prog_args`` (default: ``()``)

    - ``prog_kwargs`` (default: ``{}``)

    - ``prog_inputs`` (default: ``[]``)

    - ``desc`` (default: ``""``)

    - ``compare_formatting`` (default: ``False``)

        Boolean variable stating if formatting differences in the numbers should trigger an
        AssertionError or not. For example, 0.750 vs 0.75 and 0005 vs 5.

- **return_value_test**

    Run a function from the model program and the student program and compare the return values of
    the two functions.

    Parameters (some of them already explained earlier):

    - ``func_name`` (default: ``""``)

    - ``args`` (default: ``()``)

    - ``kwargs`` (default: ``{}``)

    - ``inputs`` (default: ``[]``)

    - ``prog`` (default: ``None``)

    - ``prog_args`` (default: ``()``)

    - ``prog_kwargs`` (default: ``{}``)

    - ``prog_inputs`` (default: ``[]``)

    - ``desc`` (default: ``""``)

    - ``show_output`` (default: ``False``)

        Boolean variable stating if the output of the student program should be shown in the
        feedback. Showing the output might help students debug their program.

- **complete_output_test**

    Run the model program and the student program and compare the text, numbers and whitespace.
    Ignore characters specified in ``self.settings["ignored_characters"]``.

    Parameters are identical to **text_test**:

    - ``func_name`` (default: ``""``)

    - ``args`` (default: ``()``)

    - ``kwargs`` (default: ``{}``)

    - ``inputs`` (default: ``[]``)

    - ``prog`` (default: ``None``)

    - ``prog_args`` (default: ``()``)

    - ``prog_kwargs`` (default: ``{}``)

    - ``prog_inputs`` (default: ``[]``)

    - ``desc`` (default: ``""``)

    - ``compare_capitalization`` (default: ``False``)

- **no_output_test**

    Run the student program and test that nothing is printed.

    Parameters (already explained earlier):

    - ``func_name`` (default: ``""``)

    - ``args`` (default: ``()``)

    - ``kwargs`` (default: ``{}``)

    - ``inputs`` (default: ``[]``)

    - ``prog`` (default: ``None``)

    - ``prog_args`` (default: ``()``)

    - ``prog_kwargs`` (default: ``{}``)

    - ``prog_inputs`` (default: ``[]``)

    - ``desc`` (default: ``""``)

- **created_file_test**

    Run the model program and the student program and compare the data in the file they create.
    The data in the two files has to be identical. This test fails with an error if the student
    program does not create a file with the correct name specified by parameter ``file_name``
    (see below).

    Parameters (some of them already explained earlier):

    - ``file_name`` (required)

        Name of the file that the student program and model program should create.
        This is shown in the feedback.

    - ``func_name`` (default: ``""``)

    - ``args`` (default: ``()``)

    - ``kwargs`` (default: ``{}``)

    - ``inputs`` (default: ``[]``)

    - ``prog`` (default: ``None``)

    - ``prog_args`` (default: ``()``)

    - ``prog_kwargs`` (default: ``{}``)

    - ``prog_inputs`` (default: ``[]``)

    - ``desc`` (default: ``""``)

- **random_state_test**

    Run the model program and the student program and compare Python's pseudo-random number
    generator states. Used to test a function that sets random seed and to check that a program
    generates pseudo-random numbers the correct amount of times.

    Parameters (already explained earlier):

    - ``func_name`` (default: ``""``)

    - ``args`` (default: ``()``)

    - ``kwargs`` (default: ``{}``)

    - ``inputs`` (default: ``[]``)

    - ``prog`` (default: ``None``)

    - ``prog_args`` (default: ``()``)

    - ``prog_kwargs`` (default: ``{}``)

    - ``prog_inputs`` (default: ``[]``)

    - ``desc`` (default: ``""``)

- **amount_of_functions_test**

    Test that the student program contains the required amount of functions.

    ``NOTE:`` Breaks if `graderutils flag <https://github.com/apluslms/grade-python#utility-commands>`_
    ``--use-rpyc`` is used while the module contains custom classes.

    Parameters (some of them already explained earlier):

    - ``op`` (required)

        One of the following strings: ``">"``, ``"<"``, ``">="``, ``"<="``, ``"=="``

        This specifies the operator used for the comparison. For example, with ``">"`` as ``op`` and
        ``2`` as ``amount`` the test will pass if the student program contains more than two
        functions.

    - ``amount`` (required)

        Integer that the number of found functions is compared against using operator ``op``.

    - ``desc`` (default: ``""``)
