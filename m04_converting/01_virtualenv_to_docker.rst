Converting an existing A+ course to Docker
==========================================

Introduction and motivation
---------------------------

If you maintain an existing A+ course, and it uses a `Python virtual
environment <https://docs.python.org/3/tutorial/venv.html>`_ (just
"virtualenv"), this section describes how to convert it to the `Docker
environment <../m01_introduction/05_docker>`_.

An A+ course not using Docker does not have **docker-compile.sh** and
**docker-up.sh** scripts. Instead, the course is typically compiled with
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
example, **Docker-TODO.txt** in the main directory.

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

Create a directory **old** and move all the current files into it. This
directory will have all the course material which is not yet converted to the
Docker version. The idea is to move files back from there in small groups and
test them. This way you will easily see what is done, and the rest of the files
will not cause Sphinx compilation errors or other trouble.

.. code-block:: none

    mkdir old
    git mv -k * old

Note that the hidden subdirectory **.git**, and files **.gitignore** and
**.gitmodules** will not be moved, as they should.

Commit and push to `Github <https://github.com/>`_, `Aalto Gitlab
<https://version.aalto.fi/>`_ or whatever git service you have. The
``--set-upstream`` option is used only this time; it allows you to later say
just `git push` and it will automatically push your commits to the **docker**
branch on the remote git service.

.. code-block:: none

    git commit -m "First commit of Docker version"
    git push --set-upstream origin docker

Import aplus-manual
...................

Copy files from the **aplus-manual** directory, excluding the **.git**
directory, to the directory of your course. For example:

.. code-block:: none

    cp -r ../aplus-manual/* .

Add directory **_data** to the **.gitignore** file of your course. That
directory is a write-enabled directory for A+ and mooc-grader which can always
be removed. Add latest A+ RST tools as submodule.

.. code-block:: none

    echo _data >> .gitignore
    git submodule add https://github.com/Aalto-LeTech/a-plus-rst-tools
    git submodule init
    git submodule update

Add directory **old** to ``exclude_patterns`` in file **conf.py**. This way
Sphinx will not compile material which is in the **old** directory.

**Note:** If your course has custom Sphinx directives, don't worry. This chapter
will describe later how to include them into the Docker version of your course.

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
your current course material in the **old** directory. You can compile the
material and run A+ and mooc-grader locally `as specified in the introductory
module <../m01_introduction/02_rst.html#workflow-for-editing-rst-files>`_.

Custom Sphinx directives
------------------------

Your course might have custom Sphinx directives. If you have those, they are
probably now in the directory **old/extensions** the **.py** files. Some of them
might even require A+ RST tools, meaning that they have lines such as ``from
a_plus_rst_tools import aplus_nodes``. This section describes how to include
those to the Docker version of your course.

Currently the A+ manual has two custom directives in the **extensions**
subdirectory: **bootstrap_styled_topic.py** and **div.py**. Let's assume the
custom Sphinx directives of *your* course are currently in the directory
**old/extensions**.

1. If there are Sphinx directives (**.py** files) with similar name both in
   **extensions** and **old/extensions**, check whether they differ. That can
   be done with your text editor, or with the command
   ``diff extensions/NAME.py old/extensions/NAME.py`` in the shell; see
   ``man diff`` or the `GNU Diffutils page
   <https://www.gnu.org/software/diffutils/>`_.

   For those files which differ, you need to know which one is more recent
   and who has modified the file. You might like to try
   ``git blame extensions/NAME.py`` and ``git blame old/extensions/NAME.py``.
   The ``git blame`` command shows for each line of a file when and who has
   changed it. This might help contacting the authors in case you have not
   written the Sphinx directives yourself. Finally decide whether to keep
   the A+ manual version, your version, or merge manually the files.

2. Custom Sphinx directives not matching step 1 can just be moved to the
   right place, e.g. ``git mv old/extensions/NAME.py extensions/NAME.py``.

3. For the custom Sphinx directives which have a couple of
   ``from a_plus_rst_tools import`` in them, chances are you have a symbolic
   link **a-plus-rst-tools** in the
   **old/extensions** directory, which points to the **a_plus_rst_tools**
   subdirectory. That latter directory may have some specific, maybe old
   version of A+ RST tools. This kind of hack has been made because normally
   A+ RST tools exists as directory **a-plus-rst-tools**. This is an invalid
   Python module name, and therefore the directory has been renamed to
   **a_plus_rst_tools** in order to import Python functions from it in the
   custom Sphinx directive. Moreover, a symbolic link **a-plus-rst-tools** has
   been created to it, because A+ RST is cloned from Github by default that
   name.

   .. code-block:: none

       atilante@t31300-lr124 ~/ohj/a-ole/tts
        % cd old/extensions
       atilante@t31300-lr124 ~/ohj/a-ole/tts/old/extensions
        % ls -l
       total 52
       -rw-r--r-- 1 atilante domain users 1273 Jun  5 13:07 aplus_exercise.py
       drwxr-xr-x 5 atilante domain users 4096 Jun  5 13:31 a_plus_rst_tools/
       lrwxrwxrwx 1 atilante domain users   16 Jun  5 13:07 a-plus-rst-tools -> a_plus_rst_tools/
       -rw-r--r-- 1 atilante domain users 4346 Jun  5 13:07 aplus_submit.py
       -rw-r--r-- 1 atilante domain users 2715 Jun  5 13:07 bootstrap_button_collapse.py
       -rw-r--r-- 1 atilante domain users 3487 Jun  5 13:07 bootstrap_panel_table.py
       -rw-r--r-- 1 atilante domain users 1628 Jun  5 13:07 bootstrap_styled_topic.py
       -rw-r--r-- 1 atilante domain users 3147 Jun  5 13:07 div.py
       drwxr-xr-x 2 atilante domain users 4096 Jun  5 13:45 __pycache__/
       -rw-r--r-- 1 atilante domain users 5060 Jun  5 13:07 sql_submit.py
       -rw-r--r-- 1 atilante domain users 1809 Jun  5 13:07 submit_no_tests.py
       -rw-r--r-- 1 atilante domain users 1116 Jun  5 13:07 yaml_extras.py

   Likely you want to use the latest A+ RST tools with your custom Sphinx
   directives. In that case, create a symbolic link from the *new*
   **extensions** directory

   .. code-block:: none

      ln -s ../a-plus-rst-tools a_plus_rst_tools

4. As a later development step, you may want to check whether the functionality
   of your custom Sphinx directives is actually included in the latest A+ RST
   tools.

Merging conf.py
---------------

Next you will have to merge **old/conf.py** to **conf.py**. Copy lines from
the former to the latter. Run ``./docker-compile.sh`` to ensure that nothing
has broken.

Possible errors encountered
...........................

.. code-block:: none

  Extension error:
  Could not import extension my_directive (exception: No module named 'my_directive')
  Makefile:60: recipe for target 'html' failed
  make: *** [html] Error 1

You have ``my_directive`` in conf.py in the list ``extensions``, but Sphinx
cannot find it. Have you moved the file to the right directory? Sphinx can
only find custom directives from directories which are declared in conf.py
with ``sys.path.append``. For example, if you need to place your directive
into directory **extensions/mydir**, put the following into conf.py:

.. code-block:: python

  sys.path.append(os.path.abspath('extensions/mydir'))
