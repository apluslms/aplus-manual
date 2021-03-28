Get Started
===========

:Author: Aplus Team
:Date: |today|

.. styled-topic::

  Main questions:
  	What are RST and Sphinx?

  Topics:
    In this section, we will present the following topics:

    * `What is reStructuredText?`_
    * `What is Sphinx?`_
    * `Directives and Roles`_
    * `What are the benefits of RST and Sphinx?`_
    * `How should I read the reStructuredText official Documentation?`_
    * `Tips to start creating your course`_

  Requirements:
    #. You only need basic computing and programming skills, prior knowledge about markup languages
       might be beneficial.
    #. A basic environment setup, as detailed in :doc:`Module "Set up environment" </set_up_environment/first_steps>`

  Estimated working time:
  	30 min.

::::

What is reStructuredText?
-------------------------

*RST* is basically another :abbr:`markup language (A markup language is a computer language that
uses tags to define elements within a document. It is human-readable, meaning markup files contain
standard words, rather than typical programming syntax)`. Markup languages make
use of symbols and keywords to structure the content of the documents. Therefore, creating *RST*
documents force you to follow a different workflow from the one you would typically follow when
creating documents with traditional `WYSIWYG <https://en.wikipedia.org/wiki/WYSIWYG>`_ editors, such
as Microsoft Word or Google documents.

Let's start by destructuring a small :ref:`snippet of RST code <rst-first-code-snippet>`. The
*RST* syntax is rather intuitive and follows the logic of any other markup languages. If you
have no experience using markup languages, it may be more difficult for you to start authoring *RST*
courses. But you do not have to worry, the learning curve of the *RST* markup language is low, and
once you start writing your first document, you will find it easier to produce new content. Besides,
you can use this whole module as a boilerplate for the creation of your course content.

The following snippet of code presents a perfectly valid *RST* document. The code contains a set of
markup symbols and keywords with a syntactical meaning that will help you to structure the content
of your documents.

.. _rst-first-code-snippet:

:sub:`Basic structure of an RST document`

.. annotated::

  .. code-block:: rst

    1«Chapter Title
    =============»

    1«First Section
    -------------»

    This is the first paragraph. It is tiny.

    This is the second paragraph. Note that paragraphs can span multiple
    lines, but they are still rendered as one block after compilation.
    *Italics* and **boldface** are produced this way.

    1«First Sub-Section
    .................»

    This is a link to the 2«`Aalto website <http://www.aalto.fi>`_». In RST you can also include
    images or files. The following image is taken from the internet, but you could include images
    located in your course folder.

    .. image:: https://geekyshacklebolt.files.wordpress.com/2018/07/rest.jpg
      :align: center
      :class: img-responsive

    1«Second Section
    --------------»
    Lists can also be made in RST.

    3«- Lists do not require much markup.
    - Create lists is intuitive.
    - Notice the lack of markup compared to HTML»

    Almost everything that exists in HTML can also be produced with RST.

  .. annotation::

    The "=, -, and ." symbols underline a sentence that is rendered as a heading in the browser.

  .. annotation::

    A link to the Aalto.fi website.

  .. annotation::

    An unordered list of elements.


The :ref:`example below <rst-to-html-example>` illustrates how a piece of *RST* code looks like in
its HTML representation. In this example, you can see how each *RST* symbol and keyword has an
equivalent representation in HTML.

.. _rst-to-html-example:

