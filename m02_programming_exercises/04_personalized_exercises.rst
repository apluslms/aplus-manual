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

Configuration
.............

The ``config.yaml`` file in the ``personalized_number`` directory contains the
configuration of the exercise for A+ and mooc-grader, as usual. In addition to
basic programming exercises, it has the following section, which defines the
personalization.

::

  personalized: True
  generated_files:
    - file: number
      key: number
      content_in_template: True
      url_in_template: True
      allow_download: True
  generator:
    cmd: [ "python3", "generator.py" ]
    cwd: exercises/personalized_number/
  max_submissions_before_regeneration: 3

The obvious ``personalized`` keyword tells A+ and mooc-grader that personalized
exercise instances must be pregenerated and each user is then assigned an
instance of the exercise.

The ``generated_files`` section define a list of generated files for a
personalized exercise. Each list item defines the following settings:

- ``file``: filename of the generated file
- ``key``: key for accessing the file in HTML templates
- ``url_in_template``: if true, the exercise instructions shown to the student includes a HTML link to download the generated file
- ``content_in_template``: if true, template variable includes the content of the generated file
- ``allow_download``: if true, the student can download the generated file

The ``generator`` section has settings for the generator program that
creates one new instance of the exercise. At least ``cmd`` must be set. The
generator command ``cmd`` will be run from course_key dir (that is, course_key
is the cwd).

``cmd`` is the command that is used to run the generator in the shell. Note
that it is given as a `Python list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
where each word is its own item. Example: ``["generator_script.sh"]`` will run
generator_script.sh from course_key dir. Example:
``["python3", "script_dir/generator.py"]`` will run generator.py from
course_key/script_dir but keep course_key as cwd. Mooc-grader appends the
instance directory path to the argument list and the generator is expected to
write files into the directory. The file names should be listed under
``generated_files`` setting so that mooc-grader is aware of them.

For A+ administrators, the Django command used to pregenerate exercises is
``python manage.py pregenerate_exercises course_key <exercise_key>``.
(The ``--help`` option prints all possible arguments).

``cwd``: if set, this sets the current working directory for the generator
program. Since the default cwd is course_key, this applies to directories
in course_key. Example: ``cwd: "script_dir"`` will change the cwd to
``course_key/script_dir`` and only after that run cmd.

``max_submissions_before_regeneration`` defines how many times the student may
submit before the personalized exercise is regenerated (the exercise instance is
changed to another one). If unset, the exercise is never regenerated.


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

.. admonition:: The role of the exercise generator and supported software
  :class: info

  The generator program is meant for creating exercise instances from
  pseudorandom data or selecting subsets of some larger exercise dataset for
  each exercise instance. Because the generator is run inside the mooc-grader
  container, not a programming exercise grader container (such as
  apluslms/grade-python), there are limitations on what software can be used on
  the generator side.

  The apluslms/run-mooc-grader container has the following software:

  - minimal `Debian <https://www.debian.org>_` ("slim" version)
    - shells: bash, dash, sh
  - GCC, G++ `(GNU C and C++ compilers) <http://gcc.gnu.org/>`_
  - libc6-dev (GNU C Library: Development Libraries and Header Files)
  - make (GNU utility for compilation)
  - `gettext <https://www.gnu.org/software/gettext/>`_
  - `jq <https://stedolan.github.io/jq/>`_
  - `Python 3 <https://www.python.org>`_ and its standard library
  - `some Python tools <https://github.com/apluslms/service-base/blob/master/python3/Dockerfile>`_ as Debian packages

  You will likely want to write your exercise generator in Python. Using a
  shell such as bash is also possible. In theory, writing a generator in C or
  C++ should also be possible, but the generator program should be either
  precompiled, or then a shell script should compile the generator just once.

  For more information, see Dockerfiles of `apluslms/run-mooc-grader <https://github.com/apluslms/run-mooc-grader/blob/master/Dockerfile>`_
  and `apluslms/service-base <https://github.com/apluslms/service-base/blob/master/base/Dockerfile>`_
  containers.



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

Detailed description of the "Personalized Python" exercise
----------------------------------------------------------

This exercise is very similar to the "Personalized number" exercise. Instead of
randomly chosen integer, the file ``names`` in the exercise directory has
list of names, and one of the names is chosen randomly for each exercise
instance. Similarly, each instance has a directory, numbered from ``0`` to
``9``, and each of these directories has a text file named ``name``, which
contains a randomly chosen name. Therefore the exercise instance directory
inside the **mooc-grader container** has the following structure:

::

  /local/grader/ex-meta/default/pregenerated/
  └── m02_programming_exercises_04_personalized_exercises_personalized_python
      ├── 0
      |   └── name
      ├── 1
      |   └── name
      ├── 2
      |   └── name
      ├── 3
      |   └── name
      ├── 4
      |   └── name
      ├── 5
      |   └── name
      ├── 6
      |   └── name
      ├── 7
      |   └── name
      ├── 8
      |   └── name
      └── 9
          └── name

Note that **config.yaml** has very similar ``personalized`` section to the
"Personalized number" exercise, but here the student's input is a file, not a
text field, and therefore there is a ``files`` section instead of a ``fields``
section.

The grading script **check.py** imports the **solution.py** submitted by the
student. **run.sh** modifies the ``PYTHONPATH`` environment variable for easy
import. The output from the grading script is very similar to the one in the
"Personalized number" exercise.
