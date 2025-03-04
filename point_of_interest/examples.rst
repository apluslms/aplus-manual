Point of Interest - Examples
============================

.. styled-topic::

  Main questions:
      Learn how to use POI directives and most of the options.

  Topics?
      Various examples of POI directives.

  Difficulty:
      Difficult

  Laboriousness:
      May take up to 1 to 2 hours if you take a good look and try to understand what is happening in the examples.

This chapter provides some examples that anyone can use as a starting point for creating their own content.


Simple POI
----------

.. code-block:: none

    .. point-of-interest:: Here is title

      This is very basic POI and it does not have any options in it.

This is how it looks.

.. point-of-interest:: Here is title

  This is very basic POI and it does not have any options in it.

POI options
-----------

Here are all POI options listed with descriptions. None of the options are mandatory.

.. code-block:: none

    :id: unique id, if not supplied a random id will be generated. Use alphanumeric IDs.
    :previous: id of previous point-of-interest (optional)
    :next: id of next point-of-interest (optional)
    :hidden: (if this flag is present, the content of this poi is hidden by default)
    :class: any additional css classes
    :height: fixed height in pixels
    :bgimg: path to background image
    :columns: used with newcol to set relative widths of poi content columns (e.e. 2 3 3) DEPRECATED
    :not_in_slides: a flag used with the presentation maker. This POI does not show in the slides if this is defined.
    :not_in_book: If this flag is given, this POI does not appear in the A+ content chapter.
    :no_poi_box: Removes surrounding box and navigation


Linking POI with another
------------------------

POI ids are used to link POI together. Each POI has next and previous links on the top of the POI to enable easy navigation between linked POI.

If you want to link POI 1, POI 2 and POI 3 you will need to set ids for the each POI and set next and previous options for the POI in order to get the links working.

Next option should be used only if the next occurrence of point of interest has been created. Same applies to the previous option vice versa. But remember that linking POI with next and previous options is not mandatory.

Here is how you do it.

.. code-block:: none

    .. point-of-interest:: POI 1 title
      :id: first
      :next: second

      This is POI 1. It has link to the next POI with id of 2.

    .. point-of-interest:: POI 2 title
      :id: second
      :previous: first
      :next: third

      This POI is linked to the POI 1 with the previous option which has the id of the previous POI. In this case it is 1. Next works the same way.

    .. point-of-interest:: POI 3 title
      :id: third
      :previous: second

      This POI is linked to the POI 2.

**Result**

.. point-of-interest:: POI 1 title
  :id: first
  :next: second

  This is POI 1. It has link to the next POI with id of 2.

.. point-of-interest:: POI 2 title
  :id: second
  :previous: first
  :next: third

  This POI is linked to the POI 1 with the previous option which has the id of the previous POI. In this case it is 1. Next works the same way.

.. point-of-interest:: POI 3 title
  :id: third
  :previous: second

  This POI is linked to the POI 2.

.. admonition:: Possible issues with linking
  :class: alert alert-info

  If you *use only numeric values* in the `id`, `previous` and `next` option fields, links between POI may not work. Try to replace `id`, `previous` and `next` options with **unique alphanumeric values.**

POI with columns
----------------

Columns can have two options `width` and `column-class`.

**Width** can be set to any value from 1 to 12, with 12 representing the full width of the available space. These values are relative widths.

**column-class** can contain any Bootstrap classes. You can, for example, set background color, add padding, or align text.

To find out more about the available classes, see Bootstrap 5 documentation for example on:
  - `Background colors <https://getbootstrap.com/docs/5.2/helpers/color-background/>`_.
  - `Columns <https://getbootstrap.com/docs/5.2/layout/columns/>`_.
  - `Spacing <https://getbootstrap.com/docs/5.2/utilities/spacing/>`_.

You can see some use cases in the examples below.

**Note**: with Bootstrap 5, you are no longer required to explicitly specify the width for each column. However, if the content does not fit into the cells in a row, some columns will flow into the next row. If this is not acceptable, you still need to specify the width of each column. In very narrow screens (xs), columns are always collapsed into one.

