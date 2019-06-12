Personalized exercises
======================

General description
-------------------

Personalized exercises contain some parts that are not the same for every
student. This is useful for preventing plagiarism: the students cannot simply
copy their answers or solutions from their peers.

Usually, the structure of the exercise is the same for everyone, but, for
example, some input data is different in each instance of the exercise. The
instances are usually randomly generated. Each student is assigned one instance
and multiple students may be assigned the same instance. The instance assigned
to the student remains the same even after refreshing the exercise page.

A personalized exercise defines a generator program that generates N instances
to the exercise. The instances are generated before the start of the course.
The mooc-grader CLI command ``python manage.py pregenerate_exercises``
runs the generator programs and saves the instance files in the correct
directory under the mooc-grader. In theory, the instance files could also
be created by some other way in the correct location.
The CLI command has some arguments to modify its behaviour: they are printed
with the ``--help`` argument. The ``run-mooc-grader`` container (used in local
testing and development) should automatically call the generators
if there are any personalized exercises in the course.

An instance contains some files that the grader program can
use while grading (the implementation of the exercise may decide freely how
those instance files are used). The instance files may also be used to add content
to the exercise description shown to the student. A student is connected to
one instance (the choice feels random but is based on their user IDs).
It is also possible to force the instance to change for the student, e.g., after
every five submissions ("you get five attempts before you must start over").
That kind of regeneration of the instance is disabled by default.


Example exercises
-----------------

Here we have two very simple example personalized exercises.
Their graders work in containers and the exercises define generator
programs that create random instances.

.. submit:: personalized_number 10
  :config: exercises/personalized_number/config.yaml

.. submit:: personalized_python 10
  :config: exercises/personalized_python/config.yaml



Detailed description of the "Personalized number" exercise
----------------------------------------------------------

Exercise instance generation
............................

When you run the A+ manual with the usual ``docker-up.sh`` script, and there
is no temporary data in the ``_data`` directory, mooc-grader will create the
instances for all personalized exercises. Mooc-grader will call the generator
script for each exercise and each instance separately. (Reference: mooc-grader
source: `access/management/commands/pregenerate_exercises.py <https://github.com/Aalto-LeTech/mooc-grader/blob/master/access/management/commands/pregenerate_exercises.py>`_
, `util/personalized.py <https://github.com/Aalto-LeTech/mooc-grader/blob/master/util/personalized.py>`_ .)

The directory for the personalized exercises inside the
**apluslms/run-mooc-grader** container is
``/local/grader/ex-meta/default/pregenerated``, where ``default`` is the name
of the course. Each personalized exercise has its own subdirectory named by
``module_page_key``, where ``module`` is the subdirectory for the RST file
(here "m02_programming_exercises"), ``page`` is the RST file which refers to
the exercise (here "04_personalized_exercises"); and ``key`` is the unique
identifier for the exercise (here "personalized_number" or
"personalized_python"). The pregenerated instances for
each exercise are inside these directories. For example, the directory
`/local/grader/ex-meta/default/pregenerated/m02_programming_exercises_04_personalized_exercises_personalized_number/`
has subdirectories ``0``, ``1``, ..., ``9``, one for each ten instances, and
each of those *instance directories* contains a text file named ``number``,
which has the personalized data for the instance.


When creating instances for the "Personalized number" exercise, mooc-grader
will call the **generator.py** script of the exercise first with command line
argument which tells the directory to store the first instance:

::

  python3 generator.py /local/grader/ex-meta/default/pregenerated/m02_programming_exercises_04_personalized_exercises_personalized_number/0

The script **generator.py** starts and stores the path string ``/local/grader/ ... /0``
to its variable ``instance_dir``. It creates a directory with that path, if it
does not exist. Then it generates a pseudorandom integer between 1 and 50,
writes it to a text file named ``number` inside the directory at ``instance_dir``
and terminates.

Next mooc-grader will call generator.py again, but this time with command line
argument ``/local/grader/ex-meta/default/pregenerated/m02_programming_exercises_04_personalized_exercises_personalized_number/1``.
This procedure is repeated for all the ten exercise instances.

Finally, the directory structure for the "Personalized number" exercise
inside the *mooc-grader container* looks like this:

::

  /local/grader/ex-meta/default/pregenerated/
  └── m02_programming_exercises_04_personalized_exercises_personalized_number
      ├── 0
      |   └── number
      ├── 1
      |   └── number
      ├── 2
      |   └── number
      ├── 3
      |   └── number
      ├── 4
      |   └── number
      ├── 5
      |   └── number
      ├── 6
      |   └── number
      ├── 7
      |   └── number
      ├── 8
      |   └── number
      └── 9
          └── number


Grading the exercise
....................

The directory structure inside the **apluslms/grade-python** container looks
essentially like this in the beginning:

::

  /
  ├── exercise
  |   ├── check_number.py
  |   ├── config.yaml
  |   ├── generator.py
  |   ├── run.sh
  |   └── template.html
  ├── submission
  |   └── user
  |       └── solution
  └── personalized_exercise
      └── number

As you can see, the directory structure is very similar to the
`nonpersonalized Python programming exercise <02_hello_world>`_.
The student's answer is at ``/submission/user/solution``. The directory
``/submission/user`` is also the starting directory for the **run.sh** script
for the exercise. Also, inside that container, the personalized data for the
exercise instance assigned to the student is initially at
``/personalized_exercise``. The contents of this directory is identical to the
directory
``/local/grader/ex-meta/default/pregenerated/m02_programming_exercises_04_personalized_exercises_personalized_number/X``
in the *mooc-grader container*, where ``X`` is the number of the instance.

Next, inside the grade-python container, the script **run.sh** copies the file
``/personalized_exercise/number`` to ``/submission/user``. Then run.sh starts
the actual Python-based grading script **check_number.py** inside commands
``capture`` and ``pre``. ``capture`` will store the text output from check_number
and finally send it to mooc-grader and A+. ``pre`` wraps the text output inside
HTML ``<pre>`` tags.

The grading script **check_number.py** starts with current working directory as
``/submission/user``. It reads both the files ``number``and ``solutions``, and
compares their contents. Next check_number prints feedback to the standard
output:

::

  Original number was: X
  Your solution was: Y

This is the feedback text that is shown to the student in A+ after the grading
is completed. Here ``X`` and ``Y`` are the actual contents of files ``number``
and ``solution`` parsed as integer values.

Finally, check_number prints two lines:

::

  TotalPoints: A
  MaxPoints: B

These lines are not shown as feedback for the student, but they are the
exercise score which is stored by A+ for this student and this submission.
``A`` is a nonnegative integer: the score that the grading script gave for
the solution. ``B`` is a positive integer: the maximum score that the
grading script can give for the exercise. Note that ``B`` can be different that
what is set in the ``max_points`` part of the **config.yaml** file of the
exercise; A+ will rescale the points if necessary.
