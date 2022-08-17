Git: version control and collaboration
======================================

.. styled-topic::

  Main questions:
      How to store editing history? How to share your work with your
      colleagues?

  Topics:
      git: add, commit, push, pull

  What you are supposed to do?
      Learn the essential use of git version control

  Difficulty:
      You need basic UNIX terminal skills

  Laboriousness:
      1-2 hours

Introduction to Git
-------------------

.. admonition:: Software: Git
  :class: meta

  Git is a *version control software*. It saves the editing history of a
  directory: what new files were added, changes to existing files or what
  files have been moved. With Git, many persons can edit the same collection
  of files at the same time and share their work.

At Aalto University, Git is used for controlling the version history of the
A+ course materials and publishing changes to the A+ production server https://plus.cs.aalto.fi .
Git is also useful on your own computer: if you delete some file in your
course folder by mistake, or break the code and don't know how to repair
it, you can revert back to an earlier version of your codebase.

There are many Git tutorials for beginners.
You can try out `this <https://www.atlassian.com/git/tutorials/what-is-version-control>`_
if you want or just read the instructions here.

First-time Git setup
....................

If you haven't used Git before, do a first-time Git setup:

- Installation

  - To check whether or not you have Git installed, simply open a terminal window and run the following command.

    .. code-block:: none

      git --version

  - If you need to install Git, you can find the instructions `here <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_.

- Your Identity

  - The first thing you should do after installing Git is to set your user name and email address.
  - This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating.

    .. code-block:: none

      git config --global user.name "John Doe"
      git config --global user.email johndoe@example.com

  - You need to do this only once if you pass the ``--global`` option, because then Git will always use that information for anything you do on that system.
  - If you want to override this with a different name or email address for specific projects, you can run the command without the ``--global`` option when you’re in that project.

- Your Editor

  - Now that your identity is set up, you can configure the default text editor that will be used when Git needs you to type in a message.
  - If not configured, Git uses your system’s default editor.

    .. code-block:: none

      git config --global core.editor atom # set Atom as the default text editor

  - On a Windows system, if you want to use a different text editor, you must specify the full path to its executable file.

More instructions for setting up Git are available on the `official Git website <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>`_.

Important Git commands
......................

Now, let's go over the most needed git commands:

- ``git clone``

  - Initializes Git, adds new remote and clones some existing project from Gitlab to your computer.
  - This is how you get some project from Gitlab and start working on it.
  - When cloning a project, by default the master branch will be cloned, if not specified otherwise.

    .. code-block:: none

      git clone {url-of-the-project}
      git clone -b {some-specific-branch} {url-of-the-project} # clone from specific branch
      git clone {url-of-the-project} {folder-in-which-to-clone} # clone in specific folder

- ``git status``

  - Used to check the status of the working tree.
  - Shows the state of your working directory and helps you see all the files which are untracked by Git, staged or unstaged.
  - Use this before ``git add``, ``git commit`` and ``git push`` to make sure that you are making the correct changes.

    .. code-block:: none

      git status

- ``git add``

  - Adds a change in your working directory to the staging area.
  - Basically tells Git that we want to include these changes to some file in the next commit.
  - Use this when you have made some changes in your working directory (your project), and want to include these changes in the next commit.

    .. code-block:: none

      git add {files-to-add}
      git add -A # add all changes

- ``git commit``

  - Records every change that you've made in your working directory (and added with ``git add``) as an object in your local repository.
  - The changes are saved in your local repository, not on Gitlab.
  - Use this when you've made some progress in your project, and want to save it in this exact state.

    .. code-block:: none

      git commit # opens some editor so you can write your commit message
      git commit -m "some message" # commit message is written inline

- ``git push``

  - Push (copy) all your local repository changes to Gitlab (after ``git commit``).
  - After pushing, you can see all your work on the remote repository (Gitlab).

    .. code-block:: none

      git push -u {remote-name} {branch-name} # push to Gitlab, and set the branch as upstream so that next time you won't have to specify the branch on which to push
      git push {remote-name} # if you have already set an upstream branch
      git push # push to current branch's remote (or origin, if no remote is configured for the current branch)

- ``git pull``

  - Pull (copy) the changes from a remote repository branch and merge all the changes locally into the current branch.
  - Same as doing ``git fetch`` and ``git merge``.
  - Use this when you want to update your local repository with changes from a remote repository.

    .. code-block:: none

      git pull {remote-name} {branch-name}
      git pull # pull from current branch's remote (or origin, if no remote is configured for the current branch)

- ``git mv``

  - Moves/renames the file/folder, updating the index to record the replaced file path, as well as updating any affected git submodules.
  - Unlike a manual move, this also detects case-only renames that would not otherwise be detected as a change by git.

    .. code-block:: none

      git mv {old-name} {new-name}

- ``git branch``

  - Show all your local branches, create new branches or delete branches.

    .. code-block:: none

      git branch # show all local branches
      git branch {branch-name} # create a new branch (it won't switch you to the new branch)
      git branch -d {branch-name} # delete a branch that's already merged
      git branch -D {branch-name} # force delete a branch even if it's not merged yet
      git push {remote-name} --delete {branch-name} # delete a remote branch (a branch that's on Gitlab)

- ``git checkout``

  - This command has many uses, which are listed below.

    .. code-block:: none

      git checkout {branch-name} # switch to some branch
      git checkout -b {branch-name} # create a new branch and switch to it
      git checkout {commit-hash} # go back to some commit so you can inspect the files at that point in time
      git checkout {commit-hash} {file-name} # get another version of some file and put it in place of the current file
      git checkout {file-name} # get the latest version of some file from the remote repository

.. admonition:: Recommendation: "git lol" custom command
  :class: meta

  One can configure additional commands for git. Copy and paste the following
  command to the terminal to add the new command "git lol". It shows a nice,
  semi-graphical tree view of your git history, as in the picture below.

.. code-block:: none

    git config --global --add alias.lol "log --graph --decorate --pretty=oneline --abbrev-commit --all"

.. image:: /images/git-lol.png
  :align: center


Aalto Gitlab
------------

Aalto University has a service for storing and sharing git repositories
(directories with history in git). In the following, you will be guided
on how to use it.

First, log in to Aalto Gitlab at https://version.aalto.fi .

Adding an SSH key
.................

If you have not used Aalto Gitlab before, you need to add an *SSH key*.
This is a cryptographic key which enables the data exchange between your
computer and the Aalto Gitlab computer safely. It is required for making
the commands ``git pull`` and ``git push`` work.

Click on your profile picture circle on the top-right corner of the
page and choose "settings". Next, on the left sidebar, click on the  "SSH option".
Then, click on the link "generate one" and follow the instructions.

.. figure:: /images/gifs/gitlab-ssh.gif
  :align: center
  :width: 90%

Course group
............

The course repository in `version.aalto.fi <https://version.aalto.fi>`_ must have the user "apluslms" as a member with the "Reporter" role (read access).
Otherwise, the servers are not able to download the course git repository.
Courses in the `course group <https://version.aalto.fi/gitlab/course>`_ owned by EDIT (A+ team) already have this set up automatically.

