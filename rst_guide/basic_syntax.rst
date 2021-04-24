Basic Syntax
============

:Author: Aplus Team
:Last-modified: |today|

.. styled-topic::

  Main questions:
    What is the basic syntax of RST?

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
    #. Prior knowledge of *RST*, as detailed in :doc:`Chapter 3.1 </rst_guide/get_started>`.

  Estimated working time:
    40 min.


::::

Introduction
------------
In order to start authoring a course in A+, you should initiate with the most basic *RST* directives
and roles. This chapter will provide you with the fundamentals of *RST*. All the directives and
roles presented in this chapter will give you the necessary skills to create static course content.
Most advance course content will be covered in :doc:`chapter 5 </questionnaires/questionnaires>`,
:doc:`chapter 6 </programming_exercises/instructions>`, :doc:`chapter 7 </acos/introduction>`,
:doc:`chapter 9 </rubyric/introduction>`, :doc:`chapter 14 </active_elements/introduction>` and
:doc:`chapter 15 </point_of_interest/introduction>` of this manual.

.. hint::

  **Remember the following syntax rules while creating an RST document.**

  #. *RST* is sensitive to indentation.
  #. *RST* requires blank lines between paragraphs and between directives.
  #. *RST* directives and roles are case-insensitive.


  .. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `RST syntax
  <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#syntax-details>`_

|


Structural elements
--------------------
In *RST* as in many other markup languages, the use of structural components is essential to
organise the content within documents. When we talk about *RST*, sections are not created with a
particular role or directive, as is the case in HTML, where you have the ``<section>`` tag. Instead,
in *RST*, we use `titles`_ and `transitions`_ to represent sections. Therefore, we strongly suggest
the use of these structural elements to facilitate the reading and understanding of your educational
material. Using titles or headers will also allow the course to be more accessible to users who use
navigation tools and assistive technologies such as screen readers.

Titles
......
Titles in *RST* are marked with "underlines". When creating your course, it is recommended to
use a maximum of three titles within your document (Title, subtitle and subsubtitle). However, if you
need to add more, it is completely possible, but not recommend. It is also important to remember that
the titles should be descriptive, concise, should not contain cross-references and you should not
have jumps in levels (For example, from level one to level 3).

.. warning::
  * If under and overline are used, their length must be identical. However, we suggest avoiding the
    use of overlines.
  * The length of the underline must be at least as long as the title itself.

Normally, there are no title levels assigned to certain characters. Instead, the levels of headings
are determined by the order in which the underline characters are used. It means that the first
underline characters encountered in the document will be the outermost title (equivalent to a
``<h1>`` title  in HTML), the second underline characters will be indicated subtitles (equivalent to
a ``<h2>`` title in HTML), and so on.

It is also important to know that each title automatically generates a hyperlink target. The
text of the hyperlink target (reference name) is the title itself, but the whitespace between
words are replaced by hyphens. We will see more about this in the :ref:`Links section
<cross-reference>`.

Title :important:`syntax` consist of underline adornments. All the adornments should remain
consistent throughout your chapters. Therefore, you should use the adornments following the order
suggested in the table below.

.. list-table::
  :widths: 50 50
  :header-rows: 1
  :class: table table-striped table-bordered

  * - Symbol
    - Semantic
  * - ``=`` (equal sign)
    - Title of the chapter. You should have just one Title per chapter.
  * - ``-`` (hyphen)
    - Subtitle
  * - ``.`` (dot)
    - Subsubtitle
  * - ``'`` (apostrophe)
    - Subsubsubtitle. We do not recommend the use deeper level of headings.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-title
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

  .. tab-content:: tab2-title
    :title: rendered: HTML

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

Transitions (Horizontal rulers)
...............................
In addition to titles, it is possible to use transitions (horizontal rulers/lines) to add a visual
cue of the sections of your document. However, it is always advisable to use the titles as the
primary mechanism for sectioning your documents, as screen readers may not understand the purpose of
the transitions.

.. warning::

    * Horizontal ruler should not be placed at the beginning or at the end of your document.
    * Horizontal rulers should not have any indentation..
    * Horizontal rules required :abbr:`blank lines (A blank line is any line without text or a
      line that contains nothing but spaces or tabs.)` above and below.

