Designing programming exercises
===============================

.. styled-topic::

  Main questions:
      How to design a programming exercise that teaches a particular
      subject? What I need to know besides the A+ related technicalities?

  Topics:
      Practical tips on how to design new programming exercises:
      pedagogical and software development aspects.
      Exercise instructions, code template, model solution, grading,
      testing

  What you are supposed to do?
      Read the documentation.

This chapter is meant for course assistants and lecturers who develop programming
exercises. It is generic knowledge on creating exercises besides on the A+ related
technicalities.

.. admonition:: Best practice, not an authoritative guide
  :class: warning

  The knowledge here is a compilation of best practises that have been used on
  years 2017-2021 on courses *Data Structures and Algorithms Y* and *Computing
  Applications*. It is not solid pedagogical or software engineering
  knowledge. Programming exercise design also depends on pedagogical techniques,
  teacher preference, and the subject to be taught. Therefore, feel free to
  apply the ideas below at your own consideration.

Developing a solution to a programming problem is creative work. Creating a
high-quality programming exercise is challenging for the same reason, and many
other reasons. Here is a short step by step guide, a sort of design and
development process, for programming exercises.

New programming exercises are needed yearly for two reasons. First, there are
new courses that need to teach new technologies. Second, it is known that if
the same programming exercise exists on the same course consecutively many
years, it is a tempting subject for plagiarism.

The practical guide for a programming exercise
----------------------------------------------

Design
......

1. Plan the learning objectives.
2. Plan the context: what data, problem, and background story is there?
3. Plan the cognitive tasks: what the student is supposed to do (or figure out)?
4. Write instructions for the exercise.

Develop
.......

5. Write a model solution.
6. Write a code template based on the model solution.
7. Write *student's unit tests* to guide the student in the development work.
8. Write *grader unit tests*: preferably one test per cognitive task. Use
   pseudorandom test data to prevent gaming.

Test
....

9. Check that exercise instructions correspond to the code template.
10. Test the model solution against student's and grader unit tests.
11. Write incorrect solutions: one solution designed to fail one particular unit test.
12. Test with incorrect solutions.
13. Let someone else do the exercise as if they were a student on your course.

14. Repeat some steps (iterate) when needed.

Preventing gaming and plagiarism
--------------------------------

With automatic assessment and feedback, some students try to
`game the system <https://doi.org/10.1145/985692.985741>`_ : they try to get
easy exercise points without learning.

One gaming behaviour is to guess the input-output pairs of grader unit tests.
This is easy, if the test input of each grader unit test is constant, and
moreover, if the test input and output are shown exactly. The one can write a
program that gives a hardcoded, correct answer to an expected question without
actually solving the problem.

Another gaming behaviour relies on verbose instructions that the intelligent
tutoring system gives. If the automatic feedback is too helpful, the student
can do gradual implementations based on the exact hints they are given, and
receive reasonable amount of correctness with their solution without actually
learning much.

To prevent this kind of gaming, one can use pseudorandom unit test data with
varying size and contents. Depending on the exercise, just generating some
pseudorandom data with the standard library of the required programming language
is enough. In case you need something fancy, there are libraries for test data
generation, such as `Hypothesis <https://hypothesis.readthedocs.io/en/latest/>`_
for Python. However, beware that the APIs for the libraries may change, which
then complicates the maintenance of the automatic grader for your programming
exercise.

Ideas for assignments in research literature
--------------------------------------------

`Nifty assignments <http://nifty.stanford.edu/>`_: a collection of
well-designed programming assigments presented yearly at
`SIGCSE conference <https://dl.acm.org/conference/sigcse>`_.

