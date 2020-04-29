.. The roles  should be created at the beginning of the document. Global roles can be created in the `global.rst` file

.. include:: /global.rst

.. Chapter content

Get Started
===========

:Author: Jhosimar Aguacia
:Date: |today|

.. styled-topic::
  
  Main questions:
  	What are RST and Sphinx?

  Topics:
    In this section, we will present the following topics:
    
    * `What is reStructuredText?`_
    * `What is Sphinx?`_
    * `What are the benefits of RST and Sphinx?`_
    * `Tips to start creating your course`_
  
  Requirements:
    #. You only need basic computing and programming skills, prior knowledge about markup languages might be beneficial.
    #. A basic environment setup, as detailed in :doc:`Module 2 </m02_setup/01_first_steps>`

  Estimated working time:
  	30 min.

::::

Introduction
------------

In this module, we will teach you from the most basic to the most advanced *RST* (reStructuredText) syntax needed to create a course in A+. It is important to understand that creating courses in A+ requires intermediate computing skills and an open-minded attitude towards this complex but valuable markup language called *RST*. Now, without further ado, let's start learning about *RST*. 

What is reStructuredText? 
-------------------------

*RST* is basically another :abbr:`markup language (A markup language is a computer language that uses tags to define elements within a document. It is human-readable, meaning markup files contain standard words, rather than typical programming syntax)`. Therefore, creating *RST* documents force you to follow a different workflow than you normally would when creating documents with traditional `WYSIWYG <https://en.wikipedia.org/wiki/WYSIWYG>`_ editors. 

As you can observe in the `code`_ below, *RST* makes use of symbols and keywords to add semantic to convey information about the meaning of some of the elements within the document. These symbols and keywords make part of the *RST* syntax, which will be cover in the next chapters of this module.

The advantage of authoring a course using *RST* is that different compilers can read the *RST* documents and therefore render the content in various formats, such as HTML, PDF, epub, and plain text. This flexibility is one of the :ref:`most significant advantages <rst-benefits>` of the *RST* markup language.

.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` Among the most popular *markup languages*, we have **Markdown**, **XML**, **LaTeX** and **HTML**.

| 

.. annotated::
  
  .. code-block:: rst
    :caption: This code example shows the basic structure of an RST document.
    :name: code
   
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

    This is a link to the 2«`Aalto website <http://www.aalto.fi>`». In RST you can also include images or files. 
    The following image is taken from the internet, but you could include images located in your course folder.

    .. image:: https://geekyshacklebolt.files.wordpress.com/2018/07/rest.jpg
      :align: center
      
    1«Second Section
    --------------»
    Also lists can be made in RST.
    3«- List do not required much markup.
    - Create lists is intuitive.
    - Notice the lack of markup compared to HTML»

    Almost everything that exists in HTML can also be produced with RST.  
  
  .. annotation::
  
    The "=, -, and ." symbols underline a sentence that will be render as a heading in the browser. 

  .. annotation::

    A link to the Aalto.fi website. 

  .. annotation::

    An unordered list of elements.

.. hidden-block:: get-started-example
  :label: Click here to see the HTML version of the code above.
  
  .. rst-class:: alert alert-success align-center 

  **HTML output** :glyphicon-print:`\ `

  .. div:: html-box

    :raw-html:`<h1>Chapter Title</h1>`
    :raw-html:`<h2>First Section</h2>`
    :raw-html:`<p>This is the first paragraph. It is tiny.</p>`
    :raw-html:`</br>`
    :raw-html:`<p>This is the second paragraph. Note that paragraphs can span multiple lines, but they are still rendered as one block after compilation. Italics and boldface are produced this way.</p>`
    :raw-html:`<h3>First Sub-Section¶</h3>`
    :raw-html:`<p>This is a link to the <a class="reference external" href="http://www.aalto.fi">Aalto website</a>. In RST you can also include images or files. The following image is taken from the internet, but you could include images located in your course folder.</p>`
    :raw-html:`<img alt="https://geekyshacklebolt.files.wordpress.com/2018/07/rest.jpg" class="align-center" src="https://geekyshacklebolt.files.wordpress.com/2018/07/rest.jpg">`
    :raw-html:`<h2>Second Section</h2>`    
    :raw-html:`<p>Also lists can be made in RST.</p>`
    :raw-html:`<ul class="simple"><li>List do not required much markup.</li><li>Create lists is intuitive.</li><li>Notice the lack of markup compared to HTML</li></ul>`
    :raw-html:`<p>Almost everything that exists in HTML can also be produced with RST.</p>`

