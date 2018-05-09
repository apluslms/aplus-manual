Customising course pages
========================

The visual outlook and layout of the course pages can be altered.
This requires basic knowledge of
`HTML <https://www.w3schools.com/html/default.asp>`_ and
`CSS <https://www.w3schools.com/css/default.asp>`_.

Configuring the CSS file for use
--------------------------------

First, create a CSS file. In this example it is
``_static/default.css``. If the directory ``_static`` does not
exist, you must create it. We will come to writing the contents of
this file a little bit later.

Second, link to the CSS file in ``_templates/layout.html``.
Currently the file looks like this:

.. code-block:: none

    {% extends "aplus/layout.html" %}

    {% block extrahead %}

    <!--  MathJax (LaTex math) -->
    <script type="text/javascript" async
             src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"
             data-aplus>
    </script>

    <!-- Custom course styles -->
    <link rel="stylesheet"
          href="{{ pathto('_static/course.css', 1) }}"
          type="text/css"
          data-aplus />

    {% endblock %}

This is a *template file* for Sphinx. It contains pieces of HTML code
that will be inserted on each HTML page when Sphinx compiles the RST files.
All commands between tags ``{%`` and ``%}`` are information for Sphinx:
where should this piece of HTML to be put? Currently there are two extra
things: we will define that we will include the MathJax JavaScript library
from the Internet and use style directives from file ``_static/course.css``
inside the main directory of the course.

Third, make sure that file ``conf.py`` contains the following line
uncommented (without the ``#`` character).

.. code-block:: none

    html_static_path = ['_static']
    templates_path = ['_templates']

This tells Sphinx that there are two special directories. First, there
is a *static* directory, which holds files that are required for the RST
compilation but which itself do not change during the compilation.
Second, there is the directory for templates, which contain extra HTML
code as described.

Contents of the CSS file
------------------------

After compiling the course, open the files
``_build/html/m02/chapter01.html`` and ``_static/course.css``
in a text editor.

Here is the original ``admonition`` block from file
``m02/chapter01.rst`` :

.. code-block:: rst

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


Here is the corresponding result in HTML:

.. code-block:: html

    <div class="meta admonition">
    <p class="first admonition-title">Algorithm</p>
    <p>An <em>algorithm</em> is a finite sequence of unambiguous instructions, which
    each can be executed with finite amount of work and which together
    compute function</p>
    <p class="last"><span class="math">\(f: I \to O\)</span>, where
    <span class="math">\(I\)</span> is the input set,
    <span class="math">\(O\)</span> is the output set,
    <span class="math">\(\forall i \in I\)</span>, the algorithm will stop in a way that
    <span class="math">\(o = f(i) \in O\)</span></p>
    </div>

Moreover, our CSS file has some custom settings for the ``admonition``
directive:

.. code-block:: css

    .admonition, .topic {
      min-height: 42px;
      padding: 15px;
      margin-bottom: 20px;
      border: 1px solid transparent;
      border-radius: 4px;
      margin-left: 0em;
      margin-right: 0em;
      margin-top: 15px;
    }

    .admonition button {
      margin-bottom: 5px;
    }

    .admonition .collapse .well,
    .admonition .collapsing .well {
      margin-bottom: 0;
    }

    .admonition-title, .topic-title {
      font-weight: 700;
    }

    /* some parts cropped out */

    .admonition, .topic {
      /* default colors */
      color: #31708f;
      background-color: #d9edf7;
      border-color: #bce8f1;
    }

As you can see, Sphinx directives produce HTML ``<div>`` elements which have
a CSS class that corrensponds the name of the Sphinx directive. The different
blocks inside directives may have additional classes, like the
``admonition-title`` here. You can always compile the RST to HTML, look at
the produced HTML code and write corresponding CSS where needed.

Note that if you edit CSS files at directory ``_static``, you must
recompile the course, restart A+ and refresh the page in the web browser -
the same way when you edit RST files and want to see the result.
One ``can`` also modify CSS files at directory ``_build/html_static`` and see
the results immediately, but that is not wise, because those changes have to
be copied to ``_static`` before recompiling the course! For faster CSS design
one might want to try the `Firefox Developer Edition
<https://www.mozilla.org/en-US/firefox/developer/>`_ which has builtin
CSS editor. 
