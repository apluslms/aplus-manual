Creating questionnaire exercises
================================

One can easily create simple questionnaire exercises for an A+ course, such as
one-line text answers and multiple choice exercises. This page shows many
examples on these.

General settings for a questionnaire
------------------------------------

**Arguments for the questionnaire directive: exercise key, maximum points and difficulty**

The questionnaire directive arguments define the exercise key and optional max points
with the difficulty. For example, ``.. questionnaire:: nro1 A50`` sets key of the
questionnaire to ``nro1``, max points to ``50`` and difficulty to ``A``.

**Maximum points**: Set as an argument of the questionnaire directive. If not explicitly
set, the max points will be set to be the sum of the question points.

**Difficulty**: The difficulty parameter is set after the exercise key. It does not affect
any scorekeeping, but only works as an indicator for the student. (The A+ REST API can group
earned points by the difficulty so that the teacher may use the difficulties for computing
final course grades.) Setting the difficulty is optional and it can be set even if the
max points aren't defined in the argument.

**Other options for the questionnaire**

The questionnaire directive accepts the following options. These are placed below the directive,
with the format ``:option: possible value``:

- ``submissions``: max submissions
- ``points-to-pass``: points to pass
- ``feedback``: If set, assumes the defaults for a feedback questionnaire
- ``title``: exercise title
- ``no-override``: If set, the conf.py override setting is ignored
- ``pick_randomly``: integer. The questionnaire selects N questions randomly for the
  user instead of showing all questions. The random selection changes after the user submits,
  but persists without changes if the user just reloads the web page. (The questionnaire should
  not include any static text fields between the questions since the text fields are part of
  the pool from which the questions are randomly selected.)
- ``preserve-questions-between-attempts``: If set, the questions in a ``pick_randomly``
  questionnaire are preserved between submission attempts, instead of being resampled
  after each attempt.
- ``category``: exercise category. If you do not define a category the default value will be used. For questionnaires
  the default ``category`` is **questionnaire**.
- ``reveal-model-at-max-submissions``: The questionnaire feedback reveals the model
  solution after the user has consumed all submission attempts. Can be set true or false.
  The feedback may reveal the model solution even before the exercise deadline.
  Note that A+ has a separate feature for showing exercise model solutions after the deadline.
  The default value can be set in index.rst with the field
  questionnaire-default-reveal-model-at-max-submissions. By default false.
- ``show-model``: Students may open the model solution in A+ after the module deadline.
  Can be set to true or false. The default value can be set in index.rst with the field
  questionnaire-default-show-model. By default true.
- ``allow-assistant-viewing``: Allows assistants to view the submissions of the students.
  Can be set to true or false. Overrides any options set in the conf.py or config.yaml files.
- ``allow-assistant-grading``: Allows assistants to grade the submissions of the students.
  Can be set to true or false. Overrides any options set in the conf.py or config.yaml files.

**Instructions:** Questionnaire instructions or description can be set below the question title as part of the directive
content.

Individual questions
--------------------

**Question type:** The question directives ``pick-one``, ``pick-any``, and ``freetext``
start a new question. So for instance ``.. pick-one:: 10`` begins a single-choice question
with the maximum points of 10.

**Question:** The questionnaire question can be set below the question type. The question must be indented relative to
the question type.

**Other options for individual questions**

The question directive accepts also the following options:

- ``class``: CSS class
- ``required``: If set, the question is required and empty answers of the questionnaire
  are rejected and no submission is consumed.
- ``key``: a manually set key for the question. This affects the HTML input element and the
  key in the submission data. If no key is set, note that automatically added keys change
  when the order and amount of questions is modified.

**Hints:** Hints are added right after the selectable answers, and these must be linked to the selectable answers.
Therefore, if we use latin letters to label the answers, we should use the same letters to label the hints. The
following snippet of code illustrates how can we use of the labels to link the answers to the given hints.

.. code-block:: rst

  .. pick-one:: 10

     Subdirective ``pick-one`` defines a single-choice question.
     When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    a § Not quite. Remember the cube root.
    !b § If this alternative is not selected, this hint will be shown.
    c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.

