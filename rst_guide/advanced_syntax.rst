Advanced Syntax
===============

:Author: Aplus Team
:Last-modified: |today|

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
going to be part of the course. Therefore, the files that are not included in any toctree directive will not be  rendered and therefore, will not be visible in the web browser.

The toctree directive can point to other toctree directives and thus create the tree structure of the files. Typically, each course has an ``index.rst`` file with the toctree directive which points to all the modules ``index.rst`` files. Subsequently, each module ``index.rst`` file point to the chapters of the course. This grouping allows to have a tree structure in the course content and organize the course more logically. :ref:`The image below <toctree-visualization>` shows the folder structure Aplus manual of the  manual and the way it is rendered in the web browser. The ``index.rst`` file located in the line 2 contains the ``toctree`` with all the modules of the course, while the ``index.rst`` files presented in lines 3, 9, 16 and 22 contain the ``index.rst`` files with the ``toctree`` that points each chapter inside such module.

.. div:: row contrast-tree
  :name: toctree-visualization

  .. div:: col-12 col-md-6

    .. code-block:: bash
      :linenos:
      :caption: Folder structure section of the Aplus manual.
      :emphasize-lines: 1,3,9,16,22

      aplus-manual
      ├── index.rst
      ├── overview
      │   ├── gallery.rst
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

    * Only the *RST* files included inside a toctree directive are render in the course menu.
    * The toctree directive refers to the files by name, but such names should not include the files extension, i.e. ``.rst``.
    * You should use relative document names (not beginning with a slash). The toctree should be relative to the files. You can review or documentation about the `structure of the course <https://plus.cs.aalto.fi/aplus-manual>`_.

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
          extended_syntax
          additional_resources_and_cheatsheet

  .. tab-content:: tab2-toctree
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<div><h3><a href="/def/current/rst_guide/">3. RST Guide</a></h3>`
      :raw-html:`<h4><small>Tue, Apr 21 2020, noon – Sat, May 1 2021, noon</small></h4>`
      :raw-html:`<ul class="toc">`
      :raw-html:`<li><a href="/def/current/rst_guide/get_started/" ">3.1 Get Started</a></li>`
      :raw-html:`<li><a href="/def/current/rst_guide/basic_syntax/">3.2 Basic Syntax</a></li>`
      :raw-html:`<li><a href="/def/current/rst_guide/extended_syntax/">3.3 Extended Syntax</a></li>`
      :raw-html:`<li><a href="/def/current/rst_guide/additional_resources_and_cheatsheet/">3.3 Extended Syntax</a></li>`
      :raw-html:`</ul></div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `transitions <https://www.sphinx-doc.org/en/1.6/markup/toctree.html?highlight=toctree#the-toc-tree>`_.

|

Container
---------
The container represents an HTML ``div`` with the container class in it. It can be used to group certain body elements. It can also be used to add some styles to your course.

.. warning::

    * The container element is quite flexible and you can use it as you wish. However, you should follow some of the CSS guidelines about container classes.

Images and figures :important:`syntax` consist of the directive name, the image URI, and some directive options.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-container
    :title: input: RST

    .. code-block:: rst

      .. container:: bg-success

        .. div:: row

          .. div:: col-sm-12 col-md-6 border

            This is div inside a container. This div occupied half of the container in medium to big screens and the whole container in small to extra small screens.

          .. div:: col-sm-12 col-md-6 border

            This is a second div inside the same container. This div occupied half of the container in medium to big screens and the whole container in small to extra small screens.


  .. tab-content:: tab2-container
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<div class="bg-success docutils container">`
      :raw-html:`<div class="row">`
      :raw-html:`<div class="col-sm-12 col-md-6">`
      :raw-html:`This is div inside a container. This div occupied half of the container in medium to big screens and the whole container in small to extra small screens.</div>`
      :raw-html:`<div class="col-sm-12 col-md-6">`
      :raw-html:`This is a second div inside the same container. This div occupied half of the container in medium to big screens and the whole container in small to extra small screens.</div>`
      :raw-html:`</div>`
      :raw-html:`</div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_.

