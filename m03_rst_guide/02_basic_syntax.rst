.. The roles  should be created at the beginning of the document. Global roles can be created in the `global.rst` file

.. include:: /global.rst

.. Chapter content

Basic Syntax
============

:Author: Aplus Team
:Last-modified: |today|

.. styled-topic::

  Main questions: 
    What is the basic syntax of RST? 
  
  Topics: 
    In this section we will talk about:

    * `Introduction`_
    * `Structural elements`_
    * `Body elements`_
    * `Inline elements`_
  
  Requirements:
    #. You only need basic computing and programming skills, prior knowledge about markup languages might be beneficial.
    #. A basic environment set-up, as detailed in :doc:`Module 2 </m02_setup/01_first_steps>`.
    #. Prior knowledge of *RST*, as detailed in :doc:`Chapter 3.1 </m03_rst_guide/01_get_started>`.

  Estimated working time:
    40 min.


::::

Introduction
------------
In order to start authoring a course in A+, you should initiate with the most basic *RST* directives and roles. Therefore, all the directives and roles presented in this chapter will provide you with the necessary skills to create learning material. However, all the content that could be produced after reading this chapter will be strictly reading material. Exercise type content will be covered in :doc:`Chapter 3.4 </m03_rst_guide/04_aplus_syntax>` and some other chapters of this manual. 

.. div:: html-box

  **Remember the following syntax rules while creating an RST document.** 

  #. *RST* is sensitive to indentation.
  #. *RST* requires blank lines between paragraphs and between directives.
  #. *RST* directives and roles are case-insensitive.

  .. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `RST syntax <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#syntax-details>`_

|


Structural elements
--------------------
In *RST* as in many other markup languages, the use of sections is essential to split the content into multiple pieces that allow the end-users to read presented material in a more friendly manner. In *RST*, sections are mainly created through `titles`_ and `transitions`_. These two elements allow the author of the course to divide topics in small parts, creating a clear structure of subtopics within the chapter.

Titles
......
The titles in *RST* are marked up with "underlines". When creating your course, it is recommended to use a maximum of three titles within your document (Title,Subtitle and subsubtitle). However, if you need to add more, it is possible. 

.. warning:: 
  * If under and overline are used, their length must be identical. However, we do not suggest using overlines.
  * The length of the underline must be at least as long as the title itself.

Normally, there are no title levels assigned to certain characters as the structure is determined from the succession of title. The first style encountered will be an outermost title (like HTML H1), the second style will be a subtitle (like HTML H2), the third will be a subsubtitle (like HTML H3), and so on.

It is also important to remember that each title automatically generates a hyperlink target. The text of the hyperlink target (reference name) is the verbatim title. We will see more about this in the :ref:`Links section <extended-syntax-links>`.

Title :important:`syntax` consist of underline adornments, and all the adornments should remain consistent throughout your chapters. Therefore, you should use the adornments following the order suggested in the table below.

.. list-table:: 
  :widths: 50 50
  :header-rows: 1
  :class: table table-striped table-bordered

  * - Symbol
    - Semantic
  * - ``=`` (equal sign)
    - Title of the chapter. (Use only underline)
  * - ``-`` (hyphen)
    - Section
  * - ``.`` (dot)
    - Subsection
  * - ``'`` (apostrophe)
    - Subsubsection


