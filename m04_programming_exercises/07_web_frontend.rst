Web frontend exercises
======================

JavaScript: Clock
-----------------

This is a real, former exercise from the course "Computing Applications"
(Tietotekniikka sovelluksissa).

Exercise instructions
.....................

Open the exercise template ``clock.html`` (exercises/clock/clock.html) and
implement the following JavaScript functionality.

1. First, create a JavaScript function which changes the text in the H1 heading
   in the template to "Hello World".

2. Then modify the function so that the heading has current time in the format
   ``hh:mm:ss``.

You can access the time and date by the JavaScript object ``Date()``. You can,
for example, read the hours as an integer in the following way:

.. code-block:: javascript

    var pvm = new Date();
    var hours = pvm.getHours();

You can read minutes and seconds by methods ``getMinutes`` and ``getSeconds()``,
respectively.

**NOTE! At this point, the clock does not need to work correctly with numbers
less than ten. (See part 4.)**

**Hint.** \ Unlike Python, in JavaScript one can concatenate a string with a
string *and* a string with an integer. The integer is automatically converted
into a string and the result is a string. Example:

.. code-block:: javascript

    "ABC" + "1" + 23 ==> "ABC123"

3. Modify your code so that the clock updates in 100 millisecond intervals.

.. admonition:: Calling a function repeatedly
  :class: note

  If you replace the function call ``func_name()`` with function
  ``setInterval(func_name, time)``, JavaScript will begin to call the function
  ``func_name()`` repeatedly with intervals. The ``time`` is in milliseconds.

You will notice that the clock does not still work quite right. If a number is
less than ten, the leading zero is not shown, because the times are integers.

4. Write a function which adds a leading zero to a number if the number is
   less than ten. Use this function to correct the clock.

5. Modify the clock function so that the text in the H1 element has color
   red on even seconds and color blue on odd seconds.

**Hint:** ``a % b`` computes a division remainder. See also: `arithmetic
operations in JavaScript
<https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Remainder>`_.

.. submit:: clock 10
  :config: exercises/clock/config.yaml
  :title: Clock


Model solution
..............

The model solution fto this exercise is in the aplus-manual directory
**exercises/clock/model_answer.html**.


Description of the grader
.........................

The exercise files are in the directory **exercises/clock/**.

The grader uses Python and Graderutils, just like described in the
:doc:`Instructions </m04_programming_exercises/01_instructions>`. Essentially, it uses `Selenium
<https://www.seleniumhq.org/>`_ and the `related Python package
<https://pypi.org/project/selenium/>`_ to run the tests. This means that it
starts a web browser which actually renders the web page and runs the
JavaScript.

**config.yaml** uses **apluslms/grading-python-web** as the grading container.
This