Horizontal rules :important:`syntax` consists of four consecutive colons ``::::``. The four colons
should be surrounded by blank lines.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-ruler
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

  .. tab-content:: tab2-ruler
    :title: rendered: HTML

    :raw-html:`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vulputate felis vel bibendum dignissim. Nunc et pretium lacus. Phasellus lorem tortor, suscipit sed aliquet sit amet, tempor sit amet purus. Cras efficitur fermentum tellus sit amet aliquam. Aliquam sed turpis faucibus, aliquam augue ut, malesuada orci. Nunc ultricies malesuada risus scelerisque tristique. Mauris scelerisque nisl purus, id lobortis velit facilisis a.`
    :raw-html:`<hr>`
    :raw-html:`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vulputate felis vel bibendum dignissim. Nunc et pretium lacus. Phasellus lorem tortor, suscipit sed aliquet sit amet, tempor sit amet purus. Cras efficitur fermentum tellus sit amet aliquam. Aliquam sed turpis faucibus, aliquam augue ut, malesuada orci. Nunc ultricies malesuada risus scelerisque tristique. Mauris scelerisque nisl purus, id lobortis velit facilisis a.`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `transitions <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions>`_.

|

Body Elements
-------------
Paragraphs
..........
Paragraphs are simple blocks of text.

.. warning::

  * Paragraphs should be left-aligned
  * Blank lines separate paragraphs

Paragraphs :important:`syntax:` consist of plain text and `Inline markup`_ elements.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-paragraph
    :title: input: RST

    .. code-block:: rst

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus
      tincidunt felis. *Suspendisse convallis semper faucibus*. In eleifend nisl
      sit amet enim mollis, vitae eleifend orci euismod. Mauris vel nibh diam.
      Quisque laoreet elit ac est fermentum auctor. Phasellus massa tortor,
      interdum eu porta sed, malesuada sed erat. Morbi magna turpis, efficitur
      a venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo
      facilisis, et elementum velit venenatis.

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus
      tincidunt felis. Suspendisse convallis semper faucibus. In eleifend nisl
      sit amet enim mollis, vitae eleifend orci euismod. Mauris vel nibh diam.
      Quisque laoreet elit ac est fermentum auctor. Phasellus massa tortor,
      interdum eu porta sed, malesuada sed erat. **Morbi magna** turpis, efficitur
      a venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo
      facilisis, et elementum velit venenatis.

  .. tab-content:: tab2-paragraph
    :title: rendered: HTML

    :raw-html:`<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus
    tincidunt felis. <em>Suspendisse convallis semper faucibus</em>. In eleifend nisl
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
    interdum eu porta sed, malesuada sed erat. <b>Morbi magna</b> turpis, efficitur a
    venenatis ac, consequat lobortis tortor. Maecenas iaculis est quis justo
    facilisis, et elementum velit venenatis.</div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `paragraphs <https://docutils.sourceforge.io/docs/ref/rst/directives.html#paragraphs>`_

|

Sidebar
.......
The sidebar is a floating element that allows you to place additional information parallel to the
flow of your document.

.. warning::

  * Sidebars should not contain nested sidebars.
  * Sidebars can not be nested inside body elements.

Sidebar :important:`syntax` follows the normal :ref:`directive syntax <directive-syntax>`.
Remember that the directive argument is required for the sidebar.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-sidebar
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

  .. tab-content:: tab2-sidebar
    :title: rendered: HTML

    :raw-html:`<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tincidunt felis. Suspendisse convallis semper faucibus.</div></br><div class="sidebar"><p class="first sidebar-title">Sidebar Title</p><p    class="sidebar-subtitle">Optional Sidebar Subtitle</p><p   class="last">Subsequent indented lines comprise the body of the sidebar, and     are interpreted as body elements.</p></div><div>Lorem ipsum dolor sit amet,     consectetur adipiscing elit. Praesent cursus tincidunt felis. Suspendisse     convallis semper faucibus. In eleifend nisl sit amet enim mollis, vitae     eleifend orci euismod. Mauris vel nibh diam. Quisque laoreet elit ac est    fermentum auctor. Phasellus massa tortor, interdum eu porta sed, malesuada    sed erat. Morbi magna turpis, efficitur a venenatis ac, consequat lobortis   tortor. Maecenas iaculis est quis justo facilisis, et elementum velit    venenatis. Phasellus sit amet lobortis magna. Cras fermentum nulla eros, id   vestibulum felis feugiat ac. Mauris eget libero ut ex mollis scelerisque sit     amet vel lectus.</div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `side bars <https://docutils.sourceforge.io/docs/ref/rst/directives.html#sidebar>`_

