Developing course material using reStructuredText (RST)
=======================================================

.. styled-topic::

  Main questions:
      What is RST? How to utilize RST-tools?

  Topics?
      RST, text editor, bootstrap-styled-topic, admonition, ...

  What you are supposed to do?
      If you have already installed aplus-manual, these features
      should work just ok. However, there are also instructions
      how to utilize them in other courses.

  Difficulty:
      You might need to edit the course config files.

  Laboriousness:
      A couple of hours for getting to know a little RST and installing a
      text editor.

In this chapter, we will take a look at different RST features, which allow you
to develop course material.  We will focus mostly on custom RST directives,
developed specifically for A+ course material.  The material will be compiled
using *Sphinx*, so all builtin Sphinx extensions are also available.

What is RST and why is it used on A+
------------------------------------

.. admonition:: File format: RST
  :class: meta

  RST (reStructured Text) is a human-friendly text file format.
  It has markup for text formatting (headers, paragraphs, italics)
  and hyperlinks and is thus similar to HTML for web pages. RST documents
  can also include images, videos and exercises. The filename suffix
  for RST is ``.rst``.

Here is a simple example of RST source code:

.. code-block:: none

    Heading
    =======

    Level 2 heading
    ---------------

    This is the first paragraph. It is tiny.

    This is the second paragraph. Note that paragraphs can span multiple
    lines, but they are still rendered as one block after compilation.
    *Italics* and **boldface** are produced this way.

    `This is a hyperlink <http://www.aalto.fi>`_ which becomes also a hyperlink
    in the final HTML version.

    Another level 2 heading
    -----------------------

    - also lists can be made
    - and they are very intuitive
    - notice the lack of markup compared to HTML

    Almost everything that exists in HTML can also be produced with RST.

There are many tutorials on how to write RST. Here are just some.

- http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
- http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. admonition:: Software: Sphinx
  :class: meta

  `Sphinx <http://www.sphinx-doc.org/>`_ is a software which reads RST files
  and produces HTML and YAML files which are used in A+. Sphinx is written in
  the Python programming language. Originally it is meant for making easily
  documentation (help files, tutorials) for software. The benefit of Sphinx
  is that new RST commands, called Sphinx directives, can be written in
  Python. All A+ courses use package *A+ RST tools* which produce things
  specific for A+. Each course can also contain its own Sphinx directives,
  if some specific layout or type of exercise is needed.

  YAML files will be discussed later.


The benefits of writing course material in RST are:

- the RST code is much simpler than HTML
- the possibility to produce also LaTeX documents (PDF handouts) from the same source
- it is possible to write new "RST commands" (called Sphinx directives)
  for any kind of material
- resulting HTML pages are automatically interlinked
- one can use HTML templates to easily make many similar HTML pages
- of course, custom web page styling can still be used with CSS

Workflow for editing RST files
------------------------------

.. image:: /images/atom.png

.. admonition:: Software: text editor
  :class: alert alert-info

  To edit the files in the course directory, like the RST files, you will need
  a software called *text editor*. This is an application which shows
  the contents of the files as text with monospaced font (all characters have
  equal height and width). In the picture above is the Atom text editor
  showing file ``m01_introduction/01_rst.rst`` of this course. As you
  can see, it is nice, because it shows line numbers and colors different
  parts of the RST code. This is called `syntax highlighting`.

  For GNU/Linux environment, some simple editors are
  `Kate <https://kate-editor.org/>`_, Mousepad included in the
  `Xfce Desktop Environment <https://xfce.org/>`_ and
  `Gedit <https://wiki.gnome.org/Apps/Gedit>`_.
  `Notepad++ <https://notepad-plus-plus.org/>`_ is similar to these in
  the Windows environment.

  An advanced, modern editor is `Atom <https://atom.io/>`_, shown
  in the picture above. Two classic editors with lots of features for
  programmers are `Emacs <https://en.wikipedia.org/wiki/Emacs>`_ and
  `Vim <https://en.wikipedia.org/wiki/Vim_(text_editor)>`_, but those
  also have high learning curve.

  Do **not** use word processors such as Microsoft Word or LibreOffice
  Writer. Their formatting commands are useless when one must edit pure
  text files.

  It is good to learn how to use your text editor: commenting multiple
  lines, changing indentation of multiple lines, show line numbers,
  search and replace.


The usual workflow for editing a course is the following:

1. Open your text editor, a terminal and a web browser.
2. Edit some RST files in your text editor.
3. Give command ``./docker-compile.sh`` in the terminal.
4. Give command ``./docker-up.sh`` in the terminal.
5. Go to ``http://localhost:8000/`` in the web browser to view A+
   running on your machine.
6. Examine the changes you made in A+.
7. Press ``Q`` or ``Ctrl+C`` in the terminal.
8. Go to step 2 if you wish to continue editing.
9. Give command ``git add -u`` in the terminal to mark all changed files to be
   added into your local git repository.
10. Give command ``git commit -m "message"`` in terminal. Replace
    ``message`` with short description (preferably less than 60 characters)
    on what you have done.
11. Remember also to say ``git push`` a couple of times in a day.
    This copies your updates to the course material to the Gitlab server
    ``version.aalto.fi``.

Steps 9-11 are explained later when discussing what is `git`.

Exercise: editing an RST file
.............................

Edit this RST file. Try to write RST code that produces content similar
to this image:

.. image:: /images/rst-sample.png


A+ RST tools
------------
There are Sphinx extensions made for writing course material on A+. The
name of this extension collection is *A+ RST tools*.




Bootstrap-styled-topic
......................

The ``styled-topic`` feature seen above generates a description list wrapped in
a ``div``-element with additional styling.

* Implementation: ``extensions/bootstrap_styled_topic.py``
* Styles: ``_static/course.css``


Adding custom RST directives
............................

Custom RST directives can be added into the ``extensions`` directory.
The name of the implementing Python module should also be added to the ``extensions`` list in the Sphinx configuration file ``conf.py``.
See for example ``bootstrap_styled_topic`` and ``div``.

Admonition with embedded MathJax-syntax
.......................................

Builtin ``admonition`` directive is useful for defining new concepts:

.. admonition:: Algorithm
  :class: meta

  An *algorithm* is a finite sequence of unambiguous instructions, which
  each can be executed with finite amount of work and which together
  compute function

  :math:`f: I \to O`, where
  :math:`I` is the input set,
  :math:`O` is the output set,
  :math:`\forall i \in I`, the algorithm will stop in a way that
  :math:`o = f(i) \in O`

Math formulas are rendered with the `MathJax`_ JavaScript library.
Custom JavaScript can be added into the course layout template found in ``_templates/layout.html``.
This template extends the default A+ theme found in ``a-plus-rst-tools/theme/aplus/layout.html``.

.. _MathJax: https://docs.mathjax.org/en/v2.7-latest/

Tips
....

When you are only writing learning material as RST which contains text, links
and MathJax notation, you don't need to start A+ to see the results. The
compiled material is in the subdirectory ``_data/html``, which you can view
with your web browser.

For example, print your working directory in the terminal with the ``pwd``
command:

.. code-block: none

    atilante@t31300-lr124 ~/ohj/a-ole/aplus-manual
     % pwd
    /u/79/atilante/unix/ohj/a-ole/aplus-manual

In this example the absolute path of the working directory is
``/u/79/atilante/unix/ohj/a-ole/aplus-manual``. Copy-paste your result to
the address bar of your web browser, add ``_build/html/index.html`` to the end
and press Enter.

.. image:: /images/_build-html-in-browser.png

Notice that images and exercises do not work with this method.
