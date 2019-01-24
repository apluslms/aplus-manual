Docker
=======================================================

.. styled-topic::

  Main questions:
      What is Docker? How are A+ and other software related to each other?

  Topics?
      Docker containers, A+ architecture.

  What you are supposed to do?
      Read the material. Try the Docker tutorial if you want to know more.

  Difficulty:
      You need UNIX terminal. We will not go deep into software technology,
      but show some things that are good to know for all course authors.

  Laboriousness:
      1-2 hours

.. admonition:: Software: Docker
  :class: meta

  `Docker <https://www.docker.com/>`_ is software which runs another software
  inside a *container*: an independent, executable package of software.
  When a software, like web server, Sphinx, or A+, runs inside a container,
  it thinks it has a computer of its own. The container has all the files
  that the software requires, like some particular directory structure and
  particular versions of some software libraries. When a container is built
  for a software, it will always run the similar way regardless of what kind
  of hardware and software is outside the container.

.. admonition:: Docker versus virtual machines
  :class: note

  A technical remark: Docker is not a typical *virtual machine* or *emulator*,
  which creates a whole imaginary computer inside another physical computer.
  Different Docker containers running on the same computer utilise the hardware
  operating system kernel (the software which controls the other software
  resources, like memory, disk and processor time efficiently. They share the
  same and shares those resources by their request).

The Docker home page also has `a short explanation of containers
<https://www.docker.com/what-container>`_.

The reasons for using Docker in A+ are the following:

- Easy installation, part 1
    Just install Docker and it will install all other software for you.

- Easy installation, part 2
    The containers work the same way both on your own  computer and the
    A+ production server which the students use.

- Easy server updates
    There are many containers running on the production server. One can
    update one container without affecting the others.

- Fault-tolerance
    There can be multiple similar containers running, for example,
    grading students' programming exercises. If one container would break,
    because it has a bug or the student's program has a bug, it can be
    terminated and other grading containers can still finish their job.

- Scalability
    It is easy to build a large service which uses many different
    types of containers and runs on many server computers together.

If you have an existing course in A+ which does not use Docker, see the chapter
`Converting an existing A+ course to Docker
<../m04_converting/01_virtualenv_to_docker>`_ for reasons to convert it to
Docker.

.. admonition:: File format: YAML
  :class: meta

  `YAML <http://yaml>`_ is a human-friendly language for defining data
  for computer programs. In Docker and A+ it is used for writing
  *configuration files*, that is, files which control the behaviour of
  A+ and some types of exercises. The file suffix is ``.yml`` or
  ``.yaml``. For a short introduction to the grammar of YAML, see
  `part "Preview" of the YAML specification"
  <http://yaml.org/spec/1.2/spec.html#Preview>`_ .

Learning Docker
---------------

This A+ manual itself will not describe the basics of Docker. This is
because most of the time the person who is writing or updating a course
for A+ actually just needs to install Docker, Docker Compose and
execute the ``./docker-compile.sh`` and ``./docker-up.sh`` commands.
To actually learn Docker, begin with the `"Get started" tutorial at Docker
documentation <https://docs.docker.com/get-started/>`_.

The A+ architecture
-------------------

It is good to know a little what happens inside your computer when you
develop a course. This is *required* if you plan to include your course
exercises that are more than simple quizzes.

.. image:: /images/aplus-architecture.png

The image above shows the software architecture of A+. The course directory
on your computer has RST files. When you run ``docker-compile.sh``, it
requests Docker to run a container called ``compile-rst``. Inside that
container is a minimal `Debian GNU/Linux operating system
<https://www.debian.org/>`_, Python programming language interpreter,
Sphinx and Python libraries for producing YAML files. The container
is allowed to access the ``a-plus-rst-tools`` directory which contain
essential Sphinx directives for producing right kind of HTML and YAML
files for A+. Sphinx runs inside the container and writes its results
to the directory ``_build`` in the course directory.

Next, when you start A+ with ``docker-up.sh``, two containers are started.
The container ``run-aplus-front`` is similar to the compile-rst container,
but it contains the A+ software - the one you can access at
http://localhost:8000. This container is allowed to read the HTML and YAML
files at the ``_build`` directory. It is good to know that those files
specify the actual structure and contents of the course.

Another container that ``docker-up.sh`` starts is ``run-mooc-grader``.
It runs the typical work pair of A+, the **mooc-grader**.
The share of work between A+ and mooc-grader is the following. A+ is
a *front-end*, the piece that shows to the student. It knows who is
logged in, which students are taking which course, which students
have answered to some exercises and how many points they got. A+ does
all the bookkeeping.

Meanwhile, mooc-grader receives exercise files from
students. For each submit, it starts a Python grader in the container
``grading-python``. Inside that container the student's program is
actually run and unit tests executed. The results of the unit tests
are passed to mooc-grader which passes them to A+. Then A+ shows
the score and feedback to the student.

This means that exercise solutions that students have submitted will not remain
on mooc-grader after grading; instead, they are stored in A+. Mooc-grader
also hosts the so-called *static content*: HTML files and images
which do not change - the ones in the course ``_build`` directory.

Mooc-grader also reads exercise configurations from the course directory.
Each exercise has its own directory named ``exercises/exercisename/``,
which contains typically the following files:

- ``run.sh``: a *shell script*: some UNIX shell commands for running Python
  with a grading library

- ``config.yaml``: a description for mooc-grader on how to start another
  container ``grading-python`` which actually runs the tests

- ``test_config.yaml``: a configuration file for **A+ grader utils**:
  grading settings

- ``grader_tests.py``: the actual Python unit tests for the exercise.
  Exercise points will be given according to these.

The grading-python container has other Python libraries, like
`Hypothesis <https://pypi.org/project/hypothesis/>`_ and
`A+ Python grader utils
<https://github.com/Aalto-LeTech/python-grader-utils>`_.

In the top of the architecture image, there is the **Aalto Gitlab
service** at https://version.aalto.fi , where your work will be copied
by the command ``git push``. Moreover, some courses use a
`GitLab Webhook
<https://docs.gitlab.com/ee/user/project/integrations/webhooks.html>`_,
which automatically copies the course material to the A+ production
server, when the author pushes the material to version.aalto.fi at some
predefined git branch, like "publish". At least course
*CS-A1141 Tietorakenteet ja algoritmit Y* uses this technique.




Programming language support in A+
..................................

If you author a course which includes programming exercises, it is nice
to know that there are already many containers for grading programming
exercises in different languages. The source code and documentation for
these containers exists the `A-plus LMS Github directory
<https://github.com/apluslms/>`_ . For example, there is support for
automatic testing and grading for Clingo, Java, MiniZinc, Scala, and
even Python-based web applications with Selenium. These container images
are of course available at `Docker hub
<https://hub.docker.com/r/apluslms/>`_, meaning that Docker will
automatically download them if you define in the course configuration
files that you will need them. If your course needs software which is
not yet available as containers for A+, see the
`A-plus LMS Github page <https://apluslms.github.io/>`_ for
contact information.