As we can see in the snippet above, the regular format for the hints is ``label used by the answer § feedback text or hint``.
Hints may also be prepended with ``!`` in order to show the feedback when the student did not select that specific answer.
In freetext questions, the label may be prepended with ``regexp``: in order to use regular expressions for matching
the student's submission. Hints are displayed after the student has clicked the submit button and are used to help
students while solving the questionnaire.

Single-choice and multiple-choice questions
-------------------------------------------

**Correct options**: The correct answers for ``pick-one`` (single-choice) and ``pick-any`` (multiple choice)
directives are marked by prefixing  the ``*`` symbol to the corresponding answer/option.

**Neutral options**: Multiple-choice questions may have neutral options, which are marked by prefixing the ``?`` symbol
to the corresponding answer/option. Neutral options do not affect grading, regardless of whether the student selected
them or not.

**Initially selected options** Initially selected options may be set with by prefixing the ``+`` symbol to the
corresponding  answer/option.
The initially selected options are pre-selected when the exercise is loaded.
The ``+`` character must always precede the ``*`` or ``?`` symbols whenever they are combined, i.e. ``+* OPTION`` or
``+? OPTION``.

The ``pick-any`` directive has following options in addition to the common question options:

- ``partial-points``: When set, the question awards points for partially correct submissions.
  The points scale linearly to the maximum points when more than half of the options
  are answered correctly.
- ``randomized``: When this option is used, a subset of the answer options (checkboxes)
  is randomly selected for the user. The random selection changes after the
  user submits, but persists when the user just reloads the web page. The value of the
  option is an integer, which is the number of choices to randomly select from all of
  the defined answer choices in the question. The option correct-count should be also
  set when this option is used.
- ``correct-count``: The number of correct answer options (checkboxes) to randomly select in the
  randomized pick-any question. This option is used with the randomized option.
- ``preserve-questions-between-attempts``: If set, the answer choices in a randomized
  question are preserved between submission attempts (instead of being resampled after each attempt).

Example: Single and multiple choices questionnaire
..................................................

.. rst-tabs::

  .. tab-content:: tab-html-render-single-multiple-choice
    :title: HTML visualisation

    .. questionnaire:: questionnaire_demo A40
      :title: Single-choice and multiple-choice questions
      :points-to-pass: 30
      :submissions: 3

      The difficulty of this questionnaire is set as A. Maximum points are 40,
      but only 30 are required to pass.

      .. pick-one:: 10

        Subdirective ``pick-one`` defines a single-choice question.
        When :math:`(x + 1)^3 = 27`, what is :math:`x`?

        a. 9
        *b. 2
        c. 3

        a § Not quite. Remember the cube root.
        c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.

      .. pick-one:: 10
        :dropdown:

        If the option ``dropdown`` is used for a single-choice question,
        the question can be transformed into a dropdown-type, such as this.

        What is the type of this entire exercise?

        a. programming exercise
        *b. questionnaire
        c. general feedback of the course

      .. pick-any:: 10

        Subdirective ``pick-any`` defines a multiple-choice question.

        When :math:`(x + 1)^2 = 16`, what is :math:`x`?

        a. 4
        *b. an integer
        *c. 3
        d. an irrational number
        e. -3
        *f. -5
        ?g. neutral option

        a § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.
        !b § If option "an integer" is not chosen, this hint will be shown.
        d § No. This equation has a nice and easy solution.

      .. pick-any:: 10
        :partial-points:

        Checkbox questions defined with ``pick-any`` can have the option ``partial-points``.
        Students are then granted points also for partially correct answers. You can try it out
        below.

        For instance, in this case there are three correct answers, the grading goes as follows:
        1 correct = 3 points,
        2 correct = 6 points,
        3 correct = 10 points.

        And for the wrong answers:
        1 wrong option chosen = 3 points deducted,
        2 wrong options chosen = 6 points deducted,
        3 wrong options chosen = 10 points deducted.

        When :math:`(x + 1)^2 = 16`, what is :math:`x`?

        a. 4
        *b. an integer
        *c. 3
        d. an irrational number
        e. -3
        *f. -5

  .. tab-content:: tab-code-single-multiple-choice
    :title: RST Code

    .. code-block:: rst

      .. questionnaire:: questionnaire_demo A40
        :title: Single-choice and multiple-choice questions
        :points-to-pass: 30
        :submissions: 3

        The difficulty of this questionnaire is set as A. Maximum points are 40,
        but only 30 are required to pass.

        .. pick-one:: 10

          Subdirective ``pick-one`` defines a single-choice question.
          When :math:`(x + 1)^3 = 27`, what is :math:`x`?

          a. 9
          *b. 2
          c. 3

          a § Not quite. Remember the cube root.
          c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.

        .. pick-one:: 10
          :dropdown:

          If the option ``dropdown`` is used for a single-choice question,
          the question can be transformed into a dropdown-type, such as this.

          What is the type of this entire exercise?

          a. programming exercise
          *b. questionnaire
          c. general feedback of the course

        .. pick-any:: 10

          Subdirective ``pick-any`` defines a multiple-choice question.

          When :math:`(x + 1)^2 = 16`, what is :math:`x`?

          a. 4
          *b. an integer
          *c. 3
          d. an irrational number
          e. -3
          *f. -5
          ?g. neutral option

          a § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.
          !b § If option "an integer" is not chosen, this hint will be shown.
          d § No. This equation has a nice and easy solution.

        .. pick-any:: 10
          :partial-points:

          Checkbox questions defined with ``pick-any`` can have the option ``partial-points``.
          Students are then granted points also for partially correct answers. You can try it out
          below.

          For instance, in this case there are three correct answers, the grading goes as follows:
          1 correct = 3 points,
          2 correct = 6 points,
          3 correct = 10 points.

          And for the wrong answers:
          1 wrong option chosen = 3 points deducted,
          2 wrong options chosen = 6 points deducted,
          3 wrong options chosen = 10 points deducted.

          When :math:`(x + 1)^2 = 16`, what is :math:`x`?

          a. 4
          *b. an integer
          *c. 3
          d. an irrational number
          e. -3
          *f. -5