|

Line blocks
...........

Line blocks are helpful for writing content where having a particular text structure is needed. Line
blocks start with a non-indented vertical bar, ``|``. Each of these vertical bars indicates a new
line of text. Each line beginning with the vertical bar takes into consideration whitespaces and tab
spaces.

.. warning::

  * A piece of text written in a new line might be considered the continuation of the previous line
    block.
  * Inline markup is supported.

Line block :important:`Syntax:` consist of a vertical bar ``|`` prefix at the beginning of the text
line. If the text is a continuation of the previous line block, the text should begin with
whitespace instead of the vertical bar.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-line-block
    :title: input: RST

    .. code-block:: rst
      :caption: Fragment of the Linux man documentation

      | **NAME**     top
      |
      |       man - an interface to the
       system reference manuals
      |
      | **SYNOPSIS**    top
      |
      |       man [man options] [[section] page ...] ...
      |       man -k [apropos options] regexp ...
      |       man -K [man options] [section] term ...
      |       man -f [whatis options] page ...
      |       man -l [man options] file ...
      |       man -w|-W [man options] page ...

  .. tab-content:: tab2-line-block
    :title: rendered: HTML

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

|

Quotation
.........
The *RST* markup language uses several syntaxes for writing quoted text. However, we will focus only
on two of them. The first quotation syntax is called *block quotes*, and the second quotation syntax
is called *epigraph*. The quotations are usually used to quote a piece of text or though that
someone else has write down or said. In order to indicate the author of the quote you must preceds the
author's name with double hyphens ``--``.

Block quote
''''''''''''
Block quotes are a relative indented text block, which is used to present quoted text.

.. warning::

  * A preceding text should exist because the block quote needs an anchor to evaluate whether or
    not it is a quoted text element. Otherwise, it might be considered a normal paragraph.

Block quote :important:`syntax` consist of an indented text block (quoted text), and an attribution
(text preceded by doubled hyphens ``--``).

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-blockquote
    :title: input: RST

    .. code-block:: rst

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tincidunt felis.

        "It is my business to know things. That is my trade."

        -- Sherlock Holmes

  .. tab-content:: tab2-blockquote
    :title: rendered: HTML

    :raw-html:`<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tincidunt felis.</p>`
    :raw-html:`<blockquote>`
    :raw-html:`<div>`
    :raw-html:`<p>“It is my business to know things. That is my trade.”</p><p>—Sherlock Holmes<p>`
    :raw-html:`</div>`
    :raw-html:`</blockquote>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `blocks quotes <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes>`_

|

Epigraph
''''''''
The epigraph works just as the block quote. However, the epigraph directive is independent of the
text-flow, and therefore, there is no need for having an anchor text above the epigraph.

.. warning::

  * If you are quoting someone, remember to add the double hyphens ``--`` at the end with the
    attribution

Epigraph :important:`syntax` follows the normal :ref:`directive syntax <directive-syntax>`. This
directive does not take any arguments, only content.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-epigraph
    :title: input: RST

    .. code-block:: rst

      .. epigraph::

        No matter where you go, there you are.

        -- Buckaroo Banzai

  .. tab-content:: tab2-epigraph
    :title: rendered: HTML

    :raw-html:`<blockquote>`
    :raw-html:`<div>`
    :raw-html:`<p>“ No matter where you go, there you are.”</p><p>—Buckaroo Banzai</p>`
    :raw-html:`</div>`
    :raw-html:`</blockquote>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `epigraphs <https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph>`_

|

.. _basic-lists:

Basic Lists
...........

Lists are useful to present sequential information inside a document. In general, there are two
types of lists, ordered and unordered. Nevertheless, there are also more specialised lists, such as
the definition list. In this chapter we will cover these three types of lists.

