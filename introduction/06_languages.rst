Multilingual course (i18n)
==========================


.. styled-topic::

  Main questions:
      How to create a course that is available in multiple human languages?

  Topics?
      RST, A-plus RST tools

  Difficulty:
      You need to first master course creation in one language.
      Technically, there are no additional difficulties in multiple languages.


This chapter describes the document structure and compilation for including
course material in multiple human languages (implementing exercises in multiple
programming languages is a different challenge).
This approach is recommended for courses that aim to
use identical study units and grading in all language versions.


Structure
---------

The different language versions reside in a single git repository
as adjacent RST trees.
Each language has its own RST index that works the same as in a
single language course. It lists the course modules for one language
in a toctree-directive.
In a multilingual course, there is an additional multilingual super index
that lists the languages of the course.
A multilingual RST index may look like this:

.. code-block:: none

    Ignored course title
    ====================

    .. toctree::
      :maxdepth: 1
      :caption: Select language

      Finnish <index_fi>
      English <index_en>

The above index includes a title, maximum tree depth, and link names so that it
compiles into sensible HTML for non A-plus use.
However, the only A-plus requirements are that the index includes
a **toctree** that has the option **:caption: Select language**.

The links are to the the different RST language indexes that must include
the course title and the toctree of the course modules in that language.
Furthermore, the RST file names must have a language postfix (such as **_en**).
The first language is considered the **default language** of the course.
The default language is selected if an A-plus student has not selected
another supported language as her or his preference.

.. admonition:: Content constraints
  :class: warning

  Each language must have an identical number of modules,
  identical number of chapters in each module,
  and exercises in each chapter that have identical keys.
  Furthermore the visibility, point, and group configuration
  must be identical to default language
  or omitted completely to use implicit defaults.

  In other words, each language must have the same content entries
  that provide the same course points.
  If the internationalization design breaks these constraints
  then A-plus project recommends to create separate course instances
  for the different internationalizations.


Compilation
-----------

The A+ RST tools detects a multilingual course and compiles it accordingly.
Near the end of the RST compilation the tools should log similarly to:

.. code-block:: none

  Detected language tree.
  Traverse document elements to write configuration index (fi).
  Traverse document elements to write configuration index (en).
  Joining language tree to one index.

.. admonition:: Git submodule
  :class: sidebar

  To check the current submodule version change into the submodule directory,
  e.g. :code:`cd a-plus-rst-tools` and see :code:`git status`.
  The latest version of the submodule is generally available via
  :code:`git checkout master && git pull`.
  To save the currently checked out submodule version
  return to the parent repository and stage the change,
  e.g. :code:`cd .. && git add a-plus-rst-tools`.
  Then create a commit and push it to the remote repository.

If the previous log lines for your languages do not appear, check the following:

* Course submodule :code:`a-plus-rst-tools` is a recent version that supports languages
* Multilingual index has the :code:`toctree` option :code:`:caption: Select language**`
* In :code:`conf.py` variable :code:`master_doc` is set to your multilingual index RST file

While joining languages the compilation halts in an error
if any previously mentioned course constraints are broken.
In the development stage it can be useful to include
:code:`conf.py` variable :code:`skip_language_inconsistencies = True`.
That flag enables compilation of broken constraints.
Warnings are generated that help to fix any inconsistencies
and the compiled course represents default language where problems exist.


Recap
-----

.. questionnaire:: 1 2
  :title: Multilingual course recap

  .. pick-one:: 1

    How does A-plus RST tools recognize a multilingual course?

    a. Course includes multiple RST indexes
    b. Course includes RST file postfixes, e.g. :code:`document_en.rst`
    *c. Course includes RST index with :code:`:caption: Select language`

    a § A separate RST index for each language is required. However, they are not found automatically.
    b § Language indexes must be postfixed to identify the language when processed. However, the indexes are not found automatically.
    c § Correct, a specific language index must be created that links to index of each available language.

  .. pick-any:: 1

    Which of the following scenarios break the language content constraints?

    *a. Course has 3 modules in English and 2 in Spanish.
    *b. Course skips one text only chapter in English that exists in the default Finnish variation.
    *c. Course defines 3 points exercise in English and 4 point exercise in Chinese in the corresponding chapter using the same exercise key.
    d. Course defines 3 points exercise in default language English and does not configure points for the corresponding exercise in Chinese.
    *e. Course supports larger groups in the default language exercises than in Finnish that has presumably less students.

    d § Some configurations can be omitted in favor of implicit values from the default language.
    !e § A-plus does not support alternative limits based on language.
