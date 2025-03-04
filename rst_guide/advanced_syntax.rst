Advanced Syntax
===============

:Author: Aplus Team
:Last-modified: 11.11.2021

.. styled-topic::

  Main questions:
    What are some of the most complex directives used in A+?

  Topics:
    In this section, we will talk about:

    * `Introduction`_
    * `Structural elements`_
    * `Body elements`_
    * `Inline elements`_

  Requirements:
    #. You only need basic computing and programming skills, prior knowledge about markup languages
       might be beneficial.
    #. A basic environment set-up, as detailed in :doc:`Module 2 </set_up_environment/first_steps>`.
    #. Prior understanding about *RST*, as detailed in :doc:`Chapter 3.1 </rst_guide/get_started>`.

  Estimated reading time:
    60 min.

::::

Introduction
------------

In this chapter, we will cover some of the most advanced *RST* directives such as csv tables,
definition lists, toctrees, code-blocks, downloads, cross-references among others. The use of
advanced syntax will allow you to navigate through different chapters, create responsive designs,
share blocks of code with highlighted syntax, and add downloadable files.

Structural elements
--------------------

Toctree
.......

Toctree stands for "Table of Content Tree", and it is perhaps one of the most important directives
for creating navigable content. This directive allows to organise and include the files that are
going to be part of the course.
Therefore, the files that are not included in any toctree directive will not be  rendered and therefore, will not be visible in the web site.

The toctree directive can point to other toctree directives and thus create the tree structure of the files.
Typically, each course has an ``index.rst`` file with the toctree directive which points to each module's ``index.rst`` file.
Subsequently, each module ``index.rst`` file points to the chapters of the module.
This grouping allows to have a tree structure in the course content and organize the course more logically.
:ref:`The image below <toctree-visualization>` shows the directory structure of the Aplus manual and
the way it is rendered in the web browser.
The ``index.rst`` file located in the line 2 contains the ``toctree`` with all the modules of the course,
while the ``index.rst`` files presented in lines 5, 12, 18, 21 and 24 contain the ``index.rst`` files
with the ``toctree`` directives that point to each chapter inside the module.

.. div:: row contrast-tree
  :name: toctree-visualization

  .. div:: col-12 col-md-6

    .. code-block:: bash
      :linenos:
      :caption: Folder structure section of the Aplus manual.
      :emphasize-lines: 2,5,12,18,21,24

      aplus-manual
      ├── index.rst
      ├── overview
      │   ├── gallery.rst
      ├── ├── index.rst
      ├── set_up_environment
      │   ├── first_steps.rst
      │   ├── git.rst
      │   ├── docker.rst
      │   ├── vs_code.rst
      │   ├── additional_resources.rst
      │   └── index.rst
      ├── rst_guide
      │   ├── get_started.rst
      │   ├── basic_syntax.rst
      │   ├── extended_syntax.rst
      |   ├── additional_resources_and_cheatsheet.rst
      │   └── index.rst
      ├── style_aplus
      │   ├── css.rst
      │   └── index.rst
      ├── questionnaires
      │   ├── questionnaires.rst
      │   └── index.rst
      |
      ...

  .. div:: col-12 col-md-6

    .. figure:: /images/gallery/table_of_content.png
      :scale: 40%
      :align: right
      :class: img-responsive img-thumbnail


.. warning::

    * Only the *RST* files included inside a toctree directive are included in the course structure.
    * The toctree directive refers to the files by name, but such names should **not** include the file extension, i.e. ``.rst``.
    * You should use relative document names (not beginning with a slash). The toctree should be relative to the files. You can review our documentation about the `structure of the course <https://plus.cs.aalto.fi/aplus-manual>`_.

Toctree :important:`syntax` consists of the ``toctree`` directive, optional directive options and the list of files that will be included in the tables of content.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''