Ordered lists
'''''''''''''
In *RST* ordered lists are often called enumerated lists. This list consists of several lines of
text where each new line is preceded by a number that changes incrementally.

.. warning::
  * You must add a line break before the list.
  * Each item should be added in a new line.
  * Each element should start with the enumerated literal.
  * Nested list should be indented.

Enumerated lists :important:`syntax` consist of an enumerated literal, followed by a dot, a
whitespace and then the text that is considered the item in the list. Enumerated lists recognised
several enumerated literals, as you can see in the table below.

.. list-table::
  :widths: 50 50
  :header-rows: 1
  :class: table table-striped table-bordered

  * - Literal
    - Semantic
  * - 1., 2., 3. ...
    - Arabic numerals
  * - #., #., #., ...
    - auto incremental arabic numbers
  * - A., B., C., ... Z.
    - uppercase alphabet characters
  * - a., b., c., ... z.
    - lowercase alphabet characters
  * - I., II., III., ...
    - uppercase roman numerals
  * - i., ii., iii., ...
    - lowercase roman numerals

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-ol
    :title: input: RST

    .. code-block:: rst

      1. First Item
      2. Second Item

      A. First Item
      B. Second Item

      a. First Item
      b. Second Item

  .. tab-content:: tab2-ol
    :title: rendered: HTML

    :raw-html:`<ol class="arabic simple"><li>First Item</li><li>Second Item</li></ol>`
    :raw-html:`</br>`
    :raw-html:`<ol class="upperalpha simple"><li>Fisrt Item</li><li>Second Item</li></ol>`
    :raw-html:`<ol class="loweralpha simple"><li>Fisrt Item</li><li>Second Item</li></ol>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `enumerated lists
  <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#enumerated-lists>`_

|

Unordered Lists
'''''''''''''''
In *RST*, unordered lists are called bullet lists. This list consists of a sequence of elements with
no enumeration whatsoever. Every item is preced by a bullet point.

.. warning::
  * You must add a line break before the list.
  * Each item should be added in a new line.
  * Each element should start with the bullet point literal.
  * Nested list should be indented.

Bullet lists :important:`syntax` follow the same syntax as enumerated lists. However, the bullet
lists use different literals, among the bullet literal we can find the following ones: ``*``, ``+``,
``-``, ``•`` and ``‣``.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-ul
    :title: input: RST

    .. code-block:: rst

      * Fisrt Item
      * Second Item

      - Fisrt Item
      - Second Item

  .. tab-content:: tab2-ul
    :title: rendered: HTML

    :raw-html:`<ul class="simple"><li>Fisrt Item</li><li>Second Item</li></ul>`
    :raw-html:`<ul class="simple"><li>First Item</li><li>Second Item</li></ul>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `bullet lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists>`_

|

Definition list
'''''''''''''''
A definition list, is a special list that can be used to build a glossary or to describe program
variables.

.. warning::
  * Blank lines are required before the first and after the last definition list item
  * You can use multiple classifiers. A classifier may be used to indicate the usage of the term
    (noun, verb, reserved word, etc.).

Definition lists :important:`syntax` is relatively straightforward. Each definition list item
contains a term, optional classifiers, and a definition. The term is just a one-line word. The
optional classifier must come after the term. But between the term and the classifier there must be
a whitespace, colon, and another whitespace. The definition is a block indented relatively to
the term, and may contain multiple paragraphs and other body elements.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-definition-list
    :title: input: RST

    .. code-block:: rst

      term 1
          Definition 1.

      term 2
          Definition 2, paragraph 1.

          Definition 2, paragraph 2.

      term 3 : classifier
          Definition 3.

      term 4 : classifier one : classifier two
          Definition 4.

  .. tab-content:: tab2-definition-list
    :title: rendered: HTML

    :raw-html:`<dl class="docutils">`
    :raw-html:`<dt>term 1</dt>`
    :raw-html:`<dd>Definition 1.</dd>`
    :raw-html:`<dt>term 2</dt>`
    :raw-html:`<dd><p class="first">Definition 2, paragraph 1.</p>`
    :raw-html:`<p class="last">Definition 2, paragraph 2.</p>`
    :raw-html:`</dd>`
    :raw-html:`<dt>term 3 <span class="classifier-delimiter">:</span> <span class="classifier">classifier</span></dt>`
    :raw-html:`<dd>Definition 3.</dd>`
    :raw-html:`<dt>term 4 <span class="classifier-delimiter">:</span> <span class="classifier">classifier one</span> <span class="classifier-delimiter">:</span> <span class="classifier">classifier two</span></dt>`
    :raw-html:`<dd>Definition 4.</dd>`
    :raw-html:`</dl>`
    :raw-html:`<ul class="simple"><li>Fisrt Item</li><li>Second Item</li></ul>`
    :raw-html:`<ul class="simple"><li>First Item</li><li>Second Item</li></ul>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `definition lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists>`_

|

Tables
......
In *RST*, it is possible to create tables using a variety of directives and markup. In this guide,
we will present you with two types of tables. The first one is the so-called grid table, and the
second one is the simple table. Both tables are based on the ``table`` directive. The table
directive can be used to add an id, classes, and a label. The table directive also allows defining
the alignment, the width of the cells, and the widht of the table itself.

.. hint::
    Creating this type of tables can be cumbersome. Therefore, we suggest using some sort of table
    generator. We recommend using the following services:

    - `<https://truben.no/table/>`_
    - `<https://www.tablesgenerator.com/text_tables>`_

