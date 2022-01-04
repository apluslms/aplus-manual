Introduction to A+
==================

A+ learning management system (LMS) enables teachers to variedly utilize both **(1)** *automatic assessment*
and **(2)** *interactive, smart learning content*.
First, A+ has no limitations on the implementation of automatic graders:
you may create any kind of assignment in A+ as long as
you are able to develop a *grader program* (often called just a *grader*) for it.
Graders receive the student's submission as input and output its score and textual feedback.
The feedback may be as simple or rich as you want and are able to programmatically generate.
Second, A+ allows you to freely develop the online learning materials:
you can control the HTML markup of the course web pages as well as the JavaScript code and CSS styles.
For example, you may develop interactive visualizations in JavaScript and easily embed them into the course materials.

A+ has been used to automatically grade *various kinds of assignments*, for example:

* Programming in Python, Scala, C, C++, JavaScript and MATLAB to name a few.
  Graders are often implemented either as a set of unit tests or
  as input/output tests that check the strings printed by the student's program.
* Relational databases: SQL queries and relational algebra expressions.
* Web frontend (JavaScript, CSS) and backend programming.
* Theoretical computer science: finite-state automata, regular expressions, context-free grammars and parse trees.
* Mobile applications on Android.
* Creating containers with Dockerfiles.
* Interactive exercises on the :abbr:`Acos server (Advanced Content Server, a method of distributing browser-based smart learning content in a reusable and interoperable way)` platform, for example:
  point-and-click,
  drag-and-drop,
  :abbr:`Jsvee (JavaScript Visual Execution Environment, a JavaScript library for providing common core features required for creating program animations)` program animations, and
  :abbr:`Parsons programming puzzles (Parsons programming puzzles are a type of scaffolded program construction tasks where the learner is given a set of code fragments, blocks of a single or multiple lines of code, and the task is to piece together a program from these.)`.
* Questionnaires with multiple-choice questions and text entry questions.
  Text entries may be automatically graded with
  `regular expressions <https://en.wikipedia.org/wiki/Regular_expression>`_.
* It is also possible to manually assesses assignments in A+.
  There is also an A+-compatible tool called Rubyric that focuses on manual grading with rubrics.

In A+, course contents and assignments are developed in *open, plain text file formats*.
You own the materials yourself: there is no vendor lock-in in proprietary file formats or
:abbr:`WYSIWYG (What You See Is What You Get)` editors
that can not export the contents to an open format.
You can freely develop and edit the materials in your own computer
using the editors and development tools of your choosing.
Often-used file formats in A+ include
:abbr:`HTML (HyperText Markup Language, the markup of web pages)`,
:abbr:`RST (reStructuredText)` and Markdown which are converted to HTML, as well as
:abbr:`YAML (YAML Ain't Markup Language, a human-readable data-serialization language)` and
:abbr:`JSON (JavaScript Object Notation, a data interchange format for objects consisting of name-value pairs and arrays)`
for assignment configuration files.
Automatic graders can be developed in any programming language.
If need be, you could convert your course materials to any other format and import them to another learning platform.
Furthermore, the static web pages in the HTML format (excluding automatically assessed assignments)
could be easily deployed to any web server without relying on any LMS software.

A+ course contents are stored in a repository under *Git version control*.
Git keeps track of the changes in your course and
you can also update the course in the server by simply pushing to the Git repository.

While developing course materials and assignments,
you can run the whole A+ platform on your own computer in `Docker`_ *containers*.
You can test new materials without interfering with the server
while real students are accessing the course.


Automatic graders
-----------------

In order to grade an assignment automatically, you must first develop a grader program for it.
Automatic graders are usually developed on the MOOC-Grader platform.
MOOC-Grader has two main features for grading:

1. questionnaires that are graded
   :abbr:`synchronously (Synchronous grading is completed immediately without delay. Its computational load must be minimal.)`
   and
2. container-based
   :abbr:`asynchronous (Asynchronous grading is not completed immediately. Its computation may last for several seconds or minutes. The grader sends the grading results back to the platform once it has finished.)`
   graders that you program yourself.

MOOC-Grader is an *exercise service* (also known as *grader service*) for A+.
It is also possible to develop new, custom exercise services, but usually that is not necessary.