.. rst-tabs::

  .. tab-content:: tab1-toctree
    :title: input: RST

    .. code-block:: rst
      :caption: The following example is the index.rst file used in this module.

      .. toctree::
        :maxdepth: 2

          get_started
          basic_syntax
          advanced_syntax
          additional_resources_and_cheatsheet

  .. tab-content:: tab2-toctree
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<div><h3><a href="/def/current/rst_guide/">3. RST Guide</a></h3>`
      :raw-html:`<h4><small>Tue, Apr 21 2020, noon – Sat, May 1 2021, noon</small></h4>`
      :raw-html:`<ul class="toc">`
      :raw-html:`<li><a href="/def/current/rst_guide/get_started/" ">3.1 Get Started</a></li>`
      :raw-html:`<li><a href="/def/current/rst_guide/basic_syntax/">3.2 Basic Syntax</a></li>`
      :raw-html:`<li><a href="/def/current/rst_guide/advanced_syntax/">3.3 Advanced Syntax</a></li>`
      :raw-html:`<li><a href="/def/current/rst_guide/additional_resources_and_cheatsheet/">3.4 Additional resources and cheat sheet</a></li>`
      :raw-html:`</ul></div>`

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_.

|

Container
.........

The container represents an HTML ``div`` with the container class in it. It can be used to group certain body elements. It can also be used to add some styles to your course.

.. warning::

    * The container element is quite flexible and you can use it as you wish. However, you should follow some of the CSS guidelines about container classes.

Images and figures :important:`syntax` consist of the directive name, the image URI, and some directive options.

Code example
''''''''''''

.. rst-tabs::

  .. tab-content:: tab1-container
    :title: input: RST

    .. code-block:: rst

      .. container:: admonition success 

        .. div:: row

          .. div:: col-sm-12 col-md-6 border

            This is div inside a container. This div occupied half of the container in medium to extra large screens and the whole container in small to extra small screens.

          .. div:: col-sm-12 col-md-6 border

            This is a second div inside the same container. This div occupied half of the container in medium to extra large screens and the whole container in small to extra small screens.


  .. tab-content:: tab2-container
    :title: rendered: HTML

    .. div:: html-box

      .. container:: admonition success

        .. div:: row

          .. div:: col-sm-12 col-md-6 border

            This is div inside a container. This div occupied half of the container in medium to extra large screens and the whole container in small to extra small screens.

          .. div:: col-sm-12 col-md-6 border

            This is a second div inside the same container. This div occupied half of the container in medium to extra large screens and the whole container in small to extra small screens.

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `containers <https://docutils.sourceforge.io/docs/ref/rst/directives.html#container>`_.

|

Body elements
-------------
Images
......
In order to include images in *RST*, it is possible to make use of two *RST* directives, ``figure`` and ``image``.
Both of them have similar options.
However, the figure directive has a couple more options than the image directive.

Images are a great tool to illustrate some step by step procedures.
In addition, you can make use of animated images to make your content even more dynamic:
`animated gifs <https://gifs-as-documentation.readthedocs.io/en/latest/>`_.
Note, that the example below makes use of the ``div`` directive to group the images in the same line.
You can always make use of the Bootstrap classes to organize images and any other components in your course.

.. warning::

    * You can use relative or absolute paths to your images.

The :important:`syntax` of images and figures consists of the directive name, the image URI, and some directive options.
Read the official documentation for adjusting the image size and the aligment.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-images
    :title: input: RST

    .. code-block:: rst

      .. div:: row

        .. div:: col-12 col-md-6

          .. image:: /images/fireworks.jpg
            :alt: This is a sample image.
            :width: 380px
            :align: center
            :class: img-fluid rounded-circle

          This is not a caption, this is only a paragraph below the image.

        .. div:: col-12 col-md-6

          .. figure:: /images/fireworks.jpg
            :alt: This is a sample figure.
            :scale: 50%
            :align: center
            :class: img-fluid img-thumbnail

            **Image X.** This is the caption.

  .. tab-content:: tab2-images
    :title: rendered: HTML

    .. div:: html-box

      .. div:: row

        .. div:: col-12 col-md-6

          .. image:: /images/fireworks.jpg
            :alt: This is a sample image.
            :width: 380px
            :align: center
            :class: img-fluid rounded-circle

          This is not a caption, this is only a paragraph below the image.

        .. div:: col-12 col-md-6

          .. figure:: /images/fireworks.jpg
            :alt: This is a sample figure.
            :scale: 50%
            :align: center
            :class: img-fluid img-thumbnail

            **Image X.** This is the caption.

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_.

|

Lists
-----

Lists are a good tool for presenting information in a sequential order. In the previous chapter, we
presented some :ref:`basic-lists` that can be used for in *RST*. Nevertheless, *RST* provides more advanced list that allows to organize information in a more logical manner.

Field list
...........

The field list are good to resemble database records. This type of list can have different applications, but those applications are better covered in the official documentation.

