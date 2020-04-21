Set up Visual Studio Code
=========================

.. styled-topic::

  Main questions:
    How do I set up VS Code to start creating a new course in A+?

  Topics:
    In this section, we talk about:

    * `VS Code`_
    * `Install python libraries`_
    * `Install VS Code extensions`_

  Material:
    In this chapter, you won't need extra material.

  Requirements:
    You need basic computational skills to install some software in the Linux OS.

  Estimated working time:
    From 30 min to 1 hour.


VS Code
-------

As has been mentioned before, VS Code is an advanced IDE that will allow you to write markup documents more efficiently than using simple text editors. VS Code has a massive set of tools and extensions that will help you to avoid some of the most common mistakes during the creation of your course content.

Installing VSCode is relatively straightforward. You only need to follow the instruction provided in the `VSCode <https://code.visualstudio.com/download>`_
official website.


Install python libraries
------------------------

At this point, you should have Python 3 already installed. However, if you do not have it installed, Download python, from the `python website <http://www.python.org/downloads>`_. 

Installing python and libraries is not always an easy task. Nevertheless, we will guide you to install the python libraries without pain. First of all, you should open a new Linux terminal. Afterwards, you need to install some python libraries by typing the following commands.

1. Install **Sphinx 1.6.7** 

.. code-block:: vim
  
  pip3 install Sphinx==1.6.7

2. Install **sphinx-autobuild 0.7.1.**

.. code-block:: vim

  pip3 install sphinx-autobuild==0.7.1

3. Install **rstcheck** as a Linter.

.. code-block:: vim

  pip3 install rstcheck

.. _vs-extensions:

Install VS Code extensions
--------------------------

The extensions in VS Code are a set of additional features that help the user accomplish his task  more efficiently and faster. To create a course in A+, you only need two extensions. The first one is `reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_ and the second one is `Aplus tools <https://httpstat.us/501>`_. These two extensions provide a set of functionalities that facilitate the creation of course content. Among these functionalities, you can find: 

* Quick preview functionality (Visualise the changes in real-time without compiling the whole project).
* Linter (Visualise syntax errors).
* Snippets (Insert complex directives by using key words).
* Creation of templates (create template files or folder structures).

In order to install the extensions, open the `VS Code interface <https://code.visualstudio.com/docs/getstarted/userinterface>`_, go to the activity bar located on the left, click the extension option. Once the activity bar opens, search for the extensions mentioned above. Finally, press the install button (click reload if needed).

.. image:: /images/gifs/install_extensions.gif
  :width:  90%
  :align: center
  :class: img-responsive
  
.. More information about this setup can be found in `docs.restructuredtext.net <https://docs.restructuredtext.net/articles/prerequisites.html>`_. 
.. However, the above three steps should be enough to start using VS Code for developing your course content.

Snippets
........

In order to increase your productivity, you might want to use the snippets provided in the `Aplus tools` extension. Below you can find the list of snippets available to create your course.


.. list-table:: Aplus rst snippets
  :widths: 25 25 50
  :header-rows: 1

  * - Keyword
    - Description
    - More information

  * - ``ap-st``
    - Styled topic
    - `rst-tools.github <https://google.com>`_
  
  * - ``ap-div``
    - Bootstrap div
    - `rst-tools.github <https://google.com>`_

  * - ``ap-link``
    - link
    - `rst documentation <https://google.com>`_

.. note::  You can develop the course content without using VS Code. However, we recommend to set up the VSCode environment because this will help you to develop your course content faster.