**POI with two columns**

.. code-block:: none

  .. point-of-interest:: POI with two columns

      .. row::

        .. column::
          :column-class: bg-warning-subtle p-3 text-center

          The first row has only one column (without a width definition), so it gets a width of 12 relative units (100%). It has background color set to bg-warning-subtle (orange), medium padding (p-3 = 1rem by default in Bootstrap). Text is centered.

      .. row::

        .. column::
          :column-class: text-bg-light p-3 text-center

          .. math::

            (a + b)^2 = a^2 + 2ab + b^2

            (a - b)^2 = a^2 - 2ab + b^2

        .. column::
          :column-class: p-3 text-center

          This second row is split evenly between two columns. You do not need to enter explicit widths when all the columns in the row are the same width, but do note that columns may flow into the next row if the content does not fit.

**Result**

.. point-of-interest:: POI with two columns

    .. row::

      .. column::
        :column-class: bg-warning-subtle p-3 text-center

        The first row has only one column (without a width definition), so it gets a width of 12 relative units (100%). It has background color set to bg-warning-subtle (orange), medium padding (p-3 = 1rem by default in Bootstrap). Text is centered.

    .. row::

      .. column::
        :column-class: text-bg-light p-3 text-center

        .. math::

          (a + b)^2 = a^2 + 2ab + b^2

          (a - b)^2 = a^2 - 2ab + b^2

      .. column::
        :column-class: p-3 text-center

        This second row is split evenly between two columns. You do not need to enter explicit widths when all the columns in the row are the same width, but do note that columns may flow into the next row if the content does not fit.


**POI with nested columns and uneven widths**

.. code-block:: none

  .. point-of-interest:: Making nested columns

    .. row::

      .. column::
        :width: 8
        :column-class: bg-warning-subtle pt-3 pl-3 pr-3 pb-1 text-center

        This column has a width of 8/12. It has medium padding (3) on each side, but only a very small (1) padding in the bottom to illustrate how the nested row is contained by it. Be careful with the RST indentation.

        .. row::

            .. column::
              :width: 5
              :column-class: text-bg-light p-2

              This column in a nested row has a width of 5/12, and a small padding (p-2)

            .. column::
              :width: 7
              :column-class: text-bg-secondary p-5

              This column in a nested row has a width of 7/12, and a very large padding (p-5).

      .. column::
        :width: 4
        :column-class:

        This first row is split between two columns. The first column has a width of 8/12, and this one has 4/12.

**Result**

.. point-of-interest:: Making nested rows/columns with uneven widths

  .. row::

    .. column::
      :width: 8
      :column-class: bg-warning-subtle pt-3 pl-3 pr-3 pb-1 text-center

      This column has a width of 8/12. It has medium padding (3) on each side, but only a very small (1) padding in the bottom to illustrate how the nested row is contained by it. Be careful with the RST indentation.

      .. row::

          .. column::
            :width: 5
            :column-class: text-bg-light p-2

            This column in a nested row has a width of 5/12, and a small padding (p-2)

          .. column::
            :width: 7
            :column-class: text-bg-secondary p-5

            This column in a nested row has a width of 7/12, and a very large padding (p-5).

    .. column::
      :width: 4
      :column-class:

      This first row is split between two columns. The first column has a width of 8/12, and this one has 4/12.


**POI with multiple rows and columns**

