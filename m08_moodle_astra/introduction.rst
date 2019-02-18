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