|

Body elements
-------------
Images
......
In order to include images in *RST*, it is possible to make use of two *RST* directives figures and images. Both of them have similar options. However, the figure directive couple more options that the image directive.

Images are a great tool to illustrate some step by step procedures. In addition, you can make use of animated images to make your content even more dynamic. `Animated Gifs <https://gifs-as-documentation.readthedocs.io/en/latest/>`_. Note , that the example below make use of the ``div`` directive to group the images in the same line. You can always make use of the bootstrap classes to organize images and any other components in your course.

.. warning::

    * You can use relative or absolute paths to your images.

Images and figures :important:`syntax` consist of the directive name, the image URI, and some directive options. Read the official documentation for adjusting th image size and the aligment.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-images
    :title: input: RST

    .. code-block:: rst

      .. div:: row

        .. div:: col-12 col-md-6

          .. image:: /images/gallery/Linux.svg
            :alt: This is a sample image.
            :width: 380px
            :align: center
            :class: img-responsive img-circle

          This is not a caption, this is only a paragraph below the image.

        .. div:: col-12 col-md-6

          .. figure:: /images/gallery/Linux.svg
            :alt: This is a sample figure.
            :scale: 10%
            :align: center
            :class: img-responsive img-thumbnail

            **Image X.** This is the caption.

  .. tab-content:: tab2-images
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<div class="row">`
      :raw-html:`<div class="col-12 col-md-6">`
      :raw-html:`<a class="img-responsive img-circle reference internal image-reference" href="http://localhost:8080/static/default/_images/Linux.svg"><img alt="This is a sample image." class="img-responsive img-circle align-center" src="http://localhost:8080/static/default/_images/Linux.svg" style="width: 380px;"></a>`
      :raw-html:`<p>This is not a caption, this is only a paragraph below the image</p>`
      :raw-html:`</div>`
      :raw-html:`<div class="col-12 col-md-6">`
      :raw-html:`<div class="figure align-center" id="id8">`
      :raw-html:`<a class="img-responsive img-thumbnail reference internal image-reference" href="http://localhost:8080/static/default/_images/Linux.svg"><img alt="This is a sample figure." class="img-responsive img-thumbnail" src="http://localhost:8080/static/default/_images/Linux.svg" style="width: 326.40000000000003px; height: 244.8px;"></a>`
      :raw-html:`<p class="caption"><span class="caption-text"><strong>Image X.</strong> This is the caption.</span></p>`
      :raw-html:`</div>`
      :raw-html:`</div>`
      :raw-html:`</div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_.

|

Lists
-----

Lists are a good tool for presenting information in a sequential order. In the previous chapter, we
presented some :ref:`basic-lists` that can be used for in *RST*. Nevertheless, *RST* provides more advanced list that allows to organize information in a more logical manner.

Field list
...........

The field list are good to resemble database records. This type of list can have different applications, but those applications are better covered in the official documentation.