.. code-block:: none

  .. point-of-interest:: Testing column widths

    .. row::

      .. column::
        :column-class: bg-warning-subtle text-center

        See how width of 12 is separated between columns on the same row. Note how the "width of 1" columns overflow when making the browser window more narrow. To prevent this, set each column width explicitly.

    .. row::

      .. column::
        :column-class: text-bg-light text-center

        This column has width of 6.

      .. column::
        :column-class: text-bg-secondary text-center

        This column also has width of 6.
        See again how width is spread with columns 6 + 6 = 12

    .. row::

      .. column::
        :column-class: text-center

        width of 4

      .. column::
        :column-class: text-center text-bg-dark

        width of 4

      .. column::
        :column-class: text-center

        width of 4

    .. row::

      .. column::
        :column-class: text-center

        width of 3

      .. column::
        :column-class: text-center bg-danger-subtle

        width of 3

      .. column::
        :column-class: text-center

        width of 3

      .. column::
        :column-class: text-center bg-danger-subtle


    .. row::

      .. column::
        :column-class: text-center bg-success-subtle

        width of 2

      .. column::
        :column-class: text-center bg-success-subtle

        width of 2

      .. column::
        :column-class: text-center bg-success-subtle

        width of 2

      .. column::
        :column-class: text-center bg-success-subtle

        width of 2

      .. column::
        :column-class: text-center bg-success-subtle

        width of 2

      .. column::
        :column-class: text-center bg-success-subtle

        width of 2

    .. row::

      .. column::
        :column-class: text-center bg-info-subtle

        width of 1

      .. column::
        :column-class: text-center

        width of 1

      .. column::
        :column-class: text-center bg-info-subtle

        width of 1

      .. column::
        :column-class: text-center

        width of 1

      .. column::
        :column-class: text-center bg-info-subtle

        width of 1

      .. column::
        :column-class: text-center

        width of 1

      .. column::
        :column-class: text-center bg-info-subtle

        width of 1

      .. column::
        :column-class: text-center

        width of 1

      .. column::
        :column-class: text-center bg-info-subtle

        width of 1

      .. column::
        :column-class: text-center

        width of 1

      .. column::
        :column-class: text-center bg-info-subtle

        width of 1

      .. column::
        :column-class: text-center

        width of 1

**Result**

.. point-of-interest:: Testing column widths

  .. row::

    .. column::
      :column-class: bg-warning-subtle text-center

      See how width of 12 is separated between columns on the same row. Note how the "width of 1" columns overflow when making the browser window more narrow. To prevent this, set each column width explicitly.

  .. row::

    .. column::
      :column-class: text-bg-light text-center

      This column has width of 6.

    .. column::
      :column-class: text-bg-secondary text-center

      This column also has width of 6.
      See again how width is spread with columns 6 + 6 = 12

  .. row::

    .. column::
      :column-class: text-center

      width of 4

    .. column::
      :column-class: text-center text-bg-dark

      width of 4

    .. column::
      :column-class: text-center

      width of 4

  .. row::

    .. column::
      :column-class: text-center

      width of 3

    .. column::
      :column-class: text-center bg-danger-subtle

      width of 3

    .. column::
      :column-class: text-center

      width of 3

    .. column::
      :column-class: text-center bg-danger-subtle


  .. row::

    .. column::
      :column-class: text-center bg-success-subtle

      width of 2

    .. column::
      :column-class: text-center bg-success-subtle

      width of 2

    .. column::
      :column-class: text-center bg-success-subtle

      width of 2

    .. column::
      :column-class: text-center bg-success-subtle

      width of 2

    .. column::
      :column-class: text-center bg-success-subtle

      width of 2

    .. column::
      :column-class: text-center bg-success-subtle

      width of 2

  .. row::

    .. column::
      :column-class: text-center bg-info-subtle

      width of 1

    .. column::
      :column-class: text-center

      width of 1

    .. column::
      :column-class: text-center bg-info-subtle

      width of 1

    .. column::
      :column-class: text-center

      width of 1

    .. column::
      :column-class: text-center bg-info-subtle

      width of 1

    .. column::
      :column-class: text-center

      width of 1

    .. column::
      :column-class: text-center bg-info-subtle

      width of 1

    .. column::
      :column-class: text-center

      width of 1

    .. column::
      :column-class: text-center bg-info-subtle

      width of 1

    .. column::
      :column-class: text-center

      width of 1

    .. column::
      :column-class: text-center bg-info-subtle

      width of 1

    .. column::
      :column-class: text-center

      width of 1


**POI with column offsets**

