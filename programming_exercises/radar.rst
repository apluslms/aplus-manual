Radar: Exercises with automatic similarity analysis
===================================================

It is possible to enable automatic program code similarity analysis for
programming exercises by adding the `Radar`_ web service for an A+ course
instance. When enabled, Radar will periodically fetch new submissions using the
A+ API, and perform syntax level similarity analysis for the submissions. The
results can be viewed using the Radar UI, accessible via the A+ menu.

.. admonition:: Configuration
    :class: default

    Radar is available as a Docker container for local testing.
    The container is included in the
    `docker-compose.yml <https://github.com/apluslms/aplus-manual/blob/master/docker-compose.yml>`_
    file in the git repo of this manual.

The following exercises are identical to the example exercises from chapter 2.2,
except that we have specified the programming language used in the exercise by
using the key ``radar_tokenizer`` in the ``submit`` rst directive. Radar will
track all submissions to exercises that have defined a valid language using the
``radar_tokenizer``. Additionally, we specified the optional
``radar_minimum_match_tokens`` to lower the match length threshold in order to
produce matches of the trivially short hello world exercises. This option
defaults to an arbitrary, empirically chosen value of 15, and can be adjusted if
the user feels that there are too many or too few matches.

You can try the service by e.g. logging in with two different accounts and
submitting the same solution using both accounts. Then, using a teacher account,
inspect the results in the Radar service.

.. submit:: python_radar 10
    :config: exercises/hello_python/config.yaml
    :radar_tokenizer: python
    :radar_minimum_match_tokens: 1

.. submit:: scala_radar 10
    :config: exercises/hello_scala/config.yaml
    :radar_tokenizer: scala
    :radar_minimum_match_tokens: 1

.. submit:: javascript_radar 10
  :config: exercises/hello_javascript/config.yaml
  :radar_tokenizer: js
  :radar_minimum_match_tokens: 1

.. submit:: primes_radar 10
    :config: exercises/primes/config.yaml
    :radar_tokenizer: python
    :radar_minimum_match_tokens: 1

.. _Radar: https://github.com/apluslms/radar

How to use Radar
----------------

1. Getting submissions to Radar
...............................

To bring submissions from A+ to Radar, select your course from the list. You 
will see a group of buttons.

.. image:: /images/radar_buttons.png

Go to "Configure" and click "Retrieve submittable exercises
and pick manually" from the bottom of the page. This will bring a list of exercises
on your course. Select the ones you want to bring to Radar by checking the "Include
into Radar" box, and then clicking "Overwrite and compare all" on the bottom. Here
you can also copy paste exercise specific templates given to students, as well as some
settings for radar to use (most important being the used tokenizer i.e. what
language the programming exercise is written in). These settings can be changed
later.

2. Different views to monitor plagiarism
........................................

Once exercises are in Radar, they will show as a list in your course in Radar.
Clicking on an exercise on the list will bring up comparisons sorted by
similarity for that exercise. Clicking these will bring up a side-by-side code
comparison between the students. These comparisons can be flagged as "plagiarized"
from the top right corner drop down menu:

.. image:: /images/radar_plagiate.png

Any side-by-side comparison will also have a button "Show all comparisons for
this pair of students", which will show all comparisons for the specific
two students on the course sorted by each exercise.

There are also two high level views for detecting plagiarism in Radar: Students
View, and Graph View. Students View will show all students in a list, along with
the average and maximum similarity scores of their submissions. This list
can be ordered by any column, and individual students can be searched by student ID.

The Graph View shows students and the number of matching submissions given the
parameters (max similarity and minimum number of matches). Note that on large
courses, the Graph View can potentially become very crowded, so filtering should
be started with very high similarity and number of matched submissions.

3. Making a similarity report
.............................

The Pair View can be accessed from any side-by-side code comparison of two students,
or alternatively, through the "Flagged pairs" button. In the Pair View, there is a
button "Get summary of marked plagiates". This will bring up a summary page, where
all flagged comparisons are listed in order. This can be printed as pdf using the
browser's print pdf method. Comments can be added to the overall report, as well
as each exercise. The comments are only visible in the report, and will disappear once
you leave the page.

4. Changing exercise settings and reuploading submissions or template code
..........................................................................

.. image:: /images/radar_exercise_columns.png
    :width: 1200

Exercise specific settings can be changed in the list of exercises by clicking
"Settings" on the right. The exercise settings include two key parameters:
Tokenizer type, and minimum match tokens. The tokenizer type must match the language
of the programming exercise. Minimum match tokens parameter refers to the number
of consecutive tokens that must be identical between two codes in order for Radar to
consider that part of the code as match/plagiarized. The default value is 15.
Lowering this number will generally produce more similarity, and is more fit for
shorter programming assignments.

If the minimum match tokens parameter is changed, all submissions can be recompared
using the "Recompare all" button. However, if you are unsure if Radar has all submissions
for whatever reason, the "Clear, reload and recompare all" button will fetch all
submissions again from A+.

Template code can be added here by simply copy pasting the code to the text area in the
"Exercise template" and saving. Template code is code included in the code template given
to students, and therefore excluding it can give more informative results, as it can
otherwise cause misleadingly high similarity scores in the student submissions.

Also note, that deleting anything in Radar does not delete anything from A+.