.. warning::

    *
    *

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

      :raw-html:`<table class="docutils field-list" frame="void" rules="none">`
      :raw-html:`<colgroup><col class="field-name"><col class="field-body">`
      :raw-html:`</colgroup><tbody valign="top">`
      :raw-html:`<tr class="field-odd field"><th class="field-name">Date:</th><td class="field-body"><p class="first">May 08, 2020</p></td></tr>`
      :raw-html:`<tr class="field-even field"><th class="field-name">Version:</th><td class="field-body"><p class="first">1.0</p></td></tr>`
      :raw-html:`<tr class="field-odd field"><th class="field-name">Authors:</th><td class="field-body"><ul class="first simple">`
      :raw-html:`<li>Author One</li>`
      :raw-html:`<li>Author Two</li>`
      :raw-html:`</ul>`
      :raw-html:`</td>`
      :raw-html:`</tr>`
      :raw-html:`<tr class="field-even field"><th class="field-name">Indentation:</th><td class="field-body"><p class="first last">Since the field marker may be quite long, the second and subsequent lines of the field body do not have to line up with the first line, but they must be indented relative to the field name marker, and they must line up with each other.</p>`
      :raw-html:`</td>`
      :raw-html:`</tr>`
      :raw-html:`</tbody>`
      :raw-html:`</table>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `field lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists>`_.

|

Option list
...........
The option list is widely used for explaining command-line options. This list has already a set of built-in options for this type of list. However, we will not covered thos options are not discussed here, but you can the information in the offcial documentation.

.. warning::

    *
    *

Option list :important:`syntax` consist of the option parameter, followed by the argument placeholder, the description.

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

      :raw-html:`<table class="docutils option-list" frame="void" rules="none">`
      :raw-html:`<colgroup><col class="option"><col class="description">`
      :raw-html:`</colgroup><tbody valign="top">`
      :raw-html:`<tr><td class="option-group"><kbd><span class="option">-a</span></kbd></td>`
      :raw-html:`<td>Output all.</td></tr>`
      :raw-html:`<tr><td class="option-group"><kbd><span class="option">-b</span></kbd></td>`
      :raw-html:`<td>Output both (this description is quite long).</td></tr>`
      :raw-html:`<tr><td class="option-group"><kbd><span class="option">-c <var>arg</var></span></kbd></td>`
      :raw-html:`<td>Output just arg.</td></tr>`
      :raw-html:`<tr><td class="option-group"><kbd><span class="option">--long</span></kbd></td>`
      :raw-html:`<td>Output all day long.</td></tr>`
      :raw-html:`<tr><td class="option-group"><kbd><span class="option">-p</span></kbd></td>`
      :raw-html:`<td>This option has two paragraphs in the description. This is the first.</td></tr>`
      :raw-html:`</tbody>`
      :raw-html:`</table>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `option lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists>`_.

|

Tables
-------
In the previous chapter, we saw how to create tables using markup. However, *RST* allows to create tables using some more advanced options and perhaps more user-friendly configurations.

List Table
..........
List tables allows to  the number of columns and the headers through the directive options. This type of tables reduce the need of manual typing needed in the  basic tables.

.. warning::

    * Each sublist must contain the same umber of items. Otherwise, the table will not be rendered.
    * Cells cannot be combined.