If you have no experience using markup languages, it may be difficult for you to start creating *RST* documents. Nevertheless, the learning curve of the *RST* markup language is quite low, and once you start writing your first document, it will become easier to produce new content for your course. In addition, you can use this whole module as a boilerplate for the creation of your course.

.. admonition:: :glyphicon-tasks:`\ ` Task
  :class: success

  Visit `rst.ninja.org <http://rst.ninjs.org/?theme=nature#>`_, then copy and paste the `code`_ from above and observe how it looks like in a browser. 

As you could observe in the previous task, it is possible to use an online editor to create and visualise *RST* files. However, the best option for creating a proper *RST* document is using a standalone text editor on your computer. As you read in the :doc:`Module 2, VS Code chapter</m02_setup/04_vs_code>` of this manual, text editors and IDEs will help create the content of your courses much faster, and make the experience of creating such courses more enjoyable and less error-prone.

.. rst-class:: pull-right 

| :glyphicon-info-sign:`\ ` **Read more about**  `RST <https://docutils.sourceforge.io/docs/ref/rst/introduction.html>`_

|

What is Sphinx? 
---------------

`Sphinx <http://www.sphinx-doc.org/>`_ is a tool mainly used to create intelligent and well-styled documentation of software projects. However, the A+ team realised the enormous potential of this tool, and today, the A+ team uses Sphinx to create intelligent and dynamic courses. The primary responsibility of Sphinx is to read the *RST* files and produce HTML and `YAML <https://en.wikipedia.org/wiki/YAML>`_ files that will be used in the A+ ecosystem to configure, and set up the course and link the exercises of your course to an `automated grading tool <https://github.com/apluslms/mooc-grader>`_ which is part of the A+ ecosystem. 

Another advantage of Sphinx is that, it allows the user to extend the syntax of the *RST* language by creating new `RST directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-directives>`_ or `RST roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#roles>`_ which can be developed in Python. These directives are usually a markup block that works as extensions of the language. Thus far, the A+ team has developed a set of tailored directives that can be easily integrated inside the A+ courses. These directives provide instructors with robust educational tools that support teaching and keep students engage in the course. These directives also allow instructors to automated grading activities. More information about the tools can be find in the repository called `A+ RST tools <https://github.com/Aalto-LeTech/a-plus-rst-tools/blob/master/README.md>`_, and also in the :doc:`Chapter 3.4 of this manual <04_aplus_syntax>`.

.. _rst-benefits:

What are the benefits of RST and Sphinx?
----------------------------------------

Using *RST* has some benefit in the creation of course content. The most remarkable benefits are:


.. rst-class:: list-group

  :list-item:`1. The RST code is much simpler than HTML.`
  :list-item:`2. The possibility to produce also LaTeX documents, PDF handouts, epub  content, and plain text files from the same source code.`
  :list-item:`3. It is possible to write new "RST commands" (called Sphinx directives for any kind of material.`
  :list-item:`4. Resulting HTML pages are automatically interlinked.`
  :list-item:`5. Custom web page styling can be used with CSS.`
  :list-item:`6. Automatic code highlighting for your code examples.`
  :list-item:`7. Using RST and Sphinx gives you the possibility to create new RST directives and create different visualizations of the content in your course.`


:important:`The video below` explains pretty well what *RST* and Sphinx are, and it will help you to understand how *RST* and Sphinx work under the hood.

.. div:: embed-responsive embed-responsive-16by9
  
  .. youtube:: hM4I58TA72g
    :video-height: 432
    :video-width: 768

How to read the reStructuredText official Documentation.
--------------------------------------------------------

