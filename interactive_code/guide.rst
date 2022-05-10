Guide to interactive code with thebe
====================================

.. styled-topic::

  Main questions:
      What is interactive code, why and how to use it.

  Topics?
      Interactive code.

  Difficulty:
      Easy

  Laboriousness:
      Around 5 minutes of reading

What is interactive code, and why you would use it
--------------------------------------------------
This feature provides a low-effort way for students to run instructive pieces of sample code. The students can also edit these, to see how they behave.

This is useful for when you want to accompany your explanations with code, and also for giving complete beginners an easy way to run code without installing anything themselves.

Currently only python, R and C/C++ are supported (see readme of `aplus-rst-tools <https://github.com/apluslms/a-plus-rst-tools>`_ for more information). You can look at the advanced section if you want to try enabling other languages.

An example of a code cell:

.. thebe-precell-button::
.. code-block:: python
   :class: thebe

   a = 1
   b = 2
   c = a + b
   print(c)

and a standalone launch button:

.. thebe-button:: 

Usage
-----
For the student
...............
The student presses a button to activate a kernel that runs the code. 

After that, code blocks become interactive. The code can be edited, and buttons "run" and "restart" appear. By pressing run, the output of the code appears below the code block. The output can include images, that will also be shown.

The edits the student does are not saved, and will be lost when the page is refreshed.

For the teacher
...............
After setting everything up (see next sections for details), the teacher has to do two things in their rst files. The first is to insert a button that activates the coede-blocks:
- The directive ``thebe-button`` for a standalone button
- The directive ``thebe-precell-button`` for a button integrated to a code cell. These can be placed just before every code cell so that the students can start running code from anywhere.
The second one is the class ``thebe``. Any code-block that has this class set will become interactive when the button is pressed.

Here is an example of how an interactive code block together with a button could be added to a course module

.. code-block:: rst

  .. thebe-precell-button:: Custom button text (defaults to "Activate")
  .. code-block:: python
    :class: thebe

    a = 1
    b = 2
    c = a + b
    print(c)

    Standalone launch button:
    .. thebe-button:: Custom buttom text (defaults to "Run code")

If you want the output to be calculated and shown as soon as the kernel has been requested and set up, you can add the ``thebe-init`` class (``:class: thebe, init-thebe``).

Installing dependencies
-----------------------
It is possible to set up the environment in which the interactive code runs. In the case of python, this is done by setting up a git repository with a requirements file. It is also possible to define your own modules in the repository, which can then be imported in interactive code segments. The repository is set with a configuration option, see the next section. For a minimal example, see `requirements <https://github.com/binder-examples/requirements>`_.

Configuration
-------------
To set up interactive code, you have to set up a few things in the ``conf.py`` file of your course

- Include the line ``'thebe'`` in the ``extensions`` list
- Include thebe configuration options by adding the following lines to ``conf.py``

.. code-block:: python

   # Thebe configuration
    thebe_config = {
      "binderUrl": "https://mybinder.org" # For testing; replace this with a binderhub server provided by your instution for production
      # "repository_url": ""
      # "repostiory_branch": ""
    }   