List tables :important:`syntax` consist of the directive name, the table title, the table options, and the list of items, which are split by rows.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-list-table
    :title: input: RST

    .. code-block:: rst

      .. rst-class:: table-striped table-bordered table-hover

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

      :raw-html:`<table class="colwidths-given table-striped table-bordered table-hover docutils" id="id33" border="1">`
      :raw-html:`<caption><span class="caption-text">This is a List Title</span><a class="headerlink" href="#id33" title="Permalink to this table">¶</a></caption>`
      :raw-html:`<colgroup><col width="25%"></colgroup>`
      :raw-html:`<colgroup><col width="25%"></colgroup>`
      :raw-html:`<colgroup><col width="50%"></colgroup>`
      :raw-html:`<thead valign="bottom">`
      :raw-html:`<tr class="row-odd"><th class="head">Heading row 1, column 1</th>`
      :raw-html:`<th class="head">Heading row 1, column 2</th>`
      :raw-html:`<th class="head">Heading row 1, column 3</th>`
      :raw-html:`</tr>`
      :raw-html:`</thead>`
      :raw-html:`<tbody valign="top">`
      :raw-html:`<tr class="row-even"><td>Row 1, column 1</td>`
      :raw-html:`<td>&nbsp;</td>`
      :raw-html:`<td>Row 1, column 3</td>`
      :raw-html:`</tr>`
      :raw-html:`<tr class="row-odd"><td>Row 2, column 1</td>`
      :raw-html:`<td>Row 2, column 2</td>`
      :raw-html:`<td>Row 2, column 3</td>`
      :raw-html:`</tr>`
      :raw-html:`</tbody>`
      :raw-html:`</table>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_.

|

A CSV table
...........

CSV tables are a convenient directive for importing csv files and render them inside the course content. Neverthless, you could also use this directive by creating the table manually inside the *RST* document using *csv* notation(comma-separated values).

.. warning::

    * There is no support for checking that the number of columns in each row is the same.
    * Block markup and inline markup within the cell are supported.

CSV tables :important:`syntax` consist of the directive name, the table title, some options and the content or file/url.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-csv-table
    :title: input: RST

    .. code-block:: rst

      .. csv-table:: This is a CSV Table imported from a file.
        :file: ../course_material/file.csv
        :widths: 30, 70, 30
        :header-rows: 1

      .. csv-table:: CSV table extracted from the people.sc.fsu.edu
        :header: "Firsr Name", "Last Name", "Street", "County", "State", "Postal Code"
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

      :raw-html:`<table class="colwidths-given docutils" id="id34" border="1">`
      :raw-html:`<caption><span class="caption-text">This is a CSV Table imported from a file.</span><a class="headerlink" href="#id34" title="Permalink to this table">¶</a></caption>`
      :raw-html:`<colgroup>`
      :raw-html:`<col width="23%">`
      :raw-html:`<col width="54%">`
      :raw-html:`<col width="23%">`
      :raw-html:`</colgroup>`
      :raw-html:`<thead valign="bottom">`
      :raw-html:`<tr class="row-odd"><th class="head">Header a</th>`
      :raw-html:`<th class="head">Header B</th>`
      :raw-html:`<th class="head">Header C</th>`
      :raw-html:`</tr>`
      :raw-html:`</thead>`
      :raw-html:`<tbody valign="top">`
      :raw-html:`<tr class="row-even"><td>Item 1a</td>`
      :raw-html:`<td>Item 1b</td>`
      :raw-html:`<td>None</td>`
      :raw-html:`</tr>`
      :raw-html:`<tr class="row-odd"><td>Item 1b</td>`
      :raw-html:`<td>Item 2b</td>`
      :raw-html:`<td>None</td>`
      :raw-html:`</tr>`
      :raw-html:`<tr class="row-even"><td>&nbsp;</td>`
      :raw-html:`<td>Item 2c</td>`
      :raw-html:`<td>None</td>`
      :raw-html:`</tr>`
      :raw-html:`</tbody>`
      :raw-html:`</table>`

      :raw-html:`<table class="colwidths-given docutils" id="id29" border="1"><caption><span class="caption-text">CSV table extracted from the people.sc.fsu.edu</span><a class="headerlink" href="#id29" title="Permalink to this table">¶</a></caption><colgroup><col width="25%"><col width="25%"><col width="15%"><col width="15%"><col width="10%"><col width="10%"></colgroup><thead valign="bottom"><tr class="row-odd"><th class="head">Firsr Name</th><th class="head">Last Name</th><th class="head">Street</th><th class="head">County</th><th class="head">State</th><th class="head">Postal Code</th></tr></thead><tbody valign="top"><tr class="row-even"><td>John</td><td>Doe</td><td>120 Jefferson st.</td><td>Riverside</td><td>NJ</td><td>08075</td></tr><tr class="row-odd"><td>Jack</td><td>McGinnis</td><td>220 hobo Av.</td><td>Phila</td><td>PA</td><td>09119</td></tr><tr class="row-even"><td>John “Da Man”</td><td>Repici</td><td>120 Jefferson St.</td><td>Riverside</td><td>NJ</td><td>08075</td></tr><tr class="row-odd"><td>Stephen</td><td>Tyler</td><td>7452 Terrace “At the Plaza” road</td><td>SomeTown</td><td>SD</td><td>91234</td></tr><tr class="row-even"><td>Anne</td><td>Blankman</td><td>&nbsp;</td><td>SomeTown</td><td>SD</td><td>00298</td></tr><tr class="row-odd"><td>Joan “the bone”</td><td>Jet</td><td>9th, at Terrace plc</td><td>Desert City</td><td>CO</td><td>00123</td></tr></tbody></table>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `CSV tables <https://docutils.sourceforge.io/docs/ref/rst/directives.html#id4>`_.

|

Block code
..........