*RST* has mainly two types of elements that are widely used to create semantic documents in *RST*. One of the elements is named `role <https://docutils.sourceforge.io/docs/ref/rst/roles.html>`_, and the other one is named `directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_. The official *RST* documentation explain in great detail all the roles and directives. However, if you do not know how to read this documentation, it will be difficult to take advantage of the *RST* language. Therefore, we will briefly explain how to read the official documentation. 

.. _`directive-syntax`:

Directive syntax
................

.. sidebar:: :glyphicon-info-sign:`\ ` VSCode snippets 

  Remember that the A+ team has an VS Code extension that contains a set of snippets which help to create course content more efficiently and will help you to avoid syntax errors when writing *RST*.

Directives are used to represent different elements within your documents, such as code blocks, quotes, figures, and tables. In order to use a directive, it is necessary to follow some specific syntax rule: directives start with two consecutive periods ``..``, followed by one whitespace, the name of the directive (directive type), a double colon, and finally one whitespace. It seems cumbersome, but once you get used to the syntax, it will become easier. The :ref:`example below <directive-code>` will explain this syntax in more detail.

.. warning:: 
  * *RST* directives are case-insensitive
  * *RST* directives require blank lines between the paragraphs and the directives.

.. _directive-code:

:sub:`This code example shows the basic structure of a RST directive`

.. annotated::
  
  .. code-block:: rst

    1«..»2« »3«sidebar»4«::»5« »6«Sidebar Title»
    7«  :subtitle:»8« Optional subtitle»
    7«  :class:»8« align-center»

      9«Subsequent indented lines comprise
      the body of the sidebar, and are
      interpreted as body elements.»
    
  .. annotation::
  
    Explicit markup start.

  .. annotation::

    Whitespace between the markup start and the directive type.

  .. annotation::

    Directive type.
  
  .. annotation::

    Double colon. 
  
  .. annotation::

    Whitespace between the double colon and the directive arguments.
  
  .. annotation::

    Directive arguments.
  
  .. annotation::

    Indented directive options.
  
  .. annotation::

    Option argument. (Notice that whitespace is required between the option and the option arguments)
  
  .. annotation::

    Indented directive content. 

As you observed in the :ref:`example above <directive-code>`, the directive block consists of the directive name, directive arguments, directive options and directive content. The directive name is the define directive name define by *RST*, the directive argument is any text after the double colon, the directive options are a set of predefined indented options which vary among directives. Notice that colon marks wrap each option, and if the option has arguments, there should be whitespace between the colon and the options argument. Finally, the directive content is any indented text that complies with the directive rules. 

As you can see, the image below shows the sidebar documentation that can be found in the `RST documentation <https://docutils.sourceforge.io/docs/ref/rst/directives.html#sidebar>`_. This piece of text explains whether or not the directive arguments and the directive options are required or optional. The documentation also includes a brief description of the directive, and most of the time, it is possible to find a small example. If you want to quickly review the appearance of the directive in a HTML page, remember that you can copy and paste the example in the `rst.ninja.org <http://rst.ninjs.org/?theme=nature#>`_ website.

.. image:: /images/gallery/sidebar-directive.png
  :alt: sidebar directive.
  :width: 100%
  :align: center
  :class: img-thumbnail

.. hint:: If you would like to have specific directives in your course, you can always suggest them to the A+ Team in the `Aplus-RST-Tools GitHub repository <https://git.io/JfYIX>`_.

Role syntax
...........

Roles are also used to represent different elements within your documents, such as mathematical formulas, text highlight, references, and downloads. In order to use a role, it is necessary to follow specific syntax rules: roles always start with a colon, followed by the role element, a colon, a single backquote, the text and closing backquote. The :ref:`example below <role-code>` present this syntax in more detail.

.. warning:: 
  * *RST* roles are case-insensitive
  * *RST* text inside the backquotes can no start or finish with whitespaces.

.. annotated::
  
  .. code-block:: rst
    :caption: This code example shows the basic structure of the RST role
    :name: role-code

    The download role -> 1«:»2«download»3«:»4«`»5«Any text </course_material/file.csv>»6«`»
    The mathematical formulas role -> 1«:»2«math»3«:»4«`»5«a^2 + b^2 = c^2»6«`» 
  
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

