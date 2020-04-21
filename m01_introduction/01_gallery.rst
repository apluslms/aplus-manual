.. The roles  should be created at the beginning of the document. Global roles can be created in the `global.rst` file

.. include:: /global.rst

.. Chapter content

Gallery of features
===================

.. styled-topic::

  Main questions:
    What are the main features of A+?

  Topics:
    In this section we will talk about:

    * `Front page`_
    * `Exercises`_
    * `Services`_

  Material:
    In this chapter you won't need extra material.

  Requirements:
    There are no requirements for this chapter.

  Estimated working time:
    20min.



This section is a visual index of exercises and services that have been used
with A+.

.. _front-page:

Front page
----------

.. figure:: /images/gallery/aplus-front-page.png
  :width: 80%
  :align: center

  **A+ front page Spring-2020.** In the A+ front page you can find the list of the courses (ongoing courses) uploaded in the platform`.

The above image shows a screenshot of the front page of `A+ at Aalto University
<https://plus.cs.aalto.fi/>`_ from Spring 2020. The front page shows the most recent courses. Each course has an optional logo image, name, course
code and teaching time. All courses have a green "Aalto" tag to indicate that
the course is for Aalto University students. The Ohjelmointistudio 2 course
has also a blue "MOOC" tag to indicate the course is also a massive open online
course. Sections :doc:`9.1 Settings a course on production servers
</m09_admin/01_setup>`
and :doc:`9.2 Course settings </m09_admin/02_settings>` describe these in detail.

Exercises
---------

Point and click
...............

.. figure:: /images/gallery/jsvee-factorial.png
  :width: 80%
  :align: center

  A **JSVEE exercise** is a slideshow of program execution. 

This particular example is from the *Data Structures and Algorithms Y* course, which shows how a factorial function in Python is executed.

.. figure:: /images/gallery/jsav-minheap-insert.png
  :width: 80%
  :align: center

  A **JSAV exercise** is a visual algorithm simulation exercise.

The student manipulates a data structure with given input data according to instructions
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
  :width: 80%
  :align: center

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
   There are Python unit tests which give points, and also a visual comparison
   of the outputs of the student's program and the correct solution.

:doc:`Section 4 </m04_programming_exercises/01_instructions/>`
describes how to create Python programming exercises.


Services
--------
.. _lab-queue:

Lab Queue
.........

.. figure:: /images/gallery/lab_queue.png
  :width: 80%
  :align: center

  **Lab Queue** (Neuvontajono) is a service used during computer exercise
  sessions, which students use to request help from a teaching assistant
  at the session.


Essay grading
.............

.. figure:: /images/gallery/rubyric.png

  **Rubyric** is a tool for grading text assignments.

:doc:`Rubyric is a tool for grading essays </m08_rubyric/01_introduction>`.
The teacher creates a *rubric*,
a grading template with scores and feedback text snippets. Then the students
submits their essays and the teacher can grade them efficiently and
consistently, possibly with additional remarks. Rubyric also supports
group submissions and peer grading.


Plagiarism detection
....................

.. figure:: /images/gallery/radar.png
  :width: 80%
  :align: center

  **Radar** is a tool for comparing similarities between code submission.

:doc:`Radar is a submission similarity matcher </m04_programming_exercises/05_radar>`
that helps detect plagiarism in programming exercises. The figure shows a
comparison view for two submissions for the same programming exercise.