This is another directive provided by Sphinx. This snippet of code use the `Pygments <https://pygments.org/>`_  to highlight the specified language. Nevertheless, there is a limited number of `supported languages <https://pygments.org/languages/>`_. The example below shows a snippet of code that is render through the ``code-block`` directive. In this example, we can see that we have numbered the code lines and also highlighted the lines 14, 18 and 22. All of this is possible thanks to the built-in options of the ``code-block`` directive.

.. warning::

    *
    *

Images and figures :important:`syntax` consists of the directive name, the image URI, and some directive options. Read the official documentation for adjusting the image size and the the aligment.

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

      :raw-html:`<div class="highlight-rst"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>`
      :raw-html:`1`
      :raw-html:`2`
      :raw-html:`3`
      :raw-html:`4`
      :raw-html:`5`
      :raw-html:`6`
      :raw-html:`7`
      :raw-html:`8`
      :raw-html:`9`
      :raw-html:`10`
      :raw-html:`11`
      :raw-html:`12`
      :raw-html:`13`
      :raw-html:`14`
      :raw-html:`15`
      :raw-html:`16`
      :raw-html:`17`
      :raw-html:`18`
      :raw-html:`19`
      :raw-html:`20`
      :raw-html:`21`
      :raw-html:`22`
      :raw-html:`</pre></div></td><td class="code"><div class="highlight"><pre><span></span>ethernet_devices = [1, [7], [2], [8374163], [84302738]]`
      :raw-html:`usb_devices = [1, [7], [1], [2314567], [0]]`
      :raw-html:`&nbsp;`
      :raw-html:`# The long way`
      :raw-html:`all_devices = [`
      :raw-html:`&nbsp;   ethernet_devices[0] + usb_devices[0],`
      :raw-html:`&nbsp;   ethernet_devices[1] + usb_devices[1],`
      :raw-html:`&nbsp;   ethernet_devices[2] + usb_devices[2],`
      :raw-html:`&nbsp;   ethernet_devices[3] + usb_devices[3],`
      :raw-html:`&nbsp;   ethernet_devices[4] + usb_devices[4]`
      :raw-html:`]`
      :raw-html:`&nbsp;`
      :raw-html:`# Some comprehension magic`
      :raw-html:`<span class="hll">all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]`
      :raw-html:`</span>`
      :raw-html:`# Let's use maps`
      :raw-html:`import operator`
      :raw-html:`<span class="hll">all_devices = list(map(operator.add, ethernet_devices, usb_devices))`
      :raw-html:`</span>`
      :raw-html:`# We can't forget our favorite computation library`
      :raw-html:`import numpy as np`
      :raw-html:`<span class="hll">all_devices = np.add(ethernet_devices, usb_devices)`
      :raw-html:`</span></pre></div></td></tr></tbody></table></div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `code block <https://www.sphinx-doc.org/en/1.5/markup/code.html#directive-code-block#images>`_.

|

Literal included
................
The ``literalincluded`` directive allows you to include code files and show then as snnipets of code within the course content. This is ideal for showing code examples stored in external files. In addition, this directive allows to emulate file comparison.

.. warning::

  * The path of the file is relative to the path of the chapter file. However, you can also use absolute paths.
  * this support many of the code-block options such as lineos and emphasize-lines.
  * You can included only some selected lines of the file.
  * This can be used to compare two different files.