:glyphicon-console:`\ ` **Code example** 
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      Chapter Title
      ==============

      Section title
      -------------
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur malesuada nulla ut eleifend placerat. 
      Curabitur sit amet nibh convallis, facilisis.

      Section subtitle
      ................
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur malesuada nulla ut eleifend placerat. 
      Curabitur sit amet nibh convallis, facilisis.

      Section subsubtitle
      '''''''''''''''''''
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur malesuada nulla ut eleifend placerat. 
      Curabitur sit amet nibh convallis, facilisis.

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<h1>Chapter Title</h1>`
      :raw-html:`<h2>Section title</h2>`
      :raw-html:`<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur malesuada nulla ut eleifend placerat. Curabitur sit amet nibh convallis, facilisis.</p>`
      :raw-html:`<h3>Section subtitle</h3>`
      :raw-html:`<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur malesuada nulla ut eleifend placerat. Curabitur sit amet nibh convallis, facilisis.</p>`
      :raw-html:`<h4>Section subsubtitle</h4>`
      :raw-html:`<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur malesuada nulla ut eleifend placerat. Curabitur sit amet nibh convallis, facilisis.</p>`

.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `titles <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections>`_

|

Transitions
...........
In addition to the titles, it is possible to use transitions (horizontal rulers/lines) to differentiated sections within your document. The horizontal rulers allows separating body elements visually. This separation shows the reader that a new topic is being started.

.. warning::

    * Horizontal ruler should not be placed at the beginning or at the end of your document. 
    * Horizontal rulers should not have any indentation.
    * Horizontal rulers are intended to separate sections within your document nor as ornamental decorators.
    * Horizontal rules required a :abbr:`blank lines (A blank line is any line without text or a line that contains nothing but spaces or tabs.)` above and below.

Horizontal rule :important:`syntax` consist of four consecutive colons ``::::``. 

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vulputate
      felis vel bibendum dignissim. Nunc et pretium lacus. Phasellus lorem 
      tortor, suscipit sed aliquet sit amet, tempor sit amet purus. Cras 
      efficitur fermentum tellus sit amet aliquam. Aliquam sed turpis faucibus, 
      aliquam augue ut, nmalesuada orci. Nunc ultricies malesuada risus 
      scelerisque tristique. Mauris scelerisque nisl purus, id lobortis velit 
      facilisis a. 
      
      ::::
      
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vulputate 
      felis vel bibendum dignissim. Nunc et pretium lacus. Phasellus lorem 
      tortor, suscipit sed aliquet sit amet, tempor sit amet purus. Cras 
      efficitur fermentum tellus sit amet aliquam. Aliquam sed turpis faucibus, 
      aliquam augue ut, malesuada orci. Nunc ultricies malesuada risus 
      scelerisque tristique. Mauris scelerisque nisl purus, id lobortis velit 
      facilisis a.

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vulputate felis vel bibendum dignissim. Nunc et pretium lacus. Phasellus lorem tortor, suscipit sed aliquet sit amet, tempor sit amet purus. Cras efficitur fermentum tellus sit amet aliquam. Aliquam sed turpis faucibus, aliquam augue ut, malesuada orci. Nunc ultricies malesuada risus scelerisque tristique. Mauris scelerisque nisl purus, id lobortis velit facilisis a.`  
      :raw-html:`<hr>`
      :raw-html:`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vulputate felis vel bibendum dignissim. Nunc et pretium lacus. Phasellus lorem tortor, suscipit sed aliquet sit amet, tempor sit amet purus. Cras efficitur fermentum tellus sit amet aliquam. Aliquam sed turpis faucibus, aliquam augue ut, malesuada orci. Nunc ultricies malesuada risus scelerisque tristique. Mauris scelerisque nisl purus, id lobortis velit facilisis a.`

.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `transitions <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions>`_.

|

Sidebar
.......
The sidebar is a nonrecursive section-like construct. Basically, the sidebar is a floating element that allows you to place additional information parallel to the flow of your document. 

.. warning:: 
  * Sidebars should not contain nested sidebars.
  * Sidebars can not be nested inside body elements.

Sidebar :important:`syntax` follows the normal :ref:`directive syntax <directive-syntax>`, which is two dots + one whitespace + name of the directive + double colom, i.e. ``.. directive_name::``. Remember that the directive argument is required for the sidebar.

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst
      
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus 
      tincidunt felis. Suspendisse convallis semper faucibus.

      .. sidebar:: Sidebar Title
        :subtitle: Optional Sidebar Subtitle

        Subsequent indented lines comprise
        the body of the sidebar, and are
        interpreted as body elements.
      
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus 
      tincidunt felis. Suspendisse convallis semper faucibus. In eleifend nisl 
      sit amet enim mollis, vitae eleifend orci euismod. Mauris vel nibh diam.
      Quisque laoreet elit ac est fermentum auctor. Phasellus massa tortor, 
      interdum eu porta sed, malesuada sed erat. Morbi magna turpis, efficitur a 
      venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo 
      facilisis, et elementum velit venenatis. Phasellus sit amet lobortis magna. 
      Cras fermentum nulla eros, id vestibulum felis feugiat ac. Mauris eget 
      libero ut ex mollis scelerisque sit amet vel lectus.

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tincidunt felis. Suspendisse convallis semper faucibus.</div></br><div class="sidebar"><p class="first sidebar-title">Sidebar Title</p><p    class="sidebar-subtitle">Optional Sidebar Subtitle</p><p   class="last">Subsequent indented lines comprise the body of the sidebar, and     are interpreted as body elements.</p></div><div>Lorem ipsum dolor sit amet,     consectetur adipiscing elit. Praesent cursus tincidunt felis. Suspendisse     convallis semper faucibus. In eleifend nisl sit amet enim mollis, vitae     eleifend orci euismod. Mauris vel nibh diam. Quisque laoreet elit ac est    fermentum auctor. Phasellus massa tortor, interdum eu porta sed, malesuada    sed erat. Morbi magna turpis, efficitur a venenatis ac, consequat lobortis   tortor. Maecenas iaculis est quis justo facilisis, et elementum velit    venenatis. Phasellus sit amet lobortis magna. Cras fermentum nulla eros, id   vestibulum felis feugiat ac. Mauris eget libero ut ex mollis scelerisque sit     amet vel lectus.</div>`

.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about** `side bars <https://docutils.sourceforge.io/docs/ref/rst/directives.html#sidebar>`_

