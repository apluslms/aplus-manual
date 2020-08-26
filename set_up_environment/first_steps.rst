First steps
===========

.. styled-topic::

  Main questions:
      How to run a template course and how to install the required software in your computer?

  Topics:
    In this section, we will present the following topics:

    * `Knowledge prerequisites`_
    * `Software prerequisites`_
    * `Cloning this codebase with git`_
    * `Workflow`_

  Material:
    In this chapter, we do not provide additional material.

  Requirements:
    You need basic computational skills to install some software in the Linux OS, and some knowledge on git.

  Estimated working time:
    From 30 min to 1 hour.

The first step to start authoring your own course is to download the `Aplus course Template`_ from GitHub. This course
template will be used as a blueprint to build your own course and subsequently publish it in the
`A+ e-learning system <https://plus.cs.aalto.fi/>`_.

It is important to know that the course content is created with the help of a markup language called
`RST <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_. RST is simpler in its syntax than HTML, and is also
highly customizable, which is a tremendous opportunity for creating well-tailored exercises and course material. A more
extensive description of the RST markup language will be presented in later chapters of this manual.

.. admonition:: Epigraph :glyphicon-certificate:`\ `
  :class: meta

  In the start there was A+. That was good, but a developer thought we needed something more. Thus, MOOC-Grader was
  created.

  Time passed, and now we have many microservices that provide our new way of life.

  -- A+ LMS

If you are already running this course template on your computer, and seeing the content in the web browser
http://localhost:8000/def/current, *congratulations!* You can skip the rest of this page.

Knowledge prerequisites
-----------------------

This manual assumes you have some basic UNIX operating system skills. It also assumes that you can use GNU/Linux
(Ubuntu, Debian) or modern Mac OS, and assumes that you know some basic
:abbr:`Unix terminal (The terminal is a text-based window where you type commands, and the terminal shows the results
by printing one or more lines of text.)` commands. You also need to know how to install software in your computer.

In this chapter, we will teach you how to install and how to use the software.

.. figure:: /images/terminal.png
  :width: 80%
  :align: center

  The above image list the content of the `Aplus course template <https://github.com/apluslms/aplus-course-template>`_
  directory, in a terminal window.

.. admonition:: Important: UNIX Shell, Terminal emulator
  :class: alert alert-warning

  The terminal is used for moving and copying files, starting software
  and examining their error messages. To be precise, there is the terminal
  emulator window and inside it another program, ``shell``, which reads
  user commands and acts according to them. If you are new to this, read the
  `"Learning the shell" LinuxCommand.org <http://linuxcommand.org/lc3_learning_the_shell.php>`_
  tutorial parts 1-6.

Software prerequisites
----------------------

The first step to start authoring a course is to install some required software on your computer. The first two software
you need to install are `git <https://git-scm.com/>`_. You can install git by running the
:ref:`following command<install-git>` in your computer.

.. code-block:: bash
  :name: install-git
  :caption: 1- Install Git

  sudo apt-get update
  sudo apt-get install git

.. code-block:: bash
  :caption: 2- Verify git version

  git --version


You can also consult the official documentation for
`installing git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_

.. warning::
  If you are using an Aalto's computer, you can install some of the required software by running the
  ``aptdcon --install`` command. It works with packages available in the default repositories. Therefore, docker cannot
  be installed that way. You will need administrator rights to install it. `More information at scicomp.aalto.fi
  <https://scicomp.aalto.fi/aalto/linux/#admin-rights>`_.

All other software runs inside `Docker <https://www.docker.com/>`_ containers. Therefore, you must install Docker for
Mac/Windows or docker-ce & docker-compose for Linux.

- `Docker Community edition <https://docs.docker.com/engine/installation/>`_
- `Docker Compose <https://docs.docker.com/compose/install/>`_

You also need to install a Text editor (`VS Code <https://code.visualstudio.com/>`_  is recommended). You can find more
 information about the most convenient text editor to create *RST* documents
 :ref:`at the end of this module <text-editor-and-ides>`.

Cloning this codebase with git
------------------------------

A good way to start is to clone the `Aplus course Template <https://github.com/apluslms/course-templates>`_ with
git and begin to work on it.

To clone the course template using a SSH key, execute the following command:

.. code-block:: sh

    git clone git@github.com:apluslms/course-templates.git
    cd course-templates

You can also clone the public GitHub repository by executing the following command

.. code-block:: sh

    git clone https://github.com/apluslms/course-templates.git
    cd course-templates

.. rst-class:: pull-right

:glyphicon-info-sign:`\ ` **Read more about**  `how to clone GitHub repositories
<https://docs.github.com/en/free-pro-team@latest/github/using-git/which-remote-url-should-i-use>`_

|

Next step, you need to get :code:`a-plus-rst-tools`.

.. code-block:: sh

    git submodule init
    git submodule update

Now all the course material is in RST format. Every time the RST part changes,
you need to recompile it. You must do it also the first time. Open your terminal, go to the course directory and type
the following command.

.. code-block:: sh

    ./docker-compile.sh

This command runs Sphinx inside a Docker container. Sphinx reads all RST files.
It produces compilation results into new directory **_build**. The **_build**
directory contains three subdirectories:

1. **doctrees** has intermediate results of the compilation.
2. **html** has the HTML versions of the RST files.
3. **yaml** contains configuration files in `YAML format
   <https://en.wikipedia.org/wiki/YAML>`_. These configuration files are used to
   set up the different services that are used in the course with A+, e.g.,
   MOOC-Grader, Acos and Rubyric.

For now, you can test the result by running A+ on your own computer:

.. code-block:: sh

    ./docker-up.sh

Now A+ runs at http://localhost:8000. Open that address with your web browser.
You must login with any of the existing accounts used for the development of the
courses:

========= ========= =================
username  password  privileges
========= ========= =================
root      root      admin
teacher   teacher   teacher
assistant assistant course assistant
student   student   student
========= ========= =================

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
10. Give command ``git commit -m "message"`` in terminal. Replace ``message`` with a short description (preferably less
than 60 characters) on what you have done.
11. Create a repository in version.aalto.fi
12. Add the remote branch
13. Push the changes to version.aalto.fi by running the ``git push`` command.


.. External links

.. _`Aplus course template`:  https://github.com/apluslms/aplus-course-template