literalinclude :important:`syntax` consist of the directive name, the filepath and the code-block options.

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

      :raw-html:`<div class="literal-block-wrapper docutils container" id="id27"><div class="code-block-caption"><span class="caption-text">Python diff example</span><a class="headerlink" href="#id27" title="Permalink to this code">¶</a></div><div class="highlight-udiff"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>`
      :raw-html:`1`
      :raw-html:`2`
      :raw-html:`3`
      :raw-html:`4`
      :raw-html:`5`
      :raw-html:`6`
      :raw-html:`7`
      :raw-html:`8`
      :raw-html:`9`
      :raw-html:`10`
      :raw-html:`11`
      :raw-html:`12`
      :raw-html:`13`
      :raw-html:`14</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="gd">--- /compile/course_material/python_examples/example.py.orig</span>`
      :raw-html:`<span class="gi">+++ /compile/course_material/python_examples/example.py</span>`
      :raw-html:`<span class="gu">@@ -1,7 +1,9 @@</span>`
      :raw-html:`&nbsp;def merge_two_dicts(a, b):`
      :raw-html:`<span class="gd">-    c = a.copy()   </span>`
      :raw-html:`<span class="gd">-    c.update(b)    </span>`
      :raw-html:`<span class="gi">+    c = a.copy()   # make a copy of a </span>`
      :raw-html:`<span class="gi">+    c.update(b)    # modify keys and values of a with the ones from b</span>`
      :raw-html:`&nbsp;    return c`
      :raw-html:`<span class="gi">+</span>`
      :raw-html:`&nbsp;`
      :raw-html:`&nbsp;a = { 'x': 1, 'y': 2}`
      :raw-html:`&nbsp;b = { 'y': 3, 'z': 4}`
      :raw-html:`<span class="gi">+print(merge_two_dicts(a, b)) # {'y': 3, 'x': 1, 'z': 4}</span>`
      :raw-html:`</pre></div></td></tr></tbody></table></div></div><div class="literal-block-wrapper docutils container" id="id28"><div class="code-block-caption"><span class="caption-text">Python example</span><a class="headerlink" href="#id28" title="Permalink to this code">¶</a></div><div class="highlight-python"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>`
      :raw-html:`1`
      :raw-html:`2`
      :raw-html:`3`
      :raw-html:`4`
      :raw-html:`5`
      :raw-html:`6`
      :raw-html:`7`
      :raw-html:`8`
      :raw-html:`9`
      :raw-html:`10</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="c1"># Prepended comment</span>`
      :raw-html:`<span class="k">def</span> <span class="nf">merge_two_dicts</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>`
      :raw-html:`<span class="n">&nbsp;   c</span> <span class="o">=</span> <span class="n">a</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>   <span class="c1"># make a copy of a </span>`
      :raw-html:`<span class="n">&nbsp;   c</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>    <span class="c1"># modify keys and values of a with the ones from b</span>`
      :raw-html:`<span class="k">&nbsp;   return</span> <span class="n">c</span>`
      :raw-html:`&nbsp;`
      :raw-html:`<span class="n">a</span> <span class="o">=</span> <span class="p">{</span> <span class="s1">'x'</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">'y'</span><span class="p">:</span> <span class="mi">2</span><span class="p">}</span>`
      :raw-html:`<span class="n">b</span> <span class="o">=</span> <span class="p">{</span> <span class="s1">'y'</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s1">'z'</span><span class="p">:</span> <span class="mi">4</span><span class="p">}</span>`
      :raw-html:`<span class="k">print</span><span class="p">(</span><span class="n">merge_two_dicts</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">))</span> <span class="c1"># {'y': 3, 'x': 1, 'z': 4}</span>`
      :raw-html:`<span class="c1"># Appended comment</span>`
      :raw-html:`</pre></div></td></tr></tbody></table></div></div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `Literal includes <https://www.sphinx-doc.org/en/1.6/markup/code.html#includes>`_.

|

Inline elements
---------------
.. _cross-reference:

Cross-reference
...............

Hyperlinks can be used to link external websites or to link to different part of the course. However, for linking to different sections or chapters of the course, we use the ``:ref:`` and the ``doc`` roles. These two roles create a ling to the determined target indicated by the role. However, in order to make these cross-references work we should create or have specific targets.

In the case of the ``ref:`` role, we define the target as ``.. _target-name:``. These syntax add an id to the element that is immediately below and create the target for the link.

.. warning::
  * You may add the targets above titles.
  * The `name property <https://docutils.sourceforge.io/docs/ref/rst/directives.html#name>`_ add an id to the respective element and can be use as a target.

In the case of the ``:doc:`` role the targets are the documents themselves. Therefore, the link to those documents should be an absolute or relative path.

Cross-referencing :important:`syntax` consists of the ``:ref:`` or ``:doc:`` role, with the target as the interpreted text of the roles.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''