Field list :important:`syntax` consist of the term surrounded by colons, a whitespace and the information related to that term.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-field-list
    :title: input: RST

    .. code-block:: rst

      :Date: May 08, 2020
      :Version: 1.0
      :Authors: - Author One
                - Author Two
      :Indentation: Since the field marker may be quite long, the second
        and subsequent lines of the field body do not have to line up
        with the first line, but they must be indented relative to the
        field name marker, and they must line up with each other.

  .. tab-content:: tab2-field-list
    :title: rendered: HTML

    .. div:: html-box

      :Date: May 08, 2020
      :Version: 1.0
      :Authors: - Author One
                - Author Two
      :Indentation: Since the field marker may be quite long, the second
        and subsequent lines of the field body do not have to line up
        with the first line, but they must be indented relative to the
        field name marker, and they must line up with each other.

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `field lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists>`_.

|

Option list
...........
The option list is widely used for explaining command-line options.
This list has already a set of built-in options for this type of list.
However, we will not cover those options here, but you can find the information in the official documentation.

Option list's :important:`syntax` consists of the option parameter, followed by the argument placeholder, and the description.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-option-list
    :title: input: RST

    .. code-block:: rst

      -a         Output all.
      -b         Output both (this description is
                quite long).
      -c arg     Output just arg.
      --long     Output all day long.

      -p         This option has two paragraphs in the description.
                This is the first.

  .. tab-content:: tab2-option-list
    :title: rendered: HTML

    .. div:: html-box

      -a         Output all.
      -b         Output both (this description is
                quite long).
      -c arg     Output just arg.
      --long     Output all day long.

      -p         This option has two paragraphs in the description.
                This is the first.

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `option lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists>`_.

|

Tables
-------
In the previous chapter, we saw how to create tables using markup. However, *RST* allows to create tables using some more advanced options and perhaps more user-friendly configurations.

List Table
..........
List tables allow to set the number of columns and the headers through the directive options.
This type of table reduces the amount of manual typing needed in the basic tables.

.. warning::

    * Each sublist must contain the same number of items. Otherwise, the table will not be rendered.
    * Cells cannot be combined.

List tables :important:`syntax` consist of the directive name, the table title, the table options, and the list of items, which are split by rows.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-list-table
    :title: input: RST

    .. code-block:: rst

      .. rst-class:: table table-success table-striped table-striped-columns table-hover

      .. list-table:: This is a List Title
        :widths: 25 25 50
        :header-rows: 1

        * - Heading row 1, column 1
          - Heading row 1, column 2
          - Heading row 1, column 3
        * - Row 1, column 1
          -
          - Row 1, column 3
        * - Row 2, column 1
          - Row 2, column 2
          - Row 2, column 3

  .. tab-content:: tab2-list-table
    :title: rendered: HTML

    .. div:: html-box

      .. rst-class:: table table-success table-striped table-striped-columns table-hover

      .. list-table:: This is a List Title
        :widths: 25 25 50
        :header-rows: 1

        * - Heading row 1, column 1
          - Heading row 1, column 2
          - Heading row 1, column 3
        * - Row 1, column 1
          -
          - Row 1, column 3
        * - Row 2, column 1
          - Row 2, column 2
          - Row 2, column 3

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `list tables <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`_.

|

A CSV table
...........

CSV tables are a convenient directive for importing CSV files and rendering them inside the course content.
Nevertheless, you could also use this directive by creating the table manually inside the *RST* document using *csv* notation (comma-separated values).

.. warning::

    * There is no support for checking that the number of columns in each row is the same.
    * Block markup and inline markup within the cell are supported.

