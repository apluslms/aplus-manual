Gallery of features
===================

This section is a visual index of exercises and services that have been used
with A+.

Front page
----------

.. _front-page-image:

.. figure:: /images/gallery/aplus-front-page.png
   :alt: Front page of A+

The above image shows an example of the front page of `A+ at Aalto University
<https://plus.cs.aalto.fi/>`_. The front page has two sections. The upper section shows
course instances which the logged-in user is currently; enrolled in, teaching
or assisting. The lower section shows all ongoing and recently ended courses.

Each course has optional image, name, instance name, course code and teaching schedule.
All courses have a green "Aalto" tag to indicate that the course is for Aalto University students.
The "Data Structures and Algorithms" -course has also a blue "MOOC" tag to indicate
that the course is also a massive open online course.
Sections :doc:`7.1 Setting up a course on production servers </admin/setup>`
and :doc:`7.2 Course settings </admin/settings>` describe these in detail.

Exercises
---------

Point and click
...............

.. figure:: /images/gallery/jsvee-factorial.png

   A **JSVEE exercise** is a slideshow of program execution. This particular
   example is from the *Data Structures and Algorithms Y* course, which shows
   how a factorial function in Python is executed.

.. figure:: /images/gallery/jsav-minheap-insert.png

   A **JSAV exercise** is an visual algorithm simulation exercise. The student
   manipulates a data structure with given input data according to instructions
   by pointing and clicking with the mouse. This particular example is about
   inserting elements to a minimum heap.

   After the student has worked with the exercise, they can submit it and
   receive points automatically. They also can review a model example or reset
   the exercise with new initial data. These exercises are used on the
   *Data Structures and Algorithms* courses (both *Y* and *SCI* versions for
   students of Computer Science minor / major).


Databases
.........

.. figure:: /images/gallery/relational-algebra.png

   A **relational algebra exercise** on the *Databases* course. The student
   constructs a database query in relational algebra, which is then
   automatically graded.

Python
......

.. figure:: /images/gallery/python-fractal-graded.png

   A **Programming exercise with graphical output**. This is a hard exercise
   from the course *Data Structures and Algorithms Y*, where the student
   writes a Python program that draws a bitmap fractal similar to
   `Sierpinski carpet <https://en.wikipedia.org/wiki/Sierpinski_carpet>`_.
   The picture shows the feedback for the student from the automatic grader.
   There are Python unit tests which give points, and also visual comparison
   of the outputs of the student's program and the correct solution.

:doc:`Section 2 </programming_exercises/instructions>`
describes how to create Python programming exercises.


Services
--------

Lab Queue
.........

.. figure:: /images/gallery/lab_queue.png

   **Lab Queue** (Neuvontajono) is a service used during computer exercise
   sessions, which students use to request help from a teaching assistant
   at the session.


Essay grading
.............

.. figure:: /images/gallery/rubyric.png

   `Rubyric is a tool for manual grading using rubrics <../rubyric/introduction>`_.
   The teacher creates a *rubric*,
   a grading template with scores and feedback text snippets. Then the students
   submits their essays and the teacher can grade them efficiently and
   consistently, possibly with additional remarks. Rubyric also supports
   group submissions and peer grading.


Plagiarism detection
....................

.. figure:: /images/gallery/radar.png

   :doc:`Radar is a submission similarity matcher </programming_exercises/radar>`
   that helps detect plagiarism in programming exercises. The figure shows a
   comparison view for two submissions for the same programming exercise.