Freetext questions
------------------

The ``freetext`` directive is represented by HTML input fields or text areas in the browser.  The students can use
the input files to submit their responses which is graded by the mooc-grader.

The freetext directive also accepts the following options in addition to
the common question options:

- ``length``: (horizontal) length for the HTML text input. If the height is not defined, the length is translated to
  the `size attribute of the input field <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefsize>`_, but if the height is defined the length represents the number of columns of
  the `textarea input field <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea>`_.
- ``height``: If greater than 1, the textarea HTML element is used. Otherwise,
  a text input is used.

**Instructions and correct answer:** The body of the freetext question is
expected to be its model solution. However, the question instructions can be
written inside the body before the model answer. The instructions and the
model solution must be separated with an empty line.

Note that if the questionnaire has the ``feedback`` option set, freetext questions
may not have a model solution and the body of the question is shown as the
question instructions.

**Comparison method**: The freetext directive accepts a second positional
argument after the points. It defines the compare method for the model solution.
For instance ``freetext:: 5 int``.

The different comparison methods are ``int``, ``float``, ``string``,
``subdiff``, ``regexp`` or ``unsortedchars`` (unsorted character set). The ``regexp``
compare method takes the correct answer as a regular expression and tries to
match the submission with it. ``subdiff``: works almost like the string method,
but it can have multiple correct answers separated with ``|`` and if the answer is
incorrect, it shows the difference of the answer to each correct answer as a hint.
For example, when the correct answer is *'cat'* and the student answers *'car'*,
the student receives feedback: *"Correct parts in your answer: ca-."*

String methods have comparison modifiers that are separated with a hyphen.
For example, ``.. freetext:: 30 string-ignorews-ignorequotes``.

The following modifiers are available:

- ``ignorews:`` ignore white space (applies to regexp too)
- ``ignorequotes``: iqnore "quotes" around
- ``requirecase``: require identical lower and upper cases (only with the
  string and subdiff types)
- ``ignorerepl``: ignore REPL prefixes
- ``ignoreparenthesis``: ignore parenthesis "( )"

