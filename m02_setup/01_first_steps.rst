.. The roles  should be created at the beginning of the document. Global roles can be created in the `global.rst` file

.. include:: /global.rst

.. Chapter content

First steps
===========

.. styled-topic::

  Main questions:
      How to run the template course? and how to install the required software in your computer?

  Topics:
    In this section, we talk about:

    * `Knowledge prerequisites`_
    * `Software prerequisites`_
    * `Cloning this codebase with git`_
    * `Workflow`_

  Material:
    In this chapter, you won't need extra material.

  Requirements:
    You need basic computational skills to install some software in the Linux OS, and some knowledge on git.

  Estimated working time:
    From 30 min to 1 hour.
    
The `Aplus course Template <https://github.com/apluslms/aplus-course-template>`_ is a template that you will use to build your own course on the `A+ <https://github.com/apluslms/a-plus>`_ platform. You can also download the :abbr:`codebase (Codebase is a collection of source code used to build a particular software system, application, or software component.)` of this manual to understand better what is happening under the hood. Perhaps you could copy some of the directives we are using in your own course. The codebase of this manual is available in the GitHub `Aplus manual <https://github.com/apluslms/aplus-manual-dev>`_ repository.

The web pages of A+ courses are written in `RST <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_. RST is simpler in syntax than HTML. A Python software called `Sphinx <http://www.sphinx-doc.org>`_ compiles a bunch of RST files into HTML. However, we will explain more about :doc:`RST and Sphinx </m03_rst_guide/01_get_started>` later.

.. admonition:: Epigraph :glyphicon-certificate:`\ `
  :class: meta

  In the start there was A+. That was good, but a developer thought we needed something more. Thus, MOOC-Grader was created.

  Time passed, and now we have many microservices that provide our new way of life.

  -- A+ LMS

If you are already running the course template on your computer, and seeing the content in a web browser, *congratulations!* You can skip the rest of this page. 

Knowledge prerequisites
-----------------------

This manual assumes you have some basic UNIX operating system skills. It also assumes that you can use GNU/Linux (Ubuntu, Debian) or modern Mac OS, and assumes that you know some basic :abbr:`Unix terminal (The terminal is a text-based window where you type commands, and the terminal shows the results by printing one or more lines of text.)` commands. You also need to know how to install some software in your computer. 

In this course, we will teach you how to install and how to use the software.

.. image:: /images/terminal.png
  :width: 70%
  :align: center

.. admonition:: Software: UNIX Shell, Terminal emulator
  :class: alert alert-info

  The above image list the content of the **aplus-manual**
  directory, in a terminal emulator window. In practice, some terminal
  commands are required for the usual workflow of writing
  a new course for A+.

  The terminal is used for moving and copying files, starting software
  and examining their error messages. To be precise, there is the terminal
  emulator window and inside it another program, `shell`, which reads
  user commands and acts according to them. If you are new to this, read the
  `"Learning the shell" LinuxCommand.org <http://linuxcommand.org/lc3_learning_the_shell.php>`_
  tutorial parts 1-6.

Software prerequisites
----------------------

The first step to start authoring a course is to install some required software on your computer. The first two software you need are `git <https://git-scm.com/>`_ and `make <https://www.gnu.org/software/make/>`_. Sometimes, these two software are installed by default, but if the **git** and **make** are not installed by default, you can install them by running the :ref:`commands below <install-git>` in your machine. Otherwise, you can consult the official documentation on how to `install git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_, and how to `install make <https://pkgs.org/download/build-essential>`_ in your OS. 

.. warning:: 
  if you are using an Aalto's computer, you will need administrator rights to install the required software; otherwise, you can ask an administrator to install them for you. `Aalto IT services <https://www.aalto.fi/en/service-entities/it-services>`_ have administrator rights for all the Aalto's computers. 

.. code-block:: bash
  :name: install-git
  :caption: 1- Install Git

  sudo apt update
  sudo apt install git

.. code-block:: bash
  :caption: 2- Verify git version

  git --version

.. code-block:: bash
  :caption: 3- Install build-essential, which includes make.

  sudo apt update
  sudo apt install build-essential

.. code-block:: bash
  :caption: 4- Verify make version

  make --version

::::

All other software runs inside `Docker <https://www.docker.com/>`_ containers.
For short, Docker is the new software platform for running A+ and software
related to it. This course will discuss Docker later.

Install Docker for Mac/Windows or docker-ce & docker-compose for Linux.

- `Docker Community edition <https://docs.docker.com/engine/installation/>`_
- `Docker Compose <https://docs.docker.com/compose/install/>`_

You also need to install a Text editor (`VS Code <https://code.visualstudio.com/>`_  is recommended). You can find more information about the most convenient text editor to create *RST* documents :ref:`at the end of this module <text-editor-and-ides>`.

Cloning this codebase with git
------------------------------

A good way to start is to clone the `Aplus course Template <https://github.com/apluslms/aplus-course-template>`_ with git and begin to work on it. In Aalto, you could use `version.aalto.fi repo <https://version.aalto.fi/gitlab/course/aplus-manual>`_. Please note that if you don't have access, then you can request access to the *Aalto IT services*. In that case, you probably should be part of :code:`apluslms-cs@aalto.fi` email list too.

To clone, execute the following command:

.. code-block:: sh

    git clone git@version.aalto.fi:course/aplus-manual.git
    cd aplus-manual

In public, you could use `GitHub repo <https://github.com/apluslms/course-templates/>`_.

.. code-block:: sh

    git clone https://github.com/apluslms/course-templates.git
    cd course-templates

Next step, you need to get :code:`a-plus-rst-tools`.

.. code-block:: sh

    git submodule init
    git submodule update

Now all the course material is in RST format. Every time the RST part changes,
you need to recompile it. You must do it also the first time. Open your terminal, go to the course directory and type the following command.

.. code-block:: sh

    ./docker-compile.sh

This command runs Sphinx inside a Docker container. Sphinx reads all RST files.
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

.. warning:: 
 
  If you do not have solid knowledge in *RST* and terminal, it is recommended to install an IDE. This manual have instructions on how to install `VSCode <https://code.visualstudio.com/>`_, and how to use it in order to create course content more efficiently. If you follow the instruction provided in the :doc:`/m02_setup/04_vs_code` chapter, your development environment will be less error-prone.

Workflow
--------

The usual workflow for creating/editing a course is the following:

1. Open your text editor, a terminal and a web browser.
2. Edit some RST files in your text editor.
3. Give command ``./docker-compile.sh`` in the terminal.
4. Give command ``./docker-up.sh`` in the terminal.
5. Go to ``http://localhost:8000/`` in the web browser to view A+
    running on your machine.
6. Examine the changes you made in A+.
7. Press :kbd:`Q` or :kbd:`Ctrl` ``+`` :kbd:`C` in the terminal to quit and remove data
    or :kbd:`S` or :kbd:`ESC` to quit and keep data.
8. Go to step 2 if you wish to continue editing.
9. Give command ``git add -u`` in the terminal to mark all changed files to be
    added into your local git repository.
10. Give command ``git commit -m "message"`` in terminal. Replace ``message`` with a short description (preferably less than 60 characters) on what you have done.
11. Remember also to say ``git push`` a couple of times in a day. This copies your updates to the course material to the Gitlab server ``version.aalto.fi``.