.. rst-tabs::

  .. tab-content:: tab1-cross-reference
    :title: input: RST

    .. code-block:: rst

      `Hyperlink`_

  .. tab-content:: tab2-cross-reference
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<a class="reference internal" href="#hyperlink">Hyperlink</a>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `cross-referencing <https://www.sphinx-doc.org/en/1.6/markup/inline.html?highlight=cross%20reference>`_.

|

Substitution reference
......................
Substitution references are an *RST* element that allows referencing certain text through the use of reference text. The sustitution reference can be use in pair with hyperlinks by appendding undersore to the end, the substitution element can be also use to replace images and some other applications can be possible.

.. warning::

    * In order to use a sustitution reference, you need a sustitution definition.
    * Substitution references are case-sensitive.

Substitution reference :important:`syntax` consist of the a reference text surrounded by vartical bars. In case of implementing links the underscore should be added at the end. On the other hand, the :important:`syntax` for the substitution definition consist of two consecutive dots followed by a whitespace, the reference name wrapped in vertical bars, followed by some directive type and the data

.. |RST| replace:: reStructuredText
.. _RST: http://docutils.sourceforge.net/rst.html

|RST|_ is the best


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

      :raw-html:`<p><a class="reference external" href="http://docutils.sourceforge.net/rst.html">reStructuredText</a> is the best</p>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `substitution references <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-references>`_.

|

Download
--------

This role allows you to attach downloadable files to your course. You can use this directive to provide the students with extra material such as pdf files and code templates.

.. warning::

    *
    *

Images and figures :important:`syntax` consist of the directive name, the image URI, and some directive options. Read the official documentation for adjusting th image size and the the aligment.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-download
    :title: input: RST

    .. code-block:: rst

      The following :download:`file </course_material/rst_guide/example_file.txt>` can be downloaded.

  .. tab-content:: tab2-download
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<div class="row">`
      :raw-html:`<div class="col-12 col-md-6">`
      :raw-html:`<a class="img-responsive img-circle reference internal image-reference" href="http://localhost:8080/static/default/_images/sample.jpeg"><img alt="This is a sample image." class="img-responsive img-circle align-center" src="http://localhost:8080/static/default/_images/sample.jpeg" style="width: 380px;"></a>`
      :raw-html:`<p>This is not a caption, this is only a paragraph below the image</p>`
      :raw-html:`</div>`
      :raw-html:`<div class="col-12 col-md-6">`
      :raw-html:`<div class="figure align-center" id="id8">`
      :raw-html:`<a class="img-responsive img-thumbnail reference internal image-reference" href="http://localhost:8080/static/default/_images/sample.jpeg"><img alt="This is a sample figure." class="img-responsive img-thumbnail" src="http://localhost:8080/static/default/_images/sample.jpeg" style="width: 326.40000000000003px; height: 244.8px;"></a>`
      :raw-html:`<p class="caption"><span class="caption-text"><strong>Image X.</strong> This is the caption.</span></p>`
      :raw-html:`</div>`
      :raw-html:`</div>`
      :raw-html:`</div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_.

|

Dictionary
..........

The dictionary directive is useful for defining terms that are used throughout the course. Having a dictionary may be help the students to get familiar with the terminology used in the course. We recommend to have and independent chapter at the end of your course with the dictionary directive.

On the other hand, the question on how to use the dictionary in your document remain. For that, we will use the ``term`` role. This role allows you to create a link between the term and the definition in your dictionary. Once again you should be careful with the links that are being created in your course

.. warning::

    *
    *

Images and figures :important:`syntax` consist of the directive name, the image URI, and some directive options. Read the official documentation for adjusting th image size and the the aligment.

:glyphicon-console:`\ ` Code example
''''''''''''''''''''''''''''''''''''
.. rst-tabs::

  .. tab-content:: tab1-dictionary
    :title: input: RST

    .. code-block:: rst

      .. div:: row

        .. div:: col-12 col-md-6

          .. image:: /images/gallery/sample.jpeg
            :alt: This is a sample image.
            :width: 380px
            :align: center
            :class: img-responsive img-circle

          This is not a caption, this is only a paragraph below the image.

        .. div:: col-12 col-md-6

          .. figure:: /images/gallery/sample.jpeg
            :alt: This is a sample figure.
            :scale: 10%
            :align: center
            :class: img-responsive img-thumbnail

            **Image X.** This is the caption.

  .. tab-content:: tab2-dictionary
    :title: rendered: HTML

    .. div:: html-box

      :raw-html:`<div class="row">`
      :raw-html:`<div class="col-12 col-md-6">`
      :raw-html:`<a class="img-responsive img-circle reference internal image-reference" href="http://localhost:8080/static/default/_images/sample.jpeg"><img alt="This is a sample image." class="img-responsive img-circle align-center" src="http://localhost:8080/static/default/_images/sample.jpeg" style="width: 380px;"></a>`
      :raw-html:`<p>This is not a caption, this is only a paragraph below the image</p>`
      :raw-html:`</div>`
      :raw-html:`<div class="col-12 col-md-6">`
      :raw-html:`<div class="figure align-center" id="id8">`
      :raw-html:`<a class="img-responsive img-thumbnail reference internal image-reference" href="http://localhost:8080/static/default/_images/sample.jpeg"><img alt="This is a sample figure." class="img-responsive img-thumbnail" src="http://localhost:8080/static/default/_images/sample.jpeg" style="width: 326.40000000000003px; height: 244.8px;"></a>`
      :raw-html:`<p class="caption"><span class="caption-text"><strong>Image X.</strong> This is the caption.</span></p>`
      :raw-html:`</div>`
      :raw-html:`</div>`
      :raw-html:`</div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_.

