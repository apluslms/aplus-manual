Converting an existing A+ course to Docker
==========================================

Introduction and motivation
---------------------------

If you maintain an existing A+ course, and it uses a `Python virtual
environment <https://docs.python.org/3/tutorial/venv.html>`_ (just
"virtualenv"), this section describes how to convert it to the `Docker
environment <../m01_introduction/05_docker>`_.

An A+ course not using Docker does not have ``docker-compile.sh`` and
``docker-up.sh`` scripts. Instead, the course is typically compiled with
commands ``source venv/bin/activate`` and ``make html``. A Python virtualenv is
more like a Python package manager compared to Docker; each virtualenv installs
a specific version of Python and specific version of libraries. A+ Docker
containers also have that, but moreover, they have all the software
preconfigured and ready to use. In contrast, developing a virtualenv A+ course
with also A+ and mooc-grader installed on your computer with virtualenv requires
extra manual configuration steps. Therefore the aim of A+ Docker containers is
to make course development and deployment as easy as possible.

Modifying your git repository
-----------------------------

New branch
..........

From now on, this text assumes that you have your current A+ course under
`git version control <../m01_introduction/04_git>`_.

First, ``cd`` to the current directory of your course. Create a new `git branch
<https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>`_
for the Docker version.

.. code-block:: sh

    git branch docker
    git checkout docker

It is recommended to add a to-do document for making the Docker version, for
example, ``Docker-TODO.txt`` in the main directory.

.. code-block:: none

    This is the to-do list for making a Docker version of this course.

    TODO
    ====
    - copy files from aplus-manual
    - update conf.py
    - check RST files
    - modify exercise graders

    DONE
    ====

Some people and teams prefer to have their task lists in `Trello
<https://trello.com/>`_. Do what suits you best.

Create a directory ``old`` and move all the current files into it. This
directory will have all the course material which is not yet converted to the
Docker version. The idea is to move files back from there in small groups and
test them. This way you will easily see what is done, and the rest of the files
will not cause Sphinx compilation errors or other trouble.

.. code-block:: none

    mkdir old
    git mv -k * old

Note that the hidden subdirectory ``.git``, and files ``.gitignore`` and
``.gitmodules`` will not be moved, as they should.

Commit and push to `Github <https://github.com/>`_, `Aalto Gitlab
<https://version.aalto.fi/>`_ or whatever git service you have. The
``--set-upstream`` option is used only this time; it allows you to later say
just `git push` and it will automatically push your commits to the ``docker``
branch on the remote git service.

.. code-block:: none

    git commit -m "First commit of Docker version"
    git push --set-upstream origin docker

Import aplus-manual
...................

Copy files from the ``aplus-manual`` directory, excluding the ``.git``
directory, to the directory of your course. For example:

.. code-block:: none

    cp -r ../aplus-manual/* .

Add directory ``_data`` to the ``.gitignore`` file of your course. That
directory is a write-enabled directory for A+ and mooc-grader which can always
be removed. Add latest A+ RST tools as submodule.

.. code-block:: none

    echo _data >> .gitignore
    git submodule add https://github.com/Aalto-LeTech/a-plus-rst-tools

Add directory ``old`` to ``exclude_patterns`` in file ``conf.py``. This way
Sphinx will not compile material which is in the ``old`` directory.

.. code-block:: python

    # List of patterns, relative to source directory, that match files and
    # directories to ignore when looking for source files.
    exclude_patterns = ['_build', '_data', 'exercises/solutions', 'old']

Finally, add all new files, commit and push.

.. code-block:: python

    git add *
    git commit -m "Added A+ manual codebase"
    git push

Congratulations! Now you have all the initial git voodoo done. You have a new
branch on your course repository, which has a working copy of the A+ manual and
your current course material in the ``old`` directory. You can compile the
material and run A+ and mooc-grader locally `as specified in the introductory
module <../m01_introduction/02_rst.html#workflow-for-editing-rst-files>`_.