Grid Table
''''''''''
Grid tables can be created using several visual elements. Symbols such as the pipe symbol ``|``,
underscores ``_``, hyphens ``-``, equal sign ``=`` and the plus symbol ``+`` can be used to draw
your table. The :ref:`example <code-example-grid-table>` below shows better how the these symbols
are combined to create a grid table.

.. warning::
  * Blank lines are required before and after the grid table.
  * The left edges should be aligned with each other.

Grid table :important:`syntax` is determined by the use of the ASCII characters. Once you have drawn
your table, each individual cell is considered a miniature document.

.. _code-example-grid-table:

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-grid-table
    :title: input: RST

    .. code-block:: rst


      .. table:: Grid table example
        :widths: auto
        :name: grid-table-example

        +----------+----------+----------+
        | Header A | Header B | Header C |
        +----------+----------+----------+
        | Item 1a  | Item 1b  | None     |
        +----------+----------+----------+
        | Item 1b  | Item 2b  | None     |
        |          +---------+----------+
        |          | Item 2c  | None     |
        +----------+----------+----------+

  .. tab-content:: tab2-grid-table
    :title: rendered: HTML

    :raw-html:`<table border="1" class="colwidths-auto docutils" id="grid-table-example">`
    :raw-html:`<caption><span class="caption-text">Grid table example</span></caption>`
    :raw-html:`<colgroup>`
    :raw-html:`<col width="33%">`
    :raw-html:`<col width="33%">`
    :raw-html:`<col width="33%">`
    :raw-html:`</colgroup>`
    :raw-html:`<tbody valign="top">`
    :raw-html:`<tr class="row-odd"><td>Header A</td>`
    :raw-html:`<td>Header B</td>`
    :raw-html:`<td>Header C</td>`
    :raw-html:`</tr>`
    :raw-html:`<tr class="row-even"><td>Item 1a</td>`
    :raw-html:`<td>Item 1b</td>`
    :raw-html:`<td>None</td>`
    :raw-html:`</tr>`
    :raw-html:`<tr class="row-odd"><td rowspan="2">Item 1b</td>`
    :raw-html:`<td>Item 2b</td>`
    :raw-html:`<td>None</td>`
    :raw-html:`</tr>`
    :raw-html:`<tr class="row-even"><td>Item 2c</td>`
    :raw-html:`<td>None</td>`
    :raw-html:`</tr>`
    :raw-html:`</tbody>`
    :raw-html:`</table>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `grid tables <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables>`_

|

Simple Table
''''''''''''
The simple table, as the name implies, has a simplistic way of drawing the table in your text editor.
However, with this simpler approach comes some limitations in terms of cell layout. Simple tables
can be used for simple data sets where a row contains a single data item.

.. warning::
  * Blank lines are required before the and after the simple table
  * Simple tables allow column spans, but not row spans.

Simple table :important:`syntax` is determined by the use of the ASCII characters.

.. _code-example-simple-table:

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-simple-table
    :title: input: RST

    .. code-block:: rst

      .. table:: Simple table example
        :class: table-striped table-bordered table-hover
        :widths: auto
        :name: simple-table-example

        =====  =====
          A    not A
        =====  =====
        False  True
        True   False
        =====  =====

  .. tab-content:: tab2-simple-table
    :title: rendered: HTML

    :raw-html:`<table border="1" class="colwidths-auto table-striped table-bordered table-hover docutils" id="simple-table-example">`
    :raw-html:`<caption><span class="caption-text">Simple table example</span></caption>`
    :raw-html:`<thead valign="bottom">`
    :raw-html:`<tr class="row-odd"><th class="head">A</th>`
    :raw-html:`<th class="head">not A</th>`
    :raw-html:`</tr>`
    :raw-html:`</thead>`
    :raw-html:`<tbody valign="top">`
    :raw-html:`<tr class="row-even"><td>False</td>`
    :raw-html:`<td>True</td>`
    :raw-html:`</tr>`
    :raw-html:`<tr class="row-odd"><td>True</td>`
    :raw-html:`<td>False</td>`
    :raw-html:`</tr>`
    :raw-html:`</tbody>`
    :raw-html:`</table>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `simple tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#simple-tables>`_

|

Code
....

Highlight directive
'''''''''''''''''''

The most basic directive to add code snippets to your course content is the ``highlight`` directive.
This directive makes use of the built-in pygments library provided by Sphinx. As a result, the
snippets of code are render with an predefined code syntax higlighting.

Code highlighting can be enabled on a document-wide basis using the `highlight directive
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-highlight>`_.
Code highlighting can be also enabled on a project-wide basis using the ``highlight_language``
`configuration value
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-highlight_options>`_ inside
the **conf.py** file in your course.

.. warning::
  * When a highlight directive is encountered, it is used until the next highlight directive is
    encountered. If there is no highlight directive in the file, the global highlighting language is
    used.

Highlighting :important:`syntax` consists of the directive name, the language identifier, and some
directive options. After the ``highlight`` directive has been configured, you can start addidng code
snippets by adding double unindented colons ``::``. After the double colons you should add the
indented snippet of code.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-highlight
    :title: input: RST

    .. code-block:: rst

      .. highlight:: rst
        :linenothreshold: 1

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ut tellus sapien. Morbi fermentum
      in libero at porta. Curabitur sed accumsan dolor. Proin tortor turpis, dictum at libero quis,
      pretium dapibus mi. Aliquam nec congue libero. Cras auctor ultrices ante, eget euismod velit
      lobortis sit amet. Mauris facilisis odio ultrices, fringilla tellus ut, lacinia neque. Vestibulum ut
      velit porta, viverra urna semper, blandit sem. In efficitur sodales eleifend. Donec ex est, fringilla
      vitae mattis vel, aliquam ut tellus. Donec dapibus laoreet magna sed porta.

      ::

        Title
        =====

        First snippet of code.

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ut tellus sapien. Morbi fermentum
      in libero at porta. Curabitur sed accumsan dolor. Proin tortor turpis, dictum at libero quis,
      pretium dapibus mi. Aliquam nec congue libero. Cras auctor ultrices ante, eget euismod velit
      lobortis sit amet. Mauris facilisis odio ultrices, fringilla tellus ut, lacinia neque. Vestibulum ut
      velit porta, viverra urna semper, blandit sem. In efficitur sodales eleifend. Donec ex est, fringilla
      vitae mattis vel, aliquam ut tellus. Donec dapibus laoreet magna sed porta.

      ::

        Title
        =====

        Second snippet of code.

  .. tab-content:: tab2-highlight
    :title: rendered: HTML

    :raw-html:`<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ut tellus sapien. Morbi fermentum`
    :raw-html:`in libero at porta. Curabitur sed accumsan dolor. Proin tortor turpis, dictum at libero quis,`
    :raw-html:`pretium dapibus mi. Aliquam nec congue libero. Cras auctor ultrices ante, eget euismod velit`
    :raw-html:`lobortis sit amet. Mauris facilisis odio ultrices, fringilla tellus ut, lacinia neque. Vestibulum ut`
    :raw-html:`velit porta, viverra urna semper, blandit sem. In efficitur sodales eleifend. Donec ex est, fringilla`
    :raw-html:`vitae mattis vel, aliquam ut tellus. Donec dapibus laoreet magna sed porta.</p>`
    :raw-html:`<div class="highlight-rst"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>1`
    :raw-html:`2`
    :raw-html:`3`
    :raw-html:`4</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="gh">Title</span>`
    :raw-html:`<span class="gh">=====</span>`
    :raw-html:`First snippet of code.`
    :raw-html:`</pre></div>`
    :raw-html:`</td></tr></tbody></table></div>`
    :raw-html:`<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ut tellus sapien. Morbi fermentum`
    :raw-html:`in libero at porta. Curabitur sed accumsan dolor. Proin tortor turpis, dictum at libero quis,`
    :raw-html:`pretium dapibus mi. Aliquam nec congue libero. Cras auctor ultrices ante, eget euismod velit`
    :raw-html:`lobortis sit amet. Mauris facilisis odio ultrices, fringilla tellus ut, lacinia neque. Vestibulum ut`
    :raw-html:`velit porta, viverra urna semper, blandit sem. In efficitur sodales eleifend. Donec ex est, fringilla`
    :raw-html:`vitae mattis vel, aliquam ut tellus. Donec dapibus laoreet magna sed porta.</p>`
    :raw-html:`<div class="highlight-rst"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>1`
    :raw-html:`2`
    :raw-html:`3`
    :raw-html:`4</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="gh">Title</span>`
    :raw-html:`<span class="gh">=====</span>`
    :raw-html:`Second snippet of code.`
    :raw-html:`</pre></div>`
    :raw-html:`</td></tr></tbody></table></div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `the highlight directive <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-highlight>`_

|

Admonition blocks
.................

*RST* has an considerable list of admonitions blocks that are used to highlight pieces of
information. However, on a more general level, the admonition blocks are divided into two types.
The first type is known as the specific admonition. The second type is known as the generic
admonition.

You can combine and use as many admonitions types as you wish. However, we strongly recommend to
select only a few of them, and use them consistently throughout the course. As an example, you can
see that in this course, we have only used the admonition type *warning* for common errors than can
cause trouble while doing something, the admonition type *note* for adding information that might
not fit the flow of the text, but is still relevant, and the admonition type *hint* for providing
information that could help do things easier or faster. In addition to those specific admonitions,
we use the generic admonition to define some terms that required an extended explanation. It may be
also a good idea to explain to the students how you plan to use these admonition types throughout
the course.

Specific
''''''''
Specific admonitions are predefined admonition that might have a purpose within your document such
as, add extra information, advise about some good practices, point out or alert about something.

.. warning::

  * The content of the admonition can be placed as a directive argument. However, that is considered
    a bad practice. It is better to place the content as directive content.

Specific admonitions :important:`syntax` consist of the admonition type directive followed by the
admonition content.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-specific
    :title: input: RST

    .. code-block:: rst

      .. warning::

        This is a warning

      .. note::

        This is a note

      .. hint::

        This is a hint

  .. tab-content:: tab2-specific
    :title: rendered: HTML

    :raw-html:`<div class="admonition warning"><p class="first admonition-title">Warning</p><p class="last">This is a warning</p></div>`
    :raw-html:`<div class="admonition note"><p class="first admonition-title">Note</p><p class="last">This is a note</p></div>`
    :raw-html:`<div class="admonition hint"><p class="first admonition-title">Hint</p><p class="last">This is a hint</p></div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `specifc admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions>`_

|

Generic
'''''''
Generic admonitions allow you to define the title and the content of the admonition. As well as the
specific admonitions the generic admonition are rendered as an offset block in the document.

Generic admonitions :important:`syntax` consist of the admonition type directive, a title and the
admonition content.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-generic
    :title: input: RST

    .. code-block:: rst

      .. admonition:: reStructuredText
        :class: meta

        reStructuredText is plaintext that uses simple and intuitive constructs to indicate the
        structure of a document. These constructs are equally easy to read in raw and processed
        forms.

  .. tab-content:: tab2-generic
    :title: rendered: HTML

    :raw-html:`<div class="meta admonition">`
    :raw-html:`<p class="first admonition-title">reStructuredText</p>`
    :raw-html:`<p class="last">reStructuredText is plaintext that uses simple and intuitive constructs to indicate the structure of a document. These constructs are equally easy to read in raw and processed forms</p></div>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about**  `generic admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#generic-admonition>`_

|

Inline elements
---------------

Inline markup
..............

It is always possible to add semantic meaning to your text, and inline markup allows you to do so.
Inline markup applies to words or phrases within a text block.

.. warning::
  * The text within inline markup should not begin or end with whitespaces.
  * Inline markup cannot be nested.

Inline markup :important:`syntax` consists of open and closed charactered with some text between
them. The characters that can be used to create inline semantic elements are: asterisk ``*``,
double asterisk ``**`` and backticks ``````. The HTML representation od these inline elements are
the ``<strong>`` tag, the ``<em>`` tag and the ``<code>`` tag respecively.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-inline
    :title: input: RST

    .. code-block:: rst

      *emphasis*
      **strong emphasis**
      ``inline literals``

  .. tab-content:: tab2-inline
    :title: rendered: HTML

    :raw-html:`<strong>emphasis</strong><br>`
    :raw-html:`<em>strong emphasis</em><br>`
    :raw-html:`<code>inline literals</code>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `inline markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup>`_.

|

Abbreviation
............
Abbreviation provides basic functionality for defining term on the fly. This *RST* role allows the
end-user to hover over the specified term and see the metainformation related to that abbreviation
in a tooltip.

Abbreviation :important:`syntax` is represente with the ``:abrr:`` keyword. Within that backticks
that wrap the role content, you shloud place the abbreviation or term that you want to define, then
leave a whitespace, and then use parentheses to enclose the definition of the term.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-abbreviation
    :title: input: RST

    .. code-block:: rst

      I can use abbreviations to define :abbr:`terms (This is a term definition)` on the fly.

  .. tab-content:: tab2-abbreviation
    :title: rendered: HTML

    :raw-html:`<p>I can use abbreviations to define <abbr title="This is a term definition">terms</abbr> on the fly</p>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `abbreviations <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html?highlight=abbreviation#role-abbr>`_.

|

kbd roles
.........
Kbd roles are used to specify a textual user input from a keyboard.

kbd :important:`syntax` is represented with the ``:abrr:`` keyword. Within that backticks that wrap
the role content, you shloud place the keystroke you want to represent.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-kbd
    :title: input: RST

    .. code-block:: rst

      Press the following keys in your keyboard. :kbd:`Ctrl` + :kbd:`s`

  .. tab-content:: tab2-kbd
    :title: rendered: HTML

    :raw-html:`<p>Press the following keys in your keyboard. <code class="kbd docutils literal"><span class="pre">Ctrl</span></code> + <code class="kbd docutils literal"><span class="pre">s</span></code></p>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `kbd <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html?highlight=abbreviation#role-kbd>`_.

|

Hyperlink
..........

Hyperlinks can be used to link external websites or to link to different parts of the course content.
In this section, we will cover hyperlinks that lead the users to external websites. For more
information about internal links, you can see the :ref:`cross-reference` section.

.. warning::
  **The embedded links with aliases**
  * A whitespace cannot be placed after the opening backtick.
  * A whitespace cannot be placed before the closing backtick.

We have **standalone links** and **embedded links with aliases**. The standalone links :important:`syntax`
consist of a plain URI. The embedded links with aliases :important:`syntax` consist of an opening
backtick, the alias text, whitespace, the less-than sign ``<``, the URI, the greater-than
sign ``>``, the closing backtick and finally an underscore.

:glyphicon-console:`\ ` **Code example**

.. rst-tabs::

  .. tab-content:: tab1-links
    :title: input: RST

    .. code-block:: rst

      This is a standalone link https://docutils.sourceforge.io/docs/.
      This is a link with an `Alias <https://docutils.sourceforge.io/docs/>`_

  .. tab-content:: tab2-links
    :title: rendered: HTML

    :raw-html:`<p>This is a standalone link <a class="reference external" href="https://docutils.sourceforge.io/docs/">https://docutils.sourceforge.io/docs/</a>.</p>`
    :raw-html:`<p>This is a link with an <a class="reference external" href="https://docutils.sourceforge.io/docs/">Alias</a></p>`

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** `hyperlinks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-references>`_.

|