In the MOOC-Grader, graders for assignments are *stateless*.
**The grader**

* grades one submission at a time,
* receives the student's submission as input,
* outputs the score (a whole number) and feedback for the submission,
* consists of any files and programs that the course staff has created using the technologies of their choosing,
* is run in a container that securely isolates the execution from the platform and other submissions, and
* has no access to data about the student's other submissions or other students' submissions.

The student's *submission* may consist of uploaded files,
data inserted into a form or by some other interactions, or
a git repository which the student has pushed the solution into.
The *score* or *points* of the submission are given as a whole number out of the maximum that may be set freely.
The grader may use a different maximum score than the A+ platform,
in which case A+ scales the points to the maximum in A+.
The *feedback* generated by the grader may be formatted in plain text or HTML markup.
Typically, automatically graded assignments show the feedback to students as soon as it is available,
but the feedback may also be delayed
so that the students gain access to it only at the time specified by the teacher,
for example, after the deadline.

Grading *containers* are normally based on Debian Linux and built with Docker.
You may install any necessary tools, frameworks and libraries in the Docker image of the grading container.
We have several `Docker images`_ available that have basic tools for different programming languages installed.
You may also define your own Dockerfile and use that image for grading.
We recommend that grading containers are based on our `grading-base`_ image
that includes some utilities and configurations for compatibility with the MOOC-Grader.

A new container is launched for grading each submission.
The MOOC-Grader server may grade multiple submissions concurrently, thus
multiple containers could be running at the same time.
It is also possible to configure a grading server so that
it runs only one submission at a time.
This is useful if the grader needs to measure the execution time of the submission.
Measuring time is more reliable when the hardware is not contested by multiple processes.

Often, the grader in the container starts with a Bash script that is sometimes named "run.sh".
Run.sh typically manages preparations for the grader and then starts it.
For example, in a Scala programming course,
run.sh could first compile the submitted Scala code,
set the CLASSPATH
:abbr:`environment variable (Environment variables are defined in the environment in which processes are run. The process may use them to change its behaviour, for example, to define configurations.)`
so that the process finds the necessary Scala libraries and finally
run the unit tests that output the points and feedback.
After the process has finished, the container sends the results back to the MOOC-Grader,
which then forwards them to A+.


Course study materials
----------------------

One A+ course consists of *modules*
(also known as *exercise rounds*, *rounds* or *weeks* depending on the course).
A module has an opening time and a closing time (deadline) that
restrict assignment submissions.
It is also possible to open the study materials of the module before the assignments
(by setting the "read opening time").
A module may be set to allow *late submissions* until the late submission deadline.
A late penalty that deducts a percentage of the score may be applied to late submissions.
The teacher may grant *personal deadline extensions* ("deviations") to students.

A module consists of *chapters* and *assignments*.
Chapters form the study materials,
which could contain, for example,
text, images, embedded videos, specialized visualizations,
and of course automatically graded assignments embedded in the chapter.
You may freely use web technologies (JavaScript, HTML, CSS)
in order to develop specialized tools when necessary.
If you only want to write text, it is easy to do so in RST.
It is also possible to include only assignments without any chapters in the course.

A+ chapters are often written in the :abbr:`RST (reStructuredText)` markup,
but using RST is not mandatory.
`Sphinx`_, the RST compiler, can also compile Markdown files
(using `recommonmark <https://recommonmark.readthedocs.io/>`_
or `MyST <https://www.sphinx-doc.org/en/master/usage/markdown.html>`_).
Sphinx is a tool for creating documentation
that can be compiled into multiple formats, such as HTML and LaTex PDF.
Sphinx itself extends the `Docutils`_ RST parser and compiler.

For courses using the RST content format and/or Sphinx,
A+ includes a module called `A-plus-rst-tools`_.
A-plus-rst-tools comprise a set of Sphinx extensions that
contain useful RST
:abbr:`directives (In RST, directives are blocks that require special handling. Directives are used, for example, to add images, admonitions or code blocks. It is possible to develop new directives in Sphinx extensions.)`
for A+ course materials,
particularly the directives for embedding assignments in chapters.
A-plus-rst-tools are included in the course repository as a Git submodule.