As you observed in the :ref:`example above <role-code>`, the directive block consists of the role name, and role content. The role name is the name of the role that has been already defined in the *RST* syntax. The role content varies among roles, and therefore the documentation should be reviewed. 

.. hint:: 

  It is always possible to `create custom roles <https://docutils.sourceforge.io/docs/ref/rst/directives.html#role>`_ within your document.

As you can see, the image below shows the ``math`` documentation that can be found in the `RST documentation <https://docutils.sourceforge.io/docs/ref/rst/roles.html#math>`_. This piece of text explains the roles, and sometimes it includes some examples. The documentation also includes some customisation arguments, but those are not relevant for the a+ users. Notice that, in this case, `rst.ninja.org <http://rst.ninjs.org/?theme=nature#>`_ website does not recognise the roles, and therefore, it is not possible to render the above example in such a website.

.. image:: /images/gallery/math-role.png
  :alt: Math role.
  :width: 100%
  :align: center
  :class: img-thumbnail

Tips to start creating your course
----------------------------------

The first step before jumping on the creation of a course is to create a sketch a proper structure of the module, chapters and sections. Once you have a proper structure is time to start typing some content using *RST*. Remember that having a well-thought structure will make easier to keep the content of your course coherent. For example, the structure we created to *RST Guide* module have 7 Chapters, and each chapter will discuss specific topics.

#. Get started: Introduction to *RST* and Sphinx
#. Basic syntax: The most basic *RST* directives and roles
#. Extended syntax: Advanced *RST* directives and roles which are used to add complex material to the course.
#. Aplus syntax: List of directives developed under the Aplus-rst-tools project
#. Cheatsheet: A Cheatsheet with the official *RST* elements
#. Styling: How to style your course.
#. Additional resources: List of resources that contains valuable information about the module topic.

After, we planned the module; we proceeded to design a consistent structure for each Chapter. The following, is the structure for most of the chapters in this module (especially chapter 3.2, 3.3 and 3.4); however, some modules required some changes.

- :important:`Header:` Styled topic
- :important:`Introduction:` Introduction (optional)
- :important:`Content:` 
    - Structural elements
    - Body elements
    - Inline elements

Each of the content sections is divided as follows:

#. Definition
#. Warnings
#. RST input + syntax
#. HTML output
#. Reference to the official documentation

As you can observe, we followed a precise and really concise plan, that helped us to keep the module organise. Of course, our planning is not the only way of doing things, but we want to emphasise the importance of planning before start writing nonsense text.

Another aspect to take into account while creating the course is the way you make use of the docker utilities provided by in the `course template <https://git.io/JfY3N>`_. When you are only writing learning material that contain text, links and MathJax notation, you don't need to run the "docker-compile - docker-up" cycle for each modification. This is only required if you add new *RST* files or exercises. One can just start A+ and mooc-grader with ``docker-up.sh``. After that, one can just edit an *RST* file, run ``docker-compile.sh`` and the update the course page in the web browser. This cycle can be repeated without shutting down docker-up.sh.

Another trick is that one does not even need to start A+ to see the HTML version
of the *RST* material. The compiled material is in the subdirectory
``_build/html``, which you can view with your web browser.

For example, print your working directory in the terminal with the ``pwd``
command:

.. code-block:: shell

    atilante@t31300-lr124 ~/ohj/a-ole/aplus-manual
     % pwd
    /u/79/atilante/unix/ohj/a-ole/aplus-manual

In the example above, the absolute path of the working directory is ``/u/79/atilante/unix/ohj/a-ole/aplus-manual``. Copy-paste your result to
the address bar of your web browser, add ``_build/html/index.html`` to the end
and press Enter.

.. image:: /images/_build-html-in-browser.png
  :width: 100%
  :align: center

|

Notice that images and exercises do not show when viewing this static HTML material in the browser. Nevertheless, it is also possible to quickly visualise the HTML version of the document you are working on by using the :ref:`reStructuredText extension in VS Code <vs-extensions>`. This extension might not be render all the Aplus directives, but definitively, it will help you to make small changes without having to compile the whole project. The image below show an example on how long does it take to visualize changes in the text.

.. image:: /images/gifs/vscode-visualization.gif
  :width: 100%
  :align: center

 