|

Dictionary can add a hover window |Sphinx| :term:`def term <Sphinx>`

.. |Sphinx| replace:: :term:`def term <Sphinx>`

.. glossary::

  Sphinx
    Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.

  Sublime Text
    Sublime Text is a sophisticated text editor for code, markup and prose. You'll love the slick user interface, extraordinary features and amazing performance.

Error management


This is a standalone link https://docutils.sourceforge.io/docs/.

This is a link with an `Alias <https://docutils.sourceforge.io/docs/>`_

.. warning::
  * All the headings/titles create target links automatically, therefore you should try to avoid having the same title twice throughout the whole course since it can cause conflicts. If this is the case, you can override the target with and explicit target on top of the title.

The external links are easy to use and can be used through the use of snippets in VS Code.


.. code-block:: rst

  `Title <https://plus.cs.aalto.fi/>`_

::::

**Good practices at using links**

1. In order to improve the readability of your code you should create a list of links at the bottom of the page and refer to those links using tag names.

  Example

You can use this |geo_link|.

.. |geo_link| raw:: html

   <a href="http://geoiptool.com" target="_blank">Geo Link</a>

.. warning::

    *
    *

Hyperlink :important:`syntax` consists of open and closed quote marks, the target inside the quote marks and an underscore at the end.

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''

.. rst-tabs::

  .. tab-content:: tab1
    :title: input: RST

    .. code-block:: rst

      `Hyperlink`_

  .. tab-content:: tab2
    :title: rendered: HTML

    :raw-html:`<a class="reference internal" href="#hyperlink">Hyperlink</a>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `Hyperlink <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup>`_.

|

Internal
........

We can find internal links, like hyperlink_ . However, due to this type of links make use of the literal to
present the text,
it might be better to use links making use of the backticks like this -> ```image_examples`_`` or ```Images`_``.

.. warning:: Remember that changing the title of your chapters an headings can break your references.

.. warning::

  This internal links needs a target.

  .. code-block:: bash

    we can find internal links, like example_.

    .. _example:

.. hint:: It is always a good idea to place the targets to these links above a heading.
.. The titles do not need a reference

Is is also important to notice than in case of having targets compound by more than one word is neccesary to surround the word with
backticks ```<any word>```.

.. warning::

  Be careful using your links. Design the flow of your webpage and create a template for your links. It will help you to avoid breaking your links once they are defined.

.. warning::

    *
    *