|

Body Elements
-------------
Paragraphs
..........
Paragraphs are a simple block of text written in your text editor.
 
.. warning:: 
  
  * Paragraphs should be left-aligned
  * Blank lines separate paragraphs

Paragraphs :important:`syntax:` consist of plain text and `Inline markup`_ elements within them.

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst
      
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus 
      tincidunt felis. Suspendisse convallis semper faucibus. In eleifend nisl 
      sit amet enim mollis, vitae eleifend orci euismod. Mauris vel nibh diam.
      Quisque laoreet elit ac est fermentum auctor. Phasellus massa tortor, 
      interdum eu porta sed, malesuada sed erat. Morbi magna turpis, efficitur 
      a venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo 
      facilisis, et elementum velit venenatis. 

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus 
      tincidunt felis. Suspendisse convallis semper faucibus. In eleifend nisl 
      sit amet enim mollis, vitae eleifend orci euismod. Mauris vel nibh diam.
      Quisque laoreet elit ac est fermentum auctor. Phasellus massa tortor, 
      interdum eu porta sed, malesuada sed erat. Morbi magna turpis, efficitur 
      a venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo 
      facilisis, et elementum velit venenatis. 

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus 
      tincidunt felis. Suspendisse convallis semper faucibus. In eleifend nisl 
      sit amet enim mollis, vitae eleifend orci euismod. Mauris vel nibh diam.
      Quisque laoreet elit ac est fermentum auctor. Phasellus massa tortor, 
      interdum eu porta sed, malesuada sed erat. Morbi magna turpis, efficitur a 
      venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo 
      facilisis, et elementum velit venenatis.</div>`
      :raw-html:`<br>`
      :raw-html:`<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus 
      tincidunt felis. Suspendisse convallis semper faucibus. In eleifend nisl 
      sit amet enim mollis, vitae eleifend orci euismod. Mauris vel nibh diam.
      Quisque laoreet elit ac est fermentum auctor. Phasellus massa tortor, 
      interdum eu porta sed, malesuada sed erat. Morbi magna turpis, efficitur a 
      venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo 
      facilisis, et elementum velit venenatis.</div>`

.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about** `paragraphs <https://docutils.sourceforge.io/docs/ref/rst/directives.html#paragraphs>`_

|

Line blocks
...........

Line blocks are useful for writing content, where having a particular text structure is needed. Line blocks start with a non-indented vertical bar ``|``. Each of these vertical bars indicates a new line of text. Each line starting with the vertical bar take into consideration whitespaces and tab spaces.

.. warning:: 
  * A piece of text written in a new line, might be consider the continuation  of the previous line block.
  * Inline markup is supported.

Line block :important:`Syntax:` consist of a vertical bar ``|`` prefix at the beginning of the text line. If the text is a continuation of the previous line block, the text should begin with whitespace in place of the vertical bar.

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''

