First Steps
===========

In the start there was A-Plus.
That was good, but a developer thought we needed something more.
Thus, MOOC-Grader was created.
Time passed and now we have many micro services that provice our new way of life, A+ LMS.

That is, this is a codebase which teaches how to make a new course on
`A+ e-learning system <https://github.com/Aalto-LeTech/a-plus>`_. It is currently
used on some computer science courses on Aalto University.

.. admonition:: File format
  :class: alert alert-info

  The web pages of A+ courses are written in 
  `RST <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.
  RST is simpler in syntax than HTML. A Python software called
  `Sphinx <http://www.sphinx-doc.org>`_ compiles bunch of RST files into
  HTML. We will come into writing RST files later.



Getting started
---------------

Software prerequisites
......................

This tutorial is tested with Aalto Ubuntu Linux environment and it probably works
on any Unix / Linux / Mac environment. It is assumed that you already have
the following software:

- `git <https://git-scm.com/>`_
- `make <https://www.gnu.org/software/make/>`_

These are already in Aalto Linux. In a generic Ubuntu or Debian GNU/Linux
environment, you must install packages ``git`` and ``build-essential``.

All other software runs inside `Docker <https://www.docker.com/>`_ containers.
For short, Docker is the new software platform for running A+ and software
related to it.

Install Docker for Mac/Windows or docker-ce & docker-compose for Linux.

- `Docker Community edition <https://docs.docker.com/engine/installation/>`_
- `Docker Compose <https://docs.docker.com/compose/install/>`_

In Aalto you need administrator rights to your machine to install these
on your machine by yourself, or have an administrator to install them for you.
Aalto IT services at Computer Science building helps with this.


Cloning this codebase with git
..............................

A good way to start is to clone this repository with git and begin to work on it. 
In Aalto, you could use `version.aalto.fi repo <https://version.aalto.fi/gitlab/course/aplus-manual>`_.
Please note that if you don't have access, then you can request one.
In that case, you probably should be part of :code:`apluslms-cs@aalto.fi` email list too.

To clone, execute command:

.. code-block:: sh

    git clone git@version.aalto.fi:course/aplus-manual.git
    cd aplus-manual

In public, you could use `github repo <https://github.com/apluslms/course-templates/tree/manual>`_.

.. code-block:: sh

    git clone --branch manual https://github.com/apluslms/course-templates.git
    cd course-templates

Next step, you need to get :code:`a-plus-rst-tools`.

.. code-block:: sh

    git submodule init
    git submodule update

Now all the course material is in RST format. Everytime the RST part changes,
you need to recompile it. You must do it also in the first time:

.. code-block:: sh

    ./docker-compile.sh

This basically runs Sphinx inside a Docker container. Sphinx reads all RST files.
It produces compilation results into new directory ``_build``. That contains
three subdirectories. ``doctrees`` has intermediate results of compilation.
``html`` has the HTML versions of the RST documentation. ``yaml`` contains
configuration files in `YAML format <https://en.wikipedia.org/wiki/YAML>`_
and they are also meant for A+.

For now, you can test the result by running A+ on your own computer:

.. code-block:: sh

    ./docker-up.sh

Now A+ runs at http://localhost:8000. Open that address with your web browser.
You must login by the maintenance login showing on the front page. The available
users are `root`:`root` and `student`:`student`.  The default course is created
from the material.

The end
-------



.. image:: /images/apluslogo.png

Above there is an example image.

Final words and end of chapter.