CSV tables' :important:`syntax` consists of the directive name, the table title, some options and the content or file/URL.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-csv-table
    :title: input: RST

    .. code-block:: rst

      .. rst-class:: table table-secondary table-striped

        .. csv-table:: This is a CSV Table imported from a file.
          :file: ../course_material/file.csv
          :widths: 30, 70, 30
          :header-rows: 1

      .. rst-class:: table table-bordered table-hover table-striped-columns

        .. csv-table:: CSV table extracted from the people.sc.fsu.edu
          :header: "First Name", "Last Name", "Street", "County", "State", "Postal Code"
          :widths: 25, 25, 15, 15, 10, 10

          John,Doe,120 Jefferson st.,Riverside, NJ, 08075
          Jack,McGinnis,220 hobo Av.,Phila, PA,09119
          "John ""Da Man""",Repici,120 Jefferson St.,Riverside, NJ,08075
          Stephen,Tyler,"7452 Terrace ""At the Plaza"" road",SomeTown,SD, 91234
          Anne, Blankman,,SomeTown, SD, 00298
          "Joan ""the bone""",Jet,"9th, at Terrace plc",Desert City,CO,00123

  .. tab-content:: tab2-csv-table
    :title: rendered: HTML

    .. div:: html-box

      .. rst-class:: table table-secondary table-striped

        .. csv-table:: This is a CSV Table imported from a file.
          :file: ../course_material/file.csv
          :widths: 30, 70, 30
          :header-rows: 1

      .. rst-class:: table table-bordered table-hover table-striped-columns

        .. csv-table:: CSV table extracted from the people.sc.fsu.edu
          :header: "First Name", "Last Name", "Street", "County", "State", "Postal Code"
          :widths: 25, 25, 15, 15, 10, 10

          John,Doe,120 Jefferson st.,Riverside, NJ, 08075
          Jack,McGinnis,220 hobo Av.,Phila, PA,09119
          "John ""Da Man""",Repici,120 Jefferson St.,Riverside, NJ,08075
          Stephen,Tyler,"7452 Terrace ""At the Plaza"" road",SomeTown,SD, 91234
          Anne, Blankman,,SomeTown, SD, 00298
          "Joan ""the bone""",Jet,"9th, at Terrace plc",Desert City,CO,00123

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `CSV tables <https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table>`_.

|

Block code
..........

This is another directive provided by Sphinx.
This snippet of code use the `Pygments <https://pygments.org/>`_ to highlight the specified language.
Nevertheless, there is a limited number of `supported languages <https://pygments.org/languages/>`_.
The example below shows a snippet of code that is rendered through the ``code-block`` directive.
In this example, we can see that we have numbered the code lines and also highlighted the lines 14, 18 and 22.
All of this is possible thanks to the built-in options of the ``code-block`` directive.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''

.. code-block:: python
  :linenos:
  :emphasize-lines: 14,18,22

  ethernet_devices = [1, [7], [2], [8374163], [84302738]]
  usb_devices = [1, [7], [1], [2314567], [0]]

  # The long way
  all_devices = [
      ethernet_devices[0] + usb_devices[0],
      ethernet_devices[1] + usb_devices[1],
      ethernet_devices[2] + usb_devices[2],
      ethernet_devices[3] + usb_devices[3],
      ethernet_devices[4] + usb_devices[4]
  ]

  # Some comprehension magic
  all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]

  # Let's use maps
  import operator
  all_devices = list(map(operator.add, ethernet_devices, usb_devices))

  # We can't forget our favorite computation library
  import numpy as np
  all_devices = np.add(ethernet_devices, usb_devices)

.. rst-tabs::

  .. tab-content:: tab1-block-code
    :title: input: RST

    .. code-block:: rst

      .. code-block:: python
        :linenos:
        :emphasize-lines: 14,18,22

        ethernet_devices = [1, [7], [2], [8374163], [84302738]]
        usb_devices = [1, [7], [1], [2314567], [0]]

        # The long way
        all_devices = [
            ethernet_devices[0] + usb_devices[0],
            ethernet_devices[1] + usb_devices[1],
            ethernet_devices[2] + usb_devices[2],
            ethernet_devices[3] + usb_devices[3],
            ethernet_devices[4] + usb_devices[4]
        ]

        # Some comprehension magic
        all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]

        # Let's use maps
        import operator
        all_devices = list(map(operator.add, ethernet_devices, usb_devices))

        # We can't forget our favorite computation library
        import numpy as np
        all_devices = np.add(ethernet_devices, usb_devices)

  .. tab-content:: tab2-block-code
    :title: rendered: HTML

    .. div:: html-box

      .. code-block:: python
        :linenos:
        :emphasize-lines: 14,18,22

        ethernet_devices = [1, [7], [2], [8374163], [84302738]]
        usb_devices = [1, [7], [1], [2314567], [0]]

        # The long way
        all_devices = [
            ethernet_devices[0] + usb_devices[0],
            ethernet_devices[1] + usb_devices[1],
            ethernet_devices[2] + usb_devices[2],
            ethernet_devices[3] + usb_devices[3],
            ethernet_devices[4] + usb_devices[4]
        ]

        # Some comprehension magic
        all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]

        # Let's use maps
        import operator
        all_devices = list(map(operator.add, ethernet_devices, usb_devices))

        # We can't forget our favorite computation library
        import numpy as np
        all_devices = np.add(ethernet_devices, usb_devices)

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `code block <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`_.