.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst
      :caption: Fragment of the Linux man documentation

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tincidunt felis.

      | **NAME**     top
      |
      |       man - an interface to the system reference manuals
      |
      | **SYNOPSIS**    top
      |
      |       man [man options] [[section] page ...] ...
      |       man -k [apropos options] regexp ...
      |       man -K [man options] [section] term ...
      |       man -f [whatis options] page ...
      |       man -l [man options] file ...
      |       man -w|-W [man options] page ...

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<div class="line-block">`
      :raw-html:`<div class="line"><strong>NAME</strong>     top</div>`
      :raw-html:`<div class="line"><br></div>`
      :raw-html:`<div class="line-block">`
      :raw-html:`<div class="line">man - an interface to the system reference manuals</div>`
      :raw-html:`<div class="line"><br></div>`
      :raw-html:`</div>`
      :raw-html:`<div class="line"><strong>SYNOPSIS</strong>    top</div>`
      :raw-html:`<div class="line"><br></div>`
      :raw-html:`<div class="line-block">`
      :raw-html:`<div class="line">man [man options] [[section] page …] …</div>`
      :raw-html:`<div class="line">man -k [apropos options] regexp …</div>`
      :raw-html:`<div class="line">man -K [man options] [section] term …</div>`
      :raw-html:`<div class="line">man -f [whatis options] page …</div>`
      :raw-html:`<div class="line">man -l [man options] file …</div>`
      :raw-html:`<div class="line">man -w|-W [man options] page …</div>`
      :raw-html:`</div>`
      :raw-html:`</div>`
  
.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `line blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks>`_

Quotation
.........

There are several ways of writing a quoted text. However, in this manual, we will focus on two of them. The first quotation syntax is called *block quotes*, and the second quotation syntax is called *epigraph*.

Block quote
''''''''''''
Block quotes are a relative indented text block, which is used to present quoted text.

.. warning:: 
  * A preceding text should exist because the block quote needs an anchor to evaluate whether or not it is a quoted text element. Otherwise, it might be considered a normal paragraph.

Block quote :important:`syntax` consist of an indented text block, and an attribution (text line preceded by the ``--`` symbol).  

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tincidunt felis.

        "It is my business to know things.  That is my trade."    

        -- Sherlock Holmes

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tincidunt felis.</p>`
      :raw-html:`<blockquote>`
      :raw-html:`<div>`
      :raw-html:`<p>“It is my business to know things.  That is my trade.”</p><p class="attribution">—Sherlock Holmes</p>`
      :raw-html:`</div>`
      :raw-html:`</blockquote>`
  
.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `blocks quotes <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes>`_

|

Epigraph
''''''''
The epigraph works just as the block quotes. However, the epigraph is independent of the text-flow and therefore, there is no need to have anchor text above the epigraph.

.. warning:: 
  * Remember to add the `--` symbol at the end with the attribution

Epigraph :important:`syntax` follows the normal :ref:`directive syntax <directive-syntax>`, which is two dots + one whitespace + name of the directive + double colon, i.e. ``.. directive_name::``. In addition, the attribution should be added at the end of the directive content preceded by the `--` symbol.  

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      .. epigraph::

        No matter where you go, there you are.

        -- Buckaroo Banzai

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<blockquote>`
      :raw-html:`<div>`
      :raw-html:`<p>“ No matter where you go, there you are.”</p><p class="attribution">—Buckaroo Banzai</p>`
      :raw-html:`</div>`
      :raw-html:`</blockquote>`
  
.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `epigraphs <https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph>`_

|

Lists
.....

List are useful to present sequential information inside a document. In general, exist to types of lists, ordered and unordered. Exist also another set of lists, but those are presented in the :doc:`advanced RST module </m03_rst_guide/03_advanced_syntax>`.

Ordered lists
'''''''''''''
In *RST* ordered lists are often called enumerated lists. This list consists of a numbered sequence of elements.

.. warning:: 
  * Always separate the elements of the list with a line break.
  * Each element should start with the enumerated literal.
  * Nested list should be indented.

Enumerated lists :important:`syntax` consist of an enumerated literal, followed by a whitespace and the text that define the item list. Enumerated lists recognised several enumerated literals. 

.. list-table:: 
  :widths: 50 50
  :header-rows: 1
  :class: table table-striped table-bordered

  * - Literal
    - Semantic
  * - 1, 2, 3 ...
    - Arabic numerals
  * - A, B, C, ... Z
    - uppercase alphabet characters
  * - a, b, c, ... z
    - lowercase alphabet characters
  * - I, II, III, ... 
    - uppercase roman numerals
  * - i, ii, iii, ...
    - lowercase roman numerals

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst
      
      1. Item 1
      2. Item 2

      A. Item A
      B. Item B

      a. Item a
      b. Item b

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<ol class="arabic simple"><li>First Item</li><li>Second Item</li></ol>`
      :raw-html:`</br>`
      :raw-html:`<ol class="upperalpha simple"><li>Fisrt Item</li><li>Second Item</li></ol>`
      :raw-html:`<ol class="loweralpha simple"><li>Fisrt Item</li><li>Second Item</li></ol>`
  
.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `enumerated lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#enumerated-lists>`_

|