* If the course repository in `version.aalto.fi <https://version.aalto.fi>`_ is not under our course group, then add the user "apluslms" with the "Reporter" role and Markku Riekkinen and Jimmy Ihalainen as members with the "Maintainer" role so that we can change the project settings when necessary.
* Note: `version.aalto.fi <https://version.aalto.fi>`_ may have a user "aplus", but that is the wrong one. The correct one is "apluslms".
* Adding members to the project in `version.aalto.fi <https://version.aalto.fi>`_: open your course project, then in the left-side menu, open Project information -> Members.
* We strongly suggest to transfer your repository to the Aplus course group in `version.aalto.fi <https://version.aalto.fi>`_. If you are interested, please ask us about the course group by emailing aplusguru@cs.aalto.fi.

Transfer an existing course git repository to the course group
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Contact aplusguru@cs.aalto.fi
2. A+ support will add you as an owner to the course-transfer group (https://version.aalto.fi/gitlab/course-transfer).
3. You can then transfer your course git repository to the course-transfer group (namespace in GitLab). The transfer is done in the project page in `version.aalto.fi <https://version.aalto.fi>`_. Go to Settings -> General -> expand the Advanced section -> Transfer project.
4. A+ support transfers the repository from the course-transfer group to the course group.
5. Anyone who has cloned the git repository to their computer needs to update the remote URL in the local repository. In the terminal, go to the repository directory and update the URL with the command ``git remote set-url origin NEW_URL`` (the remote name "origin" is the default name but you may have used a different name). You can check your git remotes and URLs with the command ``git remote -v``.

Recommendations for git workflow
................................

If you know that several persons are editing the same course as you, begin
your working day with ``git pull``. Make many of small commits: edit a
couple of files where the changes are related to each other, like adding
a new chapter, picture or exercise. Do ``git push`` many times a day. This
way it is easy to record what files were changed in each editing step.
Essentially, ``git push`` backs up your work to Aalto Gitlab
so if your laptop or workstation breaks or is stolen, you will only
lose a work of a few hours.