.. rst-tabs::

  .. tab-content:: tab-code
    :title: input: RST

    .. code-block:: rst

      Chapter Title
      =============

      First Section
      -------------

      This is the first paragraph. It is tiny.

      This is the second paragraph. Note that paragraphs can span multiple
      lines, but they are still rendered as one block after compilation.
      *Italics* and **boldface** are produced this way.

      First Sub-Section
      .................

      This is a link to the `Aalto website <http://www.aalto.fi>`. In RST you can also include
      images or files. The following image is taken from the internet, but you could include images
      located in your course folder.

      .. image:: https://geekyshacklebolt.files.wordpress.com/2018/07/rest.jpg
        :align: center
        :class: img-responsive

      1«Second Section
      --------------»
      Lists can also be made in RST.
      - Lists do not require much markup.
      - Create lists is intuitive.
      - Notice the lack of markup compared to HTML

      Almost everything that exists in HTML can also be produced with RST.

  .. tab-content:: tab-html-render
    :title: rendered: HTML

    :raw-html:`<h1>Chapter Title</h1>`
    :raw-html:`<h2>First Section</h2>`
    :raw-html:`<p>This is the first paragraph. It is tiny.</p>`
    :raw-html:`</br>`
    :raw-html:`<p>This is the second paragraph. Note that paragraphs can span multiple lines, but they are still
    rendered as one block after compilation. Italics and boldface are produced this way.</p>`
    :raw-html:`<h3>First Sub-Section¶</h3>`
    :raw-html:`<p>This is a link to the <a class="reference external" href="http://www.aalto.fi">Aalto website</a>.
    In RST you can also include images or files. The following image is taken from the internet, but you could include
    images located in your course folder.</p>`
    :raw-html:`<img alt="https://geekyshacklebolt.files.wordpress.com/2018/07/rest.jpg" class="img-responsive align-center"
    src="https://geekyshacklebolt.files.wordpress.com/2018/07/rest.jpg">`
    :raw-html:`<h2>Second Section</h2>`
    :raw-html:`<p>Lists can also be made in RST.</p>`
    :raw-html:`<ul class="simple"><li>Lists do not require much markup.</li><li>Create lists is intuitive.</li>
    <li>Notice the lack of markup compared to HTML</li></ul>`
    :raw-html:`<p>Almost everything that exists in HTML can also be produced with RST.</p>`

.. admonition:: :glyphicon-pencil:`\ ` Task
  :class: success

  Visit |ninja_website|, then copy and paste the :ref:`RST code snippet
  <rst-first-code-snippet>` and see how it looks like in a browser.

As you observed in the previous task, it is possible to use an online editor to create and visualise
*RST* files. However, the best thing you can do to create *RST* documents is to use a standalone
text editor on your computer. The :doc:`Text editors and integrated development environments
</set_up_environment/editors>` chapter has some recommendations about the best text editors and IDEs
for creating course content. Using the recommended IDEs help develop course content more efficiently
and make the experience of creating such courses more enjoyable and less error-prone.

.. rst-class:: pull-right

| :glyphicon-info-sign:`\ ` **Read more about** RST in the `official documentation
  <https://docutils.sourceforge.io/docs/ref/rst/introduction.html>`_

|

What is Sphinx?
---------------

`Sphinx <http://www.sphinx-doc.org/>`_ is a tool designed to create intelligent and elegant
documentation in software projects. However, the A+ team identified this tool's enormous potential
and decided to use Sphinx for creating smart, interactive, and robust courses at the university
level. The primary function of Sphinx within the A+ environment is to read the *RST* code and
produce HTML and `YAML <https://en.wikipedia.org/wiki/YAML>`_ files. The HTML files are used to
render the content of the courses in the browser, while the YAML files are used to set up different
exercises and external services/tools that are part of the course.

Directives and Roles
---------------------

.. _`directive-syntax`:

Directive
.........
Directives are used to build relatively complex elements within your documents, such as code blocks,
quotes, figures, and tables. The directive block consists of four main parts. The
**directive name**, the **directive argument**, the **directive options**, and the
**directive content**. The **directive name** as its name indicates is the name of the *RST*
directive. The **directive argument** is any text after the double colon. The argument sometimes has
some syntactical meaning, but it depends on the directive we are using. The **directive options**
are a predefined set of options that can be used to add some functionality to the directive itself.
Note that colons wrap each option, and if the option has arguments, there must be whitespace between
the trailing colon and the options argument. Finally, the **directive content** is any indented text
or another directive that complements the directive.

If you want to use directives, you must follow the next syntactical rules. Directives start with two
consecutive periods, followed by a whitespace, the name of the directive (directive type), and two
consecutive colons. The :ref:`example below <directive-code>` explains this syntax in more detail.

.. warning::
  * *RST* directives are case-insensitive
  * *RST* directives require blank lines between the paragraphs and the directives.

.. _directive-code:

:sub:`This code example shows the basic structure of an RST directive.`