Unordered Lists
...............
In *RST* unordered lists are called bullet lists. This list consists of a  sequence of elements without any enumeration.

.. warning:: 
  * Bullet list follows the same rules than enumerated lists.

Bullet lists :important:`syntax` follows the same syntax than the enumerated lists. However, the bullet lists use different literals, among the bullet literal we can find the following ones: ``*``, ``+``, ``-``, ``•`` and ``‣``.

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''
.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      * Item x
      * Item x

      - Item -
      - Item -

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<ul class="simple"><li>Fisrt Item</li><li>Second Item</li></ul>`
      :raw-html:`<ul class="simple"><li>First Item</li><li>Second Item</li></ul>`
  
.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `bullet lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists>`_

|

Admonition blocks
------------------

*RST* has an extensive list of :abbr:`admonition (it is a piece of advice that is also a warning to someone about their behaviour)` blocks that are used to highlight information. However, on a more general level, the admonition blocks are divided into two types, one is the specific admonition, and the other one is the generic admonition. 

You can use as many admonitions as you would like in your course. However, we strongly recommend to select only a few of them, and use them consistently throughout the course. As an example, you can see that in this course, we only use: 

- *warning* for common errors than can cause trouble while doing something. 
- *note* for adding information that might not fit the flow of the text, but is still relevant. 
- *hint* for providing inside information that could help do things easier or faster. 
- Additionally, in this course, we used the generic admonition to define some terms that required an extended explanation.


Specific
.........
Specific admonitions are predefined admonition that might have a purpose within your document such as, add extra information, advise about some good practices, point something out, or alert. Therefore, the specific admonitions add an offset block in the document, with the title which matches the admonition type.

.. warning:: 
  * The content of the admonition can be placed as a directive argument. However, that is considered a bad practice. It is better to place the content as directive content. more information about directive structure can be found in :ref:`Chapter 3.1 <directive-syntax>`.

Specific admonitions :important:`syntax` consist of the admonition type and the admonition content. 

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''

.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      .. warning:: 

        This is a warning

      .. note:: 

        This is a note

      .. hint:: 

        This is a hint

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<div class="admonition warning"><p class="first admonition-title">Warning</p><p class="last">This is a warning</p></div>`
      :raw-html:`<div class="admonition note"><p class="first admonition-title">Note</p><p class="last">This is a note</p></div>`
      :raw-html:`<div class="admonition hint"><p class="first admonition-title">Hint</p><p class="last">This is a hint</p></div>`
  
.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `specifc admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions>`_

|

Generic
.......
Generic admonitions let the user define the title of the admonition. Therefore, this type of admonition can be used to define terms within the document. As well as the specific admonitions the generic admonition are render as an offset block in the document.

.. warning:: 
  * The title of the generic admonition will be converted to a class. Therefore, you should be careful and do not use names that are being used by CSS or any other javascript code.

Generic admonitions :important:`syntax` consist of the admonition type, title and the admonition content. 

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''

.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      .. admonition:: reStructuredText
        :class: meta

        reStructuredText is plaintext that uses simple and intuitive constructs to indicate the structure of a document. These constructs are equally easy to read in raw and processed forms.      

  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<div class="meta admonition">`
      :raw-html:`<p class="first admonition-title">reStructuredText</p>`
      :raw-html:`<p class="last">reStructuredText is plaintext that uses simple and intuitive constructs to indicate the structure of a document. These constructs are equally easy to read in raw and processed forms</p></div>`
  
.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `specifc admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions>`_

|

Inline elements
---------------

Inline markup
..............

It is always possible to add certain semantic meaning to your text, and inline markup allows you to do so. Inline markup applies to words or phrases within a text block.

.. warning:: 
  * The text within inline markup should not begin or end with whitespaces.
  * Inline markup cannot be nested.

Inline markup :important:`syntax` consists of open and closed charactered with some text between them. The defined characters are ``*``,  ``**`` or ``````. 

:glyphicon-console:`\ ` **Code example**
''''''''''''''''''''''''''''''''''''''''

.. content-tabs::

  .. tab-container:: tab1
    :title: input: RST

    .. code-block:: rst

      *emphasis*  
      **strong emphasis**
      ``inline literals``
  
  .. tab-container:: tab2
    :title: output: HTML

    .. div:: html-box

      :raw-html:`<strong>emphasis</strong><br>`
      :raw-html:`<em>strong emphasis</em><br>`
      :raw-html:`<code>inline literals</code>`

.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about** `inline markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup>`_.

|


