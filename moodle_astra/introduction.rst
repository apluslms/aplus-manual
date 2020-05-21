Moodle Astra plugin
===================

`Moodle <https://moodle.org/>`_ is a widely used open-source learning management system.
Aalto University hosts all course pages in a Moodle site called
`MyCourses <https://mycourses.aalto.fi/>`_.
`Astra <https://github.com/Aalto-LeTech/moodle-mod_astra/>`_ is a Moodle plugin
that replicates the basic functionality of the A+ frontend and therefore
provides an alternative frontend to A+ courses directly embedded in a Moodle site.
Astra takes the place of A+ and connects to the MOOC grader in order to retrieve
course contents and to grade submissions. Astra does not connect to
the A+ frontend server. Astra stores course data, such as exercise submissions
and their grading results, in the Moodle database.

Astra does not implement all of the features in A+, but typical courses following
the simple basic course structure work in Astra without further modifications.
For example, group submissions and exercise difficulty settings are not supported
in Astra.

Astra is a module or activity plugin in Moodle, which means that the modules or
exercise rounds of the A+ course become `activities <https://docs.moodle.org/36/en/Activities>`_
in Moodle (one activity per module). Astra is also accompanied by
a `Moodle block plugin <https://docs.moodle.org/36/en/Blocks>`_,
`Astra exercises setup <https://github.com/Aalto-LeTech/moodle-block_astra_setup>`_,
which provides links to administrative functionalities only for teachers.

Astra course setup in Moodle
----------------------------

A course from the MOOC grader can be easily imported into a Moodle coursespace.

**The Astra exercises setup block must be added once** to a Moodle coursespace.
The block stays in the coursespace after it has been added and one does not
need to add it again in the same coursespace. Add the block with these steps:

1. Go to the Moodle coursespace (course front page).
2. Turn editing on.
3. Click "add a block" in the left-side navigation and select "Astra exercises setup".
4. You may turn editing off now.

**Import the course** into the Moodle coursespace by following these steps:

1. Decide which Moodle course section shall host these exercises and pay attention
   to its section number (0-N visible in the URL of the section page).
   The course front page is section zero.
2. Click "edit exercises" in the Astra exercises setup block. The block is visible
   in the side of the course page (after you have added the block to the coursespace).
3. In the new page, click "update and create Astra exercises automatically".
4. In the form, enter "configuration URL" for your course and
   "Moodle course section number" according to your preferred course section.
   (API key is not used.) The configuration URL depends on the MOOC grader server
   and the course key used there. The URL follows the pattern
   ``https://DOMAIN/COURSEKEY/aplus-json``.
5. Click "apply" in the form. The exercises are now ready. You can see an overview
   in the edit course page (from which you accessed the import form) and
   the Moodle activities are displayed in the specified course section.

Whenever the course structure is modified, i.e., you modify exercise settings
such as deadlines and maximum points or add new exercises, the course should be
imported again to Moodle in order to update the settings there.
The import form remembers the previously entered values so that you only need to
click the apply button in the form.


Moodle course section and activity visibility
---------------------------------------------

In Moodle, it is possible to manually hide course sections or individual activities
so that students may not access them. In Astra, modules (which correspond to
activities) and learning objects may also be hidden by setting their status to
hidden (in the course repository). There are some reasons for hiding content,
for example:

- The teacher wants to test the materials before releasing them to the students.
- The materials are temporarily broken.

Note that the module opening time prevents students from accessing the materials
early even when the module is visible.

When a Moodle course section is hidden, Moodle also hides the activities that exist
in the section at that moment. Note that a hidden Moodle course section may
contain visible activities, which the students may access even though they can
not see the section. For example, the gradebook may contain links to any visible
activities.


Moodle gradebook
----------------

`Gradebook <https://docs.moodle.org/36/en/Grader_report>`_ (also known as
the grader report) is a feature in Moodle that gathers a student's grades of
the course assignments in one place.
Astra stores the best points that a student has earned in each Astra exercise
in the gradebook. In addition, the gradebook shows each exercise round with
the total points the student has earned in the exercises of the round.

The teacher may export grades from the gradebook in different formats, such as
Excel spreadsheet. This is a standard Moodle feature unrelated to Astra.


Export results in JSON
----------------------

The teacher may export Astra exercise results in JSON format by going to the
"export course data" section in the Astra exercises setup block.
The "export results" section there allows the teacher to download a JSON file
that contains data about students submissions, in particular the points and
submission times. There are filters for including only specific exercises,
students, all submissions of a student or only the best submission.
You may download :download:`an example Python script <scripts/results_before_exam.py>`
for processing the data in the JSON file. The script may be modified
according to your own needs.

.. warning::

  Note that the JSON file exported from Astra uses a different structure than
  the JSON course data available in the REST API of the A+ frontend.
  Keep this in mind if you run courses in both A+ and Astra.

The export course data section also enables the teacher to download a ZIP archive
of the files students have submitted to exercises. Likewise, the teacher may
download the other inputs such as text fields and checkboxes entered by students
into exercise forms.

