Creating questionnaire exercises
================================

One can easily create simple questionnaire exercises for an A+ course, such as
one-line text answers and multiple choice exercises. This page shows many
examples on these.

*Technical remark.* The most recent and complete documentation on this can
be found at `the source code of the A+ RST tools package
<https://github.com/Aalto-LeTech/a-plus-rst-tools>`_. Technically A+ RST tools
provide specific Sphinx directives for writing course HTML and configuration
files, and then A+ and mooc-grader implement the actual functionality.

General description of the options
----------------------------------

The ``questionnaire`` directive implements a questionnaire exercise. Its
arguments define the exercise key (exercise identifier for A+) and max points
with the optional difficulty (``A``, ``B``, ``C``, etc.). For example,
``.. questionnaire:: easyexercise A50`` sets key to ``easyexercise``,
maximum points to ``50`` and difficulty ``A``. The difficulty parameter
does not affect any scorekeeping, but only works as an indicator for the
student. (The A+ REST API can group earned points by the difficulty so that
the teacher may use the difficulties for computing final course grades.)

The questionnaire directive accepts the following options:

* ``submissions``: max submissions
* ``points-to-pass``: points to pass
* ``feedback``: If set, assumes the defaults for a feedback questionnaire
* ``no-override``: If set, the conf.py override setting is ignored
* ``pick_randomly``: integer. Set the pick_randomly setting for the quiz
  (select N questions randomly on each load)
* ``category``: exercise category

The contents of the questionnaire directive define the questions and possible
instructions to students.

The **question directives** ``pick-one``, ``pick-any``, and ``freetext`` take
the points of the question as the first argument. The sum of the question points
should be equal to the questionnaire max points. The question directives accept
the following options:

* ``class``: `CSS class <css>`_
* ``required``: If set, the question is required and empty answers are rejected
* ``key``: a manually set key for the question. This affects the HTML **input**
  element and the key in the submission data. If no key is set, note that
  automatically added keys change when the order and amount of questions is
  modified.

The ``freetext`` directive also accepts the following options in addition to
the common question options:

* ``length``: (horizontal) length for the HTML text input in characters
* ``height``: vertical height of the text input in rows. If this is greater than
  1, the **textarea** HTML element is used. Otherwise, a text input is used.
* Also other options are defined in the `questionnaire code of A+ RST tools
  <https://github.com/Aalto-LeTech/a-plus-rst-tools/blob/master/directives/questionnaire.py>`_,
  but they mainly affect the CSS classes and they were implemented for very
  narrow usecases.

The ``freetext`` directive accepts a second positional argument after the points.
It defines the compare method for the model solution. A textual input can be
compared with the model solution as ``int``, ``float``, ``string``,
or ``unsortedchars`` (unsorted character set). Another option is ``regexp``
which takes the correct answer as a regular expression and tries to match the
submission with it using the `Python re library <https://docs.python.org/3/library/re.html>`_.

Strings have comparison modifiers that are separated with a hyphen (``-``).
For example, to create a freetext question which compares the answer to the
correct answer as string, and ignores whitespace characters and quotes, write
``.. freetext:: 30 string-ignorews-ignorequotes``.

* ``ignorews``: ignore whitespace (all space characters, applies to regexp too)
* ``ignorequotes``: iqnore quotes ``"`` around
* ``requirecase``: require identical lower and upper cases (only with the string type)
* ``ignorerepl``: ignore REPL prefixes
* ``ignoreparenthesis``: ignore parenthesis ``( )``

The question directives may define instructions. After the instructions,
the contents of the directive define the choices, the correct solution, and
possible hints. The hints are targeted to specific choices and they are shown
after answering. See the example below.

Examples
--------

.. questionnaire:: questionnaire_demo 20
  :title: A simple multiple-choice questionnaire
  :submissions: 3

  .. pick-one:: 10

    Subdirective ``pick-one`` defines a single-choice question.
    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    a § Not quite. Remember the cube root.
    b § Correct!
    c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.

  .. pick-any:: 10

    Subdirective ``pick-any`` defines a multiple-choice question.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    a. 4
    *b. an integer
    *c. 3
    d. an irrational number
    e. -3
    *f. -5

    a § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.
    b § Correct!
    c § Correct!
    d § No. This equation has a nice and easy solution.
    e § Remember that :math:`x^2 = q \leftrightarrow x = \pm \sqrt{q}`
    f § Correct!