.. admonition:: String, int, or float?
  :class: info

  Use the ``int`` answer type always when the answer is an integer. Of course
  the answer could be compared to the right answer as a string. However, the
  benefits of ``int`` over ``string`` are the following. First, extra space
  characters are always ignored. Second, A+ shows a histogram of the numerical
  answers to the teacher when they click on *View all submissions* on the
  exercise box in A+, and then *Summary*.

  ``float`` works the same way as ``int``. Currently, it considers the answer
  to be correct if the difference between the student's answer and the model
  solution is at most 2% (relative to the larger absolute value).

Example: Free-text questionnaire
................................

.. rst-tabs::

  .. tab-content:: tab-html-render
    :title: HTML visualisation

    .. questionnaire:: questionnaire_text_demo 25
      :title: Questionnaire full of freetext questions
      :submissions: 3
      :reveal-model-at-max-submissions: true

      This is the description for the whole questionnaire. It can be added below the title
      and the options set for the exercise. In this questionnaire the ``reveal-model-at-max-submissions`` is set
      is set to true, so when the student reaches maximum amount of submissions (e.g. in here has
      submitted 3 times), the correct answers are indicated below each question.

      .. freetext:: 5
        :length: 5

        This is the most basic free text questionnaire. The correct answer is
        ``test``. You can write at most 10 characters into the box. When defining the question
        remember to add an empty line between the instructions and correct answers.

        test
        !test § Hint: follow the instructions.

      .. freetext:: 5
        :height: 2

        This is the basic free text questionnaire, with the height set at 2, so the input is
        transformed into a textbox. The correct answer is ``textbox``.

        textbox

      .. freetext:: 5
        :length: 10
        :required:

        If the question has ``required`` set like here, the questionnaire submission is not
        accepted without it. The correct answer here is ``required``.

        required

      .. freetext:: 5 int
        :length: 7

        The answer can be a number, an integer. What is :math:`3 + 8`?

        11
        !11 § Hint to be shown when the student's answer is not 11.

      .. freetext:: 5 float
        :length: 7

        The answer can also be a decimal number (floating point number).
        What is :math:`3 / 8` in decimal? (When the question uses the float type,
        the grader accepts also answers that slightly differ from the model solution.)

        0.378
        !0.378 § Hint: the answer is between 0 and 1. Use the decimal point and write three first decimals, for example, ``0.375``.

  .. tab-content:: tab-code-
    :title: RST Code

    .. code-block:: rst

      .. questionnaire:: questionnaire_text_demo 25
        :title: Questionnaire full of freetext questions
        :submissions: 3
        :reveal-model-at-max-submissions: true

        This is the description for the whole questionnaire. It can be added below the title
        and the options set for the exercise. In this questionnaire the ``reveal-model-at-max-submissions`` is set
        is set to true, so when the student reaches maximum amount of submissions (e.g. in here has
        submitted 3 times), the correct answers are indicated below each question.

        .. freetext:: 5
          :length: 5

          This is the most basic free text questionnaire. The correct answer is
          ``test``. You can write at most 10 characters into the box. When defining the question
          remember to add an empty line between the instructions and correct answers.

          test
          !test § Hint: follow the instructions.

        .. freetext:: 5
          :height: 2

          This is the basic free text questionnaire, with the height set at 2, so the input is
          transformed into a textbox. The correct answer is ``textbox``.

          textbox

        .. freetext:: 5
          :length: 10
          :required:

          If the question has ``required`` set like here, the questionnaire submission is not
          accepted without it. The correct answer here is ``required``.

          required

        .. freetext:: 5 int
          :length: 7

          The answer can be a number, an integer. What is :math:`3 + 8`?

          11
          !11 § Hint to be shown when the student's answer is not 11.

        .. freetext:: 5 float
          :length: 7

          The answer can also be a decimal number (floating point number).
          What is :math:`3 / 8` in decimal? (When the question uses the float type,
          the grader accepts also answers that slightly differ from the model solution.)

          0.378
          !0.378 § Hint: the answer is between 0 and 1. Use the decimal point and write three first decimals, for example, ``0.375``.