|

Literal include
...............

The ``literalinclude`` directive allows you to include code files and show then as snippets of code within the course content.
This is ideal for showing code examples stored in external files.
In addition, this directive allows to emulate file comparison.

.. warning::

  * The path of the file is relative to the path of the chapter file. However, you can also use absolute paths.
  * This supports many of the code-block options such as lineos and emphasize-lines.
  * You may include only some selected lines of the file.
  * This can be used to compare two different files.

The literalinclude :important:`syntax` consists of the directive name, the filepath and the code-block options.

.. literalinclude:: /course_material/python_examples/example.py
  :caption: Python diff example
  :language: python
  :linenos:
  :diff: /course_material/python_examples/example.py.orig

.. literalinclude:: /course_material/python_examples/example.py
  :caption: Python example
  :language: python
  :prepend: # Prepended comment
  :append: # Appended comment
  :linenos:
  :lines: 1-5,7-9


:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-include
    :title: input: RST

    .. code-block:: rst

      .. literalinclude:: /course_material/python_examples/example.py
        :caption: Python diff example
        :language: python
        :linenos:
        :diff: /course_material/python_examples/example.py.orig

      .. literalinclude:: /course_material/python_examples/example.py
        :caption: Python example
        :language: python
        :prepend: # Prepended comment
        :append: # Appended comment
        :linenos:
        :lines: 1-5,7-11


  .. tab-content:: tab2-include
    :title: rendered: HTML

    .. div:: html-box

      .. literalinclude:: /course_material/python_examples/example.py
        :caption: Python diff example
        :language: python
        :linenos:
        :diff: /course_material/python_examples/example.py.orig

      .. literalinclude:: /course_material/python_examples/example.py
        :caption: Python example
        :language: python
        :prepend: # Prepended comment
        :append: # Appended comment
        :linenos:
        :lines: 1-5,7-11

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `literal include <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`_.

|

Inline elements
---------------
.. _cross-reference:

Cross-reference
...............

Hyperlinks can be used to link external websites or to link to different part of the course.
However, for linking to different sections or chapters of the course, we use the ``:ref:`` and the ``:doc:`` roles.
These two roles create a link to the determined target indicated by the role.
However, in order to make these cross-references work, we should create or have specific targets.

In the case of the ``:ref:`` role, we define the target as ``.. _target-name:``.
This syntax adds an id to the element that is immediately followed by and creates the target for the link.

.. warning::

  * You may add targets above titles.
  * The `name property <https://docutils.sourceforge.io/docs/ref/rst/directives.html#name>`_ adds an id to the respective element and can be used as a target.
  * All the headings/titles create target links automatically,
    therefore you should try to avoid having the same title twice throughout the whole course since it can cause conflicts.
    If this is the case, you can override the target with an explicit target on top of the title.

In the case of the ``:doc:`` role, the targets are the documents themselves.
Therefore, the link to those documents should be an absolute or relative path.

Cross-referencing :important:`syntax` consists of the ``:ref:`` or ``:doc:`` roles, with the target as the interpreted text of the roles.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''

