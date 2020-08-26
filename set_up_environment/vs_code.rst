Set up Visual Studio Code
=========================

.. styled-topic::

  Main questions:
    How do I set up VS Code to start creating a new course in A+?

  Topics:
    In this section, we will present the following topics:

    * `VS Code`_
    * `Install the recommended VS Code extensions`_

  Material:
    In this chapter, we do not provide additional material.

  Requirements:
    You need basic computational skills to install software in the Linux OS.

  Estimated working time:
    From 30 min to 1 hour.


VS Code
-------

As mentioned in previous chapters of this manual, VS Code is an advanced IDE that provide you with a set of tools
designed to improve the experience of creating, editing, and compiling source code. In this particular case, the source
code is written in RST, and the compiled output are HTML, YAML and static files. Along with the built-in tools
included in VS Code there are additional extensions designed to facilitate the experience of writing RST. The A+ team
developed an extension designed to improve the experience of creating course content. The extension will be discussed in
more detail in upcoming sections of this chapter.

The first step to enjoy the benefits of creating course content with the help of VS Code is to install the application
in you computer. Installing VS Code is relatively straightforward. You only need to follow the instruction provided in
the `download <https://code.visualstudio.com/download>`_ section of the official website.


.. _vs-extensions:

Install the recommended VS Code extensions
------------------------------------------

The `Aplus Tools extension <https://marketplace.visualstudio.com/items?itemName=jaguarfi.aplus-tools>`_ created for VS
Code provides a set of functionalities that will reduce the time needed for creating course content. Some of the
most relevant features are listed below:

* Live preview functionality (Visualise the changes in real-time without having to compile the course manually).

  .. figure:: /images/gallery/live-preview.png
    :width: 80 %
    :align: center

    Live preview capability of the Aplus Tools extension.

* Linter (Expose syntax errors).

  .. figure:: /images/gallery/linter.png
    :width: 60 %
    :align: center

    Linter capability of the Aplus Tools extension.

* Syntax Highlighting (Highlight mostly markdown syntax).

  .. figure:: /images/gallery/syntax-highlighting.png
    :width: 60 %
    :align: center

    Syntax Highlighting capability of the Aplus Tools extension.

* `Snippets <https://marketplace.visualstudio.com/items?itemName=jaguarfi.aplus-tools#snippets>`_ (Insert complex
  directives by using key words).

  .. figure:: /images/gallery/snippets.png
    :width: 60 %
    :align: center

    Small list of snippets available in the Aplus Tools extension.

In order to install the **Aplus tools extension** you should visit the
`VS Code Marketplace <https://marketplace.visualstudio.com/items?itemName=jaguarfi.aplus-tools#getting-starteds>`_ and
follow the instructions presented in the getting started section. If you experience any problem during the
installation or setup of your extension please contact aplusguru@cs.aalto.fi

.. note::

  You can develop the course content without using VS Code. However, we recommend to set up the VS Code environment
  because this will help you to reduce the strain of writing RST code.