.. code-block:: none

  .. point-of-interest:: Column offsets

    .. row::

      .. column::
        :width: 4
        :column-class: offset-sm-4 text-bg-danger

        This column has a width of 4 and offset of 4.

    .. row::

      .. column::
        :column-class: text-bg-danger p-2

        This column has no width set, resulting in a width of 12/3 = 4.

      .. column::
        :column-class: text-danger-emphasis bg-danger-subtle p-2

        This column uses the text-danger-emphasis and bg-danger-subtle classes.

      .. column::
        :column-class: text-bg-danger p-2

        This column has no width set, resulting in a width of 12/3 = 4.

    .. row::

      .. column::
        :width: 4
        :column-class: offset-sm-4 text-bg-danger p-2

        This column has a width of 4 and offset of 4.

**Result**

.. point-of-interest:: Column offsets

  .. row::

    .. column::
      :width: 4
      :column-class: offset-sm-4 text-bg-danger

      This column has a width of 4 and offset of 4.

  .. row::

    .. column::
      :column-class: text-bg-danger p-2

      This column has no width set, resulting in a width of 12/3 = 4.

    .. column::
      :column-class: text-danger-emphasis bg-danger-subtle p-2

      This column uses the text-danger-emphasis and bg-danger-subtle classes.

    .. column::
      :column-class: text-bg-danger p-2

      This column has no width set, resulting in a width of 12/3 = 4.

  .. row::

    .. column::
      :width: 4
      :column-class: offset-sm-4 text-bg-danger p-2

      This column has a width of 4 and offset of 4.

**Making columns with ::newcol (Deprecated)**

The ``::newcol`` separator in points-of-interest is deprecated and you should use row and column directives for creating columns and rows.

.. code-block:: none

    .. point-of-interest:: Testing newcol
      :columns: 3 1 1

      This is on the first column. In this case columns option sets each column to be equal width. You could set it to any ratio like 1 1 1.

      ::newcol

      This is on the second column.

      ::newcol

      And this is on the third.

**Result**

.. point-of-interest:: Testing newcol
  :columns: 3 1 1

  This is on the first column. In this case columns option sets each column to be equal width. You could set it to any ratio like 1 1 1.

  ::newcol

  This is on the second column.

  ::newcol

  And this is on the third.


.. admonition:: Don't mix newcol with row and column directives
  :class: alert alert-info

  I don't recommend mixing ``::newcol`` with row and column directives. It will work but may not work the way you intend it to.

Show POI only in the slides
---------------------------

Sometimes you may want to include specific POI only in the slides and not show it in the course material at all.

Then you should use ``:not_in_book:`` option. It doesn't take any arguments, it's just a flag.

.. code-block:: none

    .. point-of-interest:: Only in the slides
      :not_in_book:

      This is slide specific content.

**Result**

.. point-of-interest:: Only in the slides
  :not_in_book:

  This is slide specific content.


Show POI only in the A+ Course material
---------------------------------------

To create content that does not show in the slides.

.. code-block:: none

    .. point-of-interest:: Only in the book (A+ course)
      :not_in_slides:

      This does not appear in the slides.

**Result**

.. point-of-interest:: Only in the book (A+ course)
  :not_in_slides:

  This does not appear in the slides.

Hide POI from everywhere
------------------------

To create content that does not show nowhere but want still to keep around.

.. code-block:: none

    .. point-of-interest:: This POI is hidden
      :not_in_slides:
      :not_in_book:

      This content is hidden.

**Result**

.. point-of-interest:: This POI is hidden
  :not_in_slides:
  :not_in_book:

  This content is hidden.


Remove surrounding borders around POI
-------------------------------------

Use ``:no_poi_box:`` option if you want to create POI that does not pop up from the rest of the content. This also removes links (previous and next) from the POI border.

.. code-block:: none

    .. point-of-interest:: This POI does not have borders
      :no_poi_box:

      This content is blended with the rest of the content in the A+ course material.

**Result**

.. point-of-interest:: This POI does not have borders
  :no_poi_box:

  This content is blended with the rest of the content in the A+ course material.