The ``freetext`` subdirective creates text boxes and grades based on their
input.

.. questionnaire:: questionnaire_text_demo 15
  :title: A simple multiple-choice questionnaire
  :submissions: 3

  .. freetext:: 5
    :length: 10

    This is the most basic free text questionnaire. The correct answer is
    ``test``. You can write at most 10 characters into the box.

    test
    !test § Follow the instruction.


  .. freetext:: 5 int
    :length: 7

    The answer can be a number, an integer. What is :math:`3 + 8`?

    11
    !11 § Follow the instructions.


  .. freetext:: 5 float
    :length: 7

    The answer can also be a decimal number (floating point number).
    What is :math:`3 / 8` in decimal? (When the question uses the float type,
    the grader accepts also answers that slightly differ from the model solution.)

    0.378
    !0.378 § Hint: the answer is between 0 and 1. Use the decimal point and write three first decimals, for example, ``0.924``.

Testing the questionnaries
..........................

It is good practise to test your questionnaire, especially if there are
several correct answers. Note that A+ will show the correct answers for the
students who have submitted for the maximum number of times (but not for anyone
else).


.. admonition:: String, int, or float?
  :class: info

  Use the ``int`` answer type always when the answer is an integer. Of course
  the answer could be compared to the right answer as a string. However, the
  benefits of ``int`` over ``string`` are the following. First, extra space
  characters are always ignored. Second, A+ shows a histogram of the numerical
  answers to the teacher when they click on *View all submissions* on the
  exercise box in A+, and then *Summary*. See Figure "the summary a
  float-freetext questionnaire" below.

  ``float`` works the same way as ``int``. Currently it considers the answer
  to be correct if the difference between student's answer and the model
  solution is at most 0.02.

.. figure:: /images/questionnaire/summary-freetext-float.png
   :alt: Screenshot of A+: summary of a float-type freetext question

   **Figure:** *the summary of a float-freetext questionnaire*. In this case, 304
   students (83 %) have answered the question and most of them (300) have
   received 20 points. There is only one question whose correct answer is
   between 4.8 and 5.0, with 300 students giving that answer. Four students
   have an incorrect answer having value between 1.4 and 1.6.


.. figure:: /images/questionnaire/summary-freetext-string.png
  :alt: Screenshot of A+: summary of a string-type freetext question

  **Figure:** *the summary of a string-freetext questionnaire*. The answer
  is an SQL query, and A+ shows the unique answers. There are four identical
  answers of one type and three identical answers of another type.


.. questionnaire:: questionnaire_text_demo_2 10

  .. freetext:: 5 string-ignorews-ignorequotes
    :length: 10


    Here the correct answer is "anothertest". Surrounding quotes are
    ignored in the solution as well as whitespace everywhere. (modifiers
    ignorequotes and ignorews).

    anothertest
    !anothertest § Follow the instruction
    test § This was the answer to the first question.

  .. freetext:: 5 unsortedchars-ignorews
    :length: 7

    An ``unsortedchars`` example. What are the unique vovels in the word
    "cacophonic"? Correct answers are: aio, aoi, iao, ioa, oai, oia, and
    also the versions with two o's, because *unsortedchars* always compares
    unique characters.

    aio


Regular expressions are useful when there are multiple solutions, or when
one wants to have some tolerance in numeric questions, like accept real
numbers beginning with 0.014, 0.015, or 0.016.

.. questionnaire:: questionnaire_regexp 20
  :title: Fun with regular expressions
  :submissions: 10

  .. freetext:: 10 regexp
    :length: 7

    Type either "cat" or "dog".

    ^(cat|dog)$

  .. freetext:: 10 regexp
    :length: 7

    What is the value of :math:`\pi` with four most significant digits?
    This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
    ``3.141`` and zero or more digits after that.

    ^3\.141\d*$


Additional information
----------------------

See the source code of `the A+ RST tools questionnaire directive
<https://github.com/Aalto-LeTech/a-plus-rst-tools/blob/master/directives/questionnaire.py>`_
and the corresponding `form implementation in mooc-grader
<https://github.com/Aalto-LeTech/mooc-grader/blob/master/access/types/forms.py>`_.
