Developing course material using reStructuredText (RST)
=======================================================

.. styled-topic::

  Main questions:
      How to utilize RST-tools

  Topics?
      bootstrap-styled-topic, admonition, ...

  What you are supposed to do?
      If you have already installed aplus-manual, these features
      should work just ok. However, there are also instructions
      how to utilize them in other courses.

  Difficulty:
      You might need to edit the course config files.

  Laboriousness:
      Installation might take a couple of hours.

In this chapter, we will take a look at different RST features, which allow you to develop course material.
We will focus mostly on custom RST directives, developed specifically for A+ course material.
The material will be compiled using `Sphinx`_, so all builtin Sphinx extensions are also available.
Here is one tutorial on how to write RST, although many others probably exist: http://docutils.sourceforge.net/docs/user/rst/quickref.html


Bootstrap-styled-topic
----------------------

The ``styled-topic`` feature seen above generates a description list wrapped in a ``div``-element with additional styling.

* Implementation: ``extensions/bootstrap_styled_topic.py``
* Styles: ``_static/course.css``


Adding custom RST directives
----------------------------

Custom RST directives can be added into the ``extensions`` directory.
New extensions should be also be added the name of the implementing Python module in the ``extensions`` list in the Sphinx configuration file ``conf.py``.
See for example ``bootstrap_styled_topic`` and ``div``.

Admonition with embedded MathJax-syntax
---------------------------------------

Builtin ``admonition`` directive with ``:math:`` elements:

.. admonition:: Algoritmi
  :class: meta

  Algoritmi on äärellinen jono yksikäsitteisiä, äärellisellä työllä suoritettavissa olevia käskyjä, jotka laskevat funktion

  :math:`f: I \to O`, jossa
  :math:`I` on syötejoukko,
  :math:`O` on tulosjoukko ja
  :math:`\forall i \in I`, algoritmi pysähtyy s.e., :math:`o = f(i) \in O`

Math formulas are rendered with the `MathJax`_ JavaScript library.
Custom JavaScript can be added into the course layout template found in ``_templates/layout.html``.
This template extends the default A+ theme found in ``a-plus-rst-tools/theme/aplus/layout.html``.

.. _MathJax: https://docs.mathjax.org/en/v2.7-latest/
.. _Sphinx: http://www.sphinx-doc.org/en/1.6/