If you don't like writing RST or Markdown,
you could also write HTML directly.
A+ has only a couple of requirements for the structure of the HTML document
so that it can be used as an A+ chapter.
The requirements are specified in the
`CONTENT.md documentation <https://github.com/apluslms/a-plus/blob/master/doc/CONTENT.md>`_.
You could also write chapters in any other format that can be compiled into HTML.


Architecture of A+
------------------

The main components of A+ are the frontend server and exercise services.
The frontend server is responsible for

* the student's uniform user interface,
* retrieving course materials and assignments from the backend Git manager service and exercise service,
* forwarding submissions to the exercise service for grading,
* storing submissions and grading results (points and feedback) in the database, and
* teacher's functionalities such as inspecting submissions and manual assessment.

The :ref:`figure <aplus-architecture>` below presents the architecture of the components.
The figure includes only one exercise service, the MOOC-Grader.

The teacher edits the course contents on his/her computer and
pushes the changes to the Git server.
The Git repositories are typically hosted on a `GitLab`_ server.
(At Aalto University, the GitLab server is called `Version`_.)
The GitLab project is configured with a webhook so that
it notifies the A+ Git manager service of the course update.
The A+ Git manager service pulls the update and builds the course.
Building includes, for example, compiling the study materials written in RST to HTML.
You define yourself what processes are run during the build.
For example, you could compile materials written in other markup than RST, or
package source code templates (skeleton code) into archives
that the students download as a starting point for a programming assignment.
(If you package files in the build,
you don't need to manually package them and store the archive in the Git repository.)

The A+ frontend retrieves the contents of the assignment from the exercise service.
The exercise service to use is defined by the assignment settings.
The retrieved assignment content is shown to the student in the A+ website, and
it typically includes the instructions for the assignment and
a form for making the submission (e.g., uploading a file).
For an interactive assignment,
the content could include a specialized editor that the students use to create their solutions.
You may include any JavaScript code in the assignment in order to implement specialized editors or widgets.
When the student submits, A+ saves the submission in its database and
sends the submission to the exercise service for grading.
The exercise service sends the points and feedback back to A+ (not necessarily immediately).
In the case of the MOOC-Grader,
when it receives a new submission from the A+ frontend,
it launches a new grading container.
The container sends the grading results back to the MOOC-Grader,
which sends them to the A+ frontend.

The most used exercise service is the `MOOC-Grader`_ platform.
Other widely used services include `Acos server`_ (`demo`_) and `Rubyric`_.
Acos server is a platform for distributing browser-based smart learning content in a reusable and interoperable way.
Rubyric is a tool for manual assessment:
it supports pre-defined grading rubrics that may be used to score submissions and to provide feedback.
The feedback may also be freely modified so that it is not constrained to the rubric.
In addition, Rubyric has limited support for peer reviews between students.
It is possible to develop new, specialized exercise services,
but usually it is not necessary.
The A+ frontend connects to the exercise service with the grader protocol,
which uses :abbr:`HTTP (Hypertext Transfer Protocol)` GET and POST requests with a few parameters.
The protocol is described in the
`GRADERS.md documentation <https://github.com/apluslms/a-plus/blob/master/doc/GRADERS.md>`_.
A new exercise service could, for example, be stateful as opposed to the stateless MOOC-Grader.
It could combine data from multiple submissions and retrieve additional data
from the A+
:abbr:`REST (Representational State Transfer, a software architectural style for stateless, reliable web APIs that are based on HTTP methods to access resources and use JSON to transmit data)`
:abbr:`API (Application Programming Interface)`.
Its implementation does not have to depend on containers like the MOOC-Grader does.

It is worth mentioning the `Radar`_ service.
It is not an exercise service,
but a tool for the similarity analysis (plagiarism detection) of the submitted source code in programming assignments.
Radar retrieves submission data from A+ via the API.


.. note::

  We have said that the MOOC-Grader launches containers for grading submissions.
  When you run A+ on your own computer during the course development and testing,
  the containers are run on `Docker`_.
  However, in the production servers at Aalto University,
  the containers are run on `Kubernetes`_.
  This makes no practical difference in most courses
  and the grading containers function locally in the same way as in the production servers.


.. _aplus-architecture:

.. code-block:: text

  Student           ________________
    |              | Database:      |
    | http         | submissions,   |   Course staff/Teacher
    |              | grading results|                  |
  A-PLUS-FRONT --->|                |  Push the course |
    |              |________________|           to Git |
    | http                                             |
    | Fetch exercise                                   |
    | Grade submission          Build the course:  ____v__
    |                                   make html |       |
  MOOC-GRADER <-----------------------------------|  Git  |
      |                          a-plus-rst-tools |_______|
      |-- _build/yaml/index.yaml                   |
           |                                       |-- index.rst
           |-- _build/yaml/asgn_hello_python.yaml  |    |
                    |                              |    |-- chapter1.rst
                    | Grade submission             |
                    | Docker/Kubernetes            |-- exercises/
                    |                                  |-- hello_python/
        apluslms/grade-python:3.9-4.3-4.0                  |-- grader_tests.py


Structure of the Manual
-----------------------

This A+ Manual (or Aplus Manual) has been created as an A+ course.

* The manual course is deployed at https://plus.cs.aalto.fi/aplus-manual/master/
* The Git repository with the source code is in GitHub: https://github.com/apluslms/aplus-manual

  - You can clone the course to your computer and run it in Docker containers!
  - See instructions in the `Aplus Manual README`_.

This first module of the manual course provides an overview of the platform.
The rest of the modules explain topics in more detail.

* :doc:`Set up your environment <../set_up_environment/first_steps>`:
  the installation of Docker, Git and text editors
* :doc:`RST guide <../rst_guide/get_started>`:
  how to write reStructuredText markup
* :doc:`Style Aplus courses <../style_aplus/css>`:
  how to use CSS to change the appearance of the course pages
* :doc:`Questionnaires <../questionnaires/questionnaires>`:
  how to make questionnaires (multiple-choice questions) in RST
* :doc:`Programming assignments <../programming_exercises/instructions>`:
  how to automatically grade programming assignments
* :doc:`Acos server <../acos/introduction>`:
  interactive browser-based smart learning content
* :doc:`Rubyric <../rubyric/introduction>`:
  manual rubrics-based assessment in Rubyric
* :doc:`LTI <../lti/introduction>`:
  the standard Learning Tools Interoperability protocol in A+
* :doc:`Interactive code blocks <../interactive_code/guide>`:
  code blocks that allow the student to modify the code
  and execute it in the server backend in order to see the output
* :doc:`Course administration <../admin/settings>`:
  A+ course settings
* :doc:`Multilingual course materials <../languages/languages>`:
  how to make multilingual courses
  that have the same contents and assignments in multiple languages (e.g., Finnish and English)
* :doc:`Active elements <../active_elements/introduction>`:
  how to make active elements, i.e.,
  ungraded, interactive tools embedded in A+ chapters
  that process user input asynchronously in the same way as assignment graders
* :doc:`Points of interest <../point_of_interest/introduction>`:
  how to embed browsable summary blocks in A+ chapters
* :doc:`Moodle Astra plugin <../moodle_astra/introduction>`:
  a Moodle plugin that replicates the A+ frontend in Moodle
* :doc:`Adding new Sphinx extensions <../sphinx_extensions/guide>`:
  how to add new Sphinx extensions to A+ courses


.. _Docker: https://www.docker.com/
.. _Docker images: https://hub.docker.com/u/apluslms
.. _grading-base: https://github.com/apluslms/grading-base/
.. _Sphinx: https://www.sphinx-doc.org/
.. _Docutils: https://docutils.sourceforge.io/
.. _A-plus-rst-tools: https://github.com/apluslms/a-plus-rst-tools/
.. _GitLab: https://gitlab.com/
.. _Version: https://version.aalto.fi/
.. _MOOC-Grader: https://github.com/apluslms/mooc-grader
.. _Acos server: https://github.com/acos-server/acos-server/
.. _demo: https://acos.cs.aalto.fi/
.. _Rubyric: https://github.com/apluslms/rubyric
.. _Radar: https://github.com/apluslms/radar
.. _Kubernetes: https://kubernetes.io/
.. _Aplus Manual README: https://github.com/apluslms/aplus-manual/blob/master/README.md