.. annotated::

  .. code-block:: rst

    1«..»2« »3«sidebar»4«::»5« »6«Sidebar Title»
    7«  :subtitle:»8« Optional subtitle»
    7«  :class:»8« align-center»

      9«Subsequent indented lines comprise
      the body of the sidebar, and are
      interpreted as body elements.»

  .. annotation::

    All directives start with two consecutive periods.

  .. annotation::

    Whitespace between the two initial periods and the directive name.

  .. annotation::

    Directive name.

  .. annotation::

    Double colon.

  .. annotation::

    Whitespace between the double colon and the directive arguments.

  .. annotation::

    Directive arguments.

  .. annotation::

    Indented directive options.

  .. annotation::

    Option argument. (Notice that a whitespace is required between the option and the option's arguments)

  .. annotation::

    Indented directive content.

Role syntax
...........

Roles are also used to represent different elements within your document. However, roles do not have
the same complexity as the directive. In order to use a role, it is necessary to follow the
following syntax rules. Roles always start with a colon, followed by the role element, a colon, a
single backquote, the text and closing backquote. The :ref:`example below <role-code>` present this
syntax in more detail.

.. warning::
  * *RST* roles are case-insensitive
  * *RST* text inside the backquotes can no start or finish with whitespaces.

.. _role-code:

:sub:`This code example shows the basic structure of the RST role`

.. annotated::

  .. code-block:: rst

    The download role looks like follows 1«:»2«download»3«:»4«`»5«Any text </course_material/file.csv>»6«`»

    The mathematical formulas role looks like follows 1«:»2«math»3«:»4«`»5«a^2 + b^2 = c^2»6«`»

  .. annotation::

    Colon opening

  .. annotation::

    Role name

  .. annotation::

    Closing colon

  .. annotation::

    Back quote opening

  .. annotation::

    Role content

  .. annotation::

    Closing backquote


As you observed in the :ref:`example above <role-code>`, the directive block consists of the role
name, and role content. The role name is the name used to invoke the role, and the role content may
vary among roles, and therefore the documentation should be reviewed.

.. hint::

  It is always possible to `create custom roles <https://docutils.sourceforge.io/docs/ref/rst/directives.html#role>`_
  within your document.

.. _rst-benefits:

What are the benefits of RST and Sphinx?
----------------------------------------

Some of the most remarkable benefits of using *RST* are:

1. Writing *RST* code is much simpler than writing HTML.
2. *RST* allows producing LaTeX documents, PDF handouts, EPUB  content, slides and plain text files.
3. It is possible to create new `RST directives
   <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-directives>`_ and
   `RST roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#roles>`_.
4. Resulting HTML pages are automatically interlinked.
5. Authors can add customised CSS.
6. Automatic code highlighting for your code examples.

.. note::

  Thus far, the A+ team has developed a set of custom directives that can be easily integrated into
  the A+ courses. These directives are designed to support teaching and keep students engaged in the
  course. More information about the A+ directives can be found in the `A+ RST tools repository
  <https://github.com/apluslms/a-plus-rst-tools/blob/master/README.md>`_.

If you want to know more about *RST* and Sphinx, we recommend you to **Watch the following video**.

.. div:: embed-responsive embed-responsive-16by9

  .. youtube:: hM4I58TA72g
    :video-height: 432
    :video-width: 768

How should I read the reStructuredText official Documentation?
--------------------------------------------------------------

*RST* has two types of elements that are widely used to create *RST* documents. The first element is
known as `role <https://docutils.sourceforge.io/docs/ref/rst/roles.html>`_, while the second one is
known as `directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_. The official
*RST* documentation explains in great detail most of the roles and directives. However, if you do not
know how to read the official documentation, it may be rather difficult to take advantage of it.
Therefore, in this section, we will explain how to read the official documentation.

Directive
.........

As you can see, the image below shows the documentation of the sidebar directive. You can find the
official documentation in the `RST directives documentation
<https://docutils.sourceforge.io/docs/ref/rst/directives.html#sidebar>`_.

.. image:: /images/gallery/sidebar-directive.png
  :alt: sidebar directive.
  :width: 100%
  :align: center
  :class: img-thumbnail

The official documentation explains whether or not the directive arguments and the
directive options are required or optional. The documentation also includes a brief description of
the directive, and in most cases, it is possible to find a small example. If you want to review the
directive's appearance on an HTML page, remember that you can copy and paste the
example in |ninja_website| or use VS Code in conjunction with the `Aplus tools official extension
<https://marketplace.visualstudio.com/items?itemName=apluslms.aplus-tools-official>`_.

.. hint:: If you want to have custom directives in your course, you can create a GitHub
  issue and suggest your ideas to the A+ Team in the `Aplus-RST-Tools GitHub repository
  <https://git.io/JfYIX>`_. Of course, you can also create the directive and share it with the A+
  team.

Role
....

As you can see, the image below shows the documentation for the ``math`` role. You can find the
official documentation in the `RST roles documentation
<https://docutils.sourceforge.io/docs/ref/rst/roles.html#math>`_.

.. image:: /images/gallery/math-role.png
  :alt: Math role.
  :width: 100%
  :align: center
  :class: img-thumbnail

The documentation generally explains the roles and their syntax. It is also possible to find some
examples. The documentation also includes some customisations, but those are not relevant for the A+
users. Notice that, in this case, if you try to run the ``math`` example in |ninja_website|, the
online application does not recognise the role, and therefore, it is not possible to render the above
example in such a website. This is because the online tool does not have access to the Math library
required for rendering the ``math`` role.

Tips to start creating your course
----------------------------------

Before embarking on creating a course, the first step is to create an outline of the modules,
chapters, and sections. Once you have a proper structure is time to start typing some
content using *RST*. Remember that having a well-thought structure will make it easier to keep the
content of your course coherent. For example, the structure we created for the *RST Guide* module
consists of four chapters, and each chapter discusses specific topics.

#. :doc:`Get started <get_started>`: Introduction to *RST* and Sphinx
#. :doc:`Basic syntax <basic_syntax>`: The most basic *RST* directives and roles
#. :doc:`Extended syntax <extended_syntax>`: Advanced *RST* directives and roles, which are used to
   add complex material to the course.
#. :doc:`Additional resources <additional_resources_and_cheatsheet>`: List of resources that
   contains valuable information about the module topic.

After we planned the module, we proceeded to design a consistent structure for each chapter. The
following is the structure for most of the chapters.

- **Header:** Styled topic
- **Introduction:** Introduction (optional)
- **Content:**

  - Structural elements
  - Body elements
  - Inline elements

Each section inside the **Content** section is divided as follows:

#. Definition
#. Warnings
#. RST input + syntax
#. HTML output
#. Reference to the official documentation

As you can observe, we followed a precise and concise plan that helped us to keep the module
organised. Of course, our planning is not the only way of doing things, but we want to emphasise the
importance of planning before start writing your course content.

Another aspect to consider while creating the course is how you use **Docker**. When you are only
writing learning material that contains RST text, links and MathJax notation, you do not need to
stop the containers, then run the ``./docker-compile.sh`` and run ``./docker-up.sh`` again. In these
cases, you can solely run the ``./docker-compile.sh`` command, and your changes will be reflected
on the browser. However, if you add or remove *RST* files or edit *RST* exercises such as the Acos,
coding, Rubyric exercises or others, you will need to stop the docker containers, compile the course
and run the docker containers again.

Another trick to view the course is to use the :ref:`Aplus tools extension in VS Code
<vs-extensions>`. This extension might not render all the Aplus directives, but definitively, it
will help you to edit the content of your course and quickly visualise how those changes will render
in A+. The image below shows an example of how this feature works.

.. image:: /images/gifs/vscode-visualization.gif
  :width: 100%
  :align: center

|

The *Aplus tools* VS Code extension also contains a `set of snippets
<https://marketplace.visualstudio.com/items?itemName=apluslms.aplus-tools-official#aplus-tools-1>`_
that may help you to create the course content more efficiently and will help you to avoid syntax
errors when writing *RST*.

.. |ninja_website| raw:: html

   <a href="http://rst.ninjs.org/?theme=basic#" target="_blank">rst.ninja.org</a>