.. rst-tabs::

  .. tab-content:: tab-html-render-freetext
    :title: HTML visualisation

    .. questionnaire:: questionnaire_text_demo_2 10

      .. freetext:: 5 string-ignorews-ignorequotes
        :length: 10

        Here the correct answer is ``anothertest``. Surrounding quotes are ignored in the
        solution as well as whitespace everywhere. (modifiers ignorequotes and ignorews).

        anothertest
        !anothertest § Check the correct answer given in the description

      .. freetext:: 5 unsortedchars-ignorews
        :length: 7

        An ``unsortedchars`` example. What are the unique vovels in the word
        "cacophonic"? Correct answers are: aio, aoi, iao, ioa, oai, oia, and
        also the versions with two o's, because *unsortedchars* always compares
        unique characters.

        aio

  .. tab-content:: tab-code-freetext
    :title: RST Code

    .. code-block:: rst

      .. questionnaire:: questionnaire_text_demo_2 10

        .. freetext:: 5 string-ignorews-ignorequotes
          :length: 10

          Here the correct answer is ``anothertest``. Surrounding quotes are ignored in the
          solution as well as whitespace everywhere. (modifiers ignorequotes and ignorews).

          anothertest
          !anothertest § Check the correct answer given in the description

        .. freetext:: 5 unsortedchars-ignorews
          :length: 7

          An ``unsortedchars`` example. What are the unique vovels in the word
          "cacophonic"? Correct answers are: aio, aoi, iao, ioa, oai, oia, and
          also the versions with two o's, because *unsortedchars* always compares
          unique characters.

          aio

Example: Regex questionnaire
............................

.. rst-tabs::

  .. tab-content:: tab-html-render-regexp
    :title: HTML visualisation

    .. questionnaire:: questionnaire_regexp 20
      :title: Questionnaire using regular expressions
      :submissions: 5

      Regular expressions can provide several alternative correct answers
      for a single question such as in the first example. Both cat and dog
      give full points. You can also give an example of correct answers
      by following the regexp with " °=° " and some of the alternatives
      (which is visible in the model answer instead of the whole regexp).

      Regular expressions are also useful when there are multiple solutions, or when
      one wants to have some tolerance in numeric questions, like accept real
      numbers beginning with 0.014, 0.015, or 0.016.

      .. freetext:: 10 regexp
        :length: 7

        Type either "cat" or "dog".

        ^(cat|dog)$ °=° cat

      .. freetext:: 10 regexp
        :length: 7

        What is the value of :math:`\pi` with four most significant digits?
        This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
        ``3.141`` and zero or more digits after that.

        ^3\.141\d*$

  .. tab-content:: tab-code-regexp
    :title: RST Code

    .. code-block:: rst

      .. questionnaire:: questionnaire_regexp 20
        :title: Questionnaire using regular expressions
        :submissions: 5

        Regular expressions can provide several alternative correct answers
        for a single question such as in the first example. Both cat and dog
        give full points. You can also give an example of correct answers
        by following the regexp with " °=° " and some of the alternatives
        (which is visible in the model answer instead of the whole regexp).

        Regular expressions are useful when there are multiple solutions, or when
        one wants to have some tolerance in numeric questions, like accept real
        numbers beginning with 0.014, 0.015, or 0.016.

        .. freetext:: 10 regexp
          :length: 7

          Type either "cat" or "dog".

          ^(cat|dog)$ °=° cat

        .. freetext:: 10 regexp
          :length: 7

          What is the value of :math:`\pi` with four most significant digits?
          This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
          ``3.141`` and zero or more digits after that.

          ^3\.141\d*$

Additional information
----------------------

* The most recent and complete documentation on this can
  be found at `the source code of the A+ RST tools package
  <https://github.com/apluslms/a-plus-rst-tools>`_.
* See the source code of `the A+ RST tools questionnaire directive
  <https://github.com/apluslms/a-plus-rst-tools/blob/master/directives/questionnaire.py>`_
* Review the corresponding `form implementation in mooc-grader
  <https://github.com/apluslms/mooc-grader/blob/master/access/types/forms.py>`_.