.. rst-tabs::

  .. tab-content:: tab1-cross-reference
    :title: input: RST

    .. code-block:: rst

      .. _examples:

      Examples
      --------

      This is the text of the section.

      It refers to the section itself, see :ref:`examples`.

      In addition, see the chapter :doc:`questionnaires </questionnaires/questionnaires>`.

  .. tab-content:: tab2-cross-reference
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<span id="id1"></span>`
      :raw-html:`<h2>Examples</h2>`
      :raw-html:`<p>This is the text of the section.</p>`
      :raw-html:`<p>It refers to the section itself, see <a href="#id1" class="reference internal">Examples</a>.</p>`
      :raw-html:`<p>In addition, see the chapter <a data-aplus-chapter="yes" href="../../questionnaires/questionnaires" class="reference internal">questionnaires</a>.</p>`

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about** `cross-referencing <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role>`_.

|

Substitution reference
......................

Substitution references allow you to define some value once and
use it in multiple locations without copy-pasting the same value manually everywhere.
The substition could, for example, contain some often repeated phrase.

You could compare substitutions to constant variables in programming.
You define the constant once and then you use it anywhere.
If you change the value of the constant, it automatically affects all the locations where the constant has been used.

The substitution reference can be used in pair with hyperlinks by appending an underscore to the end.
The substitution element can also be used to replace images.


.. warning::

    * In order to use a substitution reference, you need a sustitution definition.
    * Substitution references are case-sensitive.

Substitution reference's :important:`syntax` consists of the reference text surrounded by vertical bars.
In case of implementing links, the underscore should be added at the end.
On the other hand, the :important:`syntax` for the substitution definition consists of two consecutive dots followed by a whitespace,
the reference name wrapped in vertical bars, followed by some directive type and the data.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-subs-reference
    :title: input: RST

    .. code-block:: rst

      .. |RST| replace:: reStructuredText
      .. _RST: http://docutils.sourceforge.net/rst.html

      |RST|_ is the best

  .. tab-content:: tab2-subs-reference
    :title: rendered: HTML

    .. div:: html-box

      .. |RST| replace:: reStructuredText
      .. _RST: http://docutils.sourceforge.net/rst.html

      |RST|_ is the best

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `substitution references <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-references>`_.

|

Download
........

This role allows you to attach downloadable files to your course.
You can use this directive to provide the students with extra material such as PDF files and code templates.

The following :download:`file </course_material/example_file.txt>` can be downloaded.

Code example
''''''''''''

.. rst-tabs::

  .. tab-content:: tab1-download
    :title: input: RST

    .. code-block:: rst

      The following :download:`file </course_material/example_file.txt>` can be downloaded.

  .. tab-content:: tab2-download
    :title: rendered: HTML

    .. div:: html-box

      The following :download:`file </course_material/example_file.txt>` can be downloaded.

.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `download <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-download>`_.

|

Dictionary/Glossary
...................

The ``glossary`` directive is useful for defining terms that are used throughout the course.
Having a glossary may help the students get familiar with the terminology used in the course.
We recommend to have an independent chapter at the end of your course with the ``glossary`` directive.

You use the ``term`` role to link terms in the text content to the glossary with the definition of the term.
You use the ``glossary`` directive in some chapter in order to define all the terms.


:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''

This chapter has included many features of :term:`Sphinx`.
Have you tried the :term:`Sublime Text` editor yet?

.. glossary::

  Sphinx
    Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.
    It was originally created for the Python documentation, and
    it has excellent facilities for the documentation of software projects in a range of languages.

  Sublime Text
    Sublime Text is a sophisticated text editor for code, markup and prose.
    You'll love the slick user interface, extraordinary features and amazing performance.

.. code-block:: rst

  This chapter has included many features of :term:`Sphinx`.
  Have you tried the :term:`Sublime Text` editor yet?

  .. glossary::

    Sphinx
      Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.
      It was originally created for the Python documentation, and
      it has excellent facilities for the documentation of software projects in a range of languages.

    Sublime Text
      Sublime Text is a sophisticated text editor for code, markup and prose.
      You'll love the slick user interface, extraordinary features and amazing performance.


.. rst-class:: text-end

| :glyphicon-info-sign:`\ ` **Read more about**  `term <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-term>`_ and `glossary <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-glossary>`_.

|


::::

Good practices for using links
------------------------------

1. In order to improve the readability of your RST markup,
   you should create a list of links in the bottom of the page and refer to those links using substitution names.


Example
.......

Link to the `Aplus manual`_ git repo.

|sphinx|_ is the best.

You can use this |geolink|_.

.. _Aplus manual: https://github.com/apluslms/aplus-manual

.. |geolink| replace:: Geo Link
.. _geolink: http://geoiptool.com

.. |sphinx| replace:: Sphinx
.. _sphinx: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Internal
........

We can use internal links, like `Good practices for using links`_, referring to a section.
However, since the link text uses the heading text verbatim,
it breaks when the heading is changed later.
It might be better to use your own labels above the headings and refer to the labels.
Example :ref:`link to the cross-reference section <cross-reference>`.

.. warning:: Remember that changing the title of your chapters and headings can break your references.


.. hint:: It is always a good idea to place the targets to these links above a heading.
.. The titles do not need a reference

It is also important to notice than in case the targets consist of more than one word,
it is necessary to surround the word with backticks ```<any word>```.

.. warning::

  Be careful using your links. Design the flow of your webpage and create a template for your links.
  It will help you to avoid breaking your links once they are defined.
