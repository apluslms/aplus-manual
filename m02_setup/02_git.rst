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

Introduction to git
-------------------

.. admonition:: Software: git
  :class: meta

  git is a *version control software*. It saves the editing history of a
  directory: what new files were added, changes to existing files or what
  files have been moved. With git, many persons can edit the same collection
  of files at the same time and share their work.

At Aalto University, git is used for controlling the version history of the
A+ course materials and publishing changes to the A+ production server https://plus.cs.aalto.fi .
Git is also useful on your own computer: if you delete some file in your
course folder by mistake, or break the code and don't know how to repair
it, you can revert back to an earlier version of your codebase.

There are many git tutorials for beginners. Try out these:

- https://www.atlassian.com/git/tutorials/what-is-version-control

If you haven't used git before, do a first-time git setup:

- https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

When you edit course material, the most needed git commands are:

- ``git add``, ``git mv``
- ``git commit``
- ``git status``
- ``git pull``, ``git push``

.. admonition:: Recommendation: "git lol" custom command
  :class: meta

  One can configure additional commands for git. Copypaste the following
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
page and choose "settings". Next, on the left sidebar, click :guilabel:`&SSH`  "SSH Keys" on the sidebar on the left.


.. figure:: /images/gifs/gitlab-ssh.gif
  :align: center
  :width: 90%

Click on the link "generate one" and follow the instructions.


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

