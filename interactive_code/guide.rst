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

Currently only Python, R, C/C++ and Octave are supported (see readme of `aplus-rst-tools <https://github.com/apluslms/a-plus-rst-tools>`_ for more information). You can look at the advanced section if you want to try enabling other languages.

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

After setting everything up (see next sections for details), the teacher has to do two things in their rst files. The first is to insert a button that activates the code blocks:

- The directive ``thebe-button`` for a standalone button
- The directive ``thebe-precell-button`` for a button integrated to a code cell. These can be placed just before every code cell so that the students can start running code from anywhere.

The second one is the class ``thebe``. Any code-block that has this class set will become interactive when the button is pressed.

Here is an example of how an interactive code block together with a button could be added to a course module:

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

To set up interactive code, you have to set up a few things in the ``conf.py`` file of your course:

- Include the line ``'thebe'`` in the ``extensions`` list
- Include thebe configuration options by adding the following lines to ``conf.py``

.. code-block:: python

   # Thebe configuration
    thebe_config = {
      "binderUrl": "https://mybinder.org" # For testing only
      # "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
      # "repository_branch": "master",
      "selector": "div.highlight",
      "codemirror-config": {
          "theme": "eclipse",
          "electricChars": "true"
          "lineNumbers": "true",
          "indentWithTabs": "true",
          "indentUnit": 4,
      }
    }

Kernel and code cell configuration
...................................

``"binderUrl"``
    A url to a BinderHub server. ``mybinder.org`` should only be used for testing, and should be replaced by a binderhub server provided by your instution when running a course. (*For Aalto Users:* you can use the BinderHub server at ``https://csej4404-binderhub.aalto.fi``)
``"repository_url"``
    A valid `binderhub repository <https://mybinder.readthedocs.io/en/latest/examples/sample_repos.html>`_ to base the code environment on. Should be a public GitHub repostiory. Defaults to `Jupyter datascience image <https://github.com/binder-examples/jupyter-stacks-datascience>`_. (*For Aalto users:* if you want to this repository to be private, please contact ``aplusguru@cs.aalto.fi`` and ask for a ``version.aalto.fi`` gitlab repository in the group binderhub-code).
``"repository_branch"``
    The branch to use from the repository above. Defaults to ``master``.
``"selector"``
    Which ``rst`` code blocks should be converted to interactive code elements. Defaults to ``".thebe"``. Some examples

    - ``"selector": "div.highlight"`` all the code blocks in ``rst`` files starting or containing ``:thebe-kernel: <KERNEL-NAME-HERE>`` directive will be converted to interactive code blocks.
    - ``"selector": ".thebe"`` the code blocks containing ``:class: thebe`` option will be converted to interactive code blocks. This is the default option, and if it is desired to have all code blocks to be interactive code blocks ``"selector": "div.highlight"`` should be explicitly configured.

Editable code area behaviour configuration
..........................................

``"theme": "eclipse"``
    The editor code style theme. We support only two options for now:

    - ``"theme": "eclipse"`` (default). This theme is very similar to the default theme of Eclipse IDE, and has a light background, which makes it a natural choice for the default A+ style in general.
    - ``"theme": "abcdef"``. This is a colorful theme with a dark background.
``"electricChars": "true"``
    Whether the editor (interactive code block) should re-indent the current line when a character is typed. Change this configuration to ``"false"`` if you prefer the students to practice proper indentation. Default is ``"true"``.
``"lineNumbers": "true"``
    Whether line numbering is enabled. When enabled, the editor will have a left gutter area with line numbers. The default is ``"true"``, and should be explicitly set to ``"false"`` if you do not want to have line numbers.
``"indentWithTabs": "true"``
    Whether indentation with tabs is enabled. The default configuration is ``"true"``, and should be set to ``"false"`` if you prefer to use spaces for indentation. A tab has ``4`` characters width.
``"indentUnit": 4``
    How many spaces define an indented block. The default is ``4`` spaces, and should be explicitly configured to change the indentation experience.

In addition to the settings above, the matching braces are highlighted when one of (``}``, ``)`` or ``]``) is typed.
