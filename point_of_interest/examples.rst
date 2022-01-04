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

**Width** can have values between 1 to 12. Where 12 is the whole width of the available space. These are relative widths.

**column-class** can have any bootstrap class. You can set background color or align text for instance.

To find out more about the classes you can use: `Bootstrap documentation <https://getbootstrap.com/docs/3.4/css/#helper-classes-backgrounds>`_.

In the examples below you can see some use cases.

**POI with two columns**

.. code-block:: none

    .. point-of-interest:: POI with columns

        .. row::

            .. column::
               :width: 12
               :column-class: bg-warning text-center

               First row with the width of 12. This has background color set to bg-warning which is red and text is aligned to center.

        .. row::

            .. column::
              :width: 6
              :column-class: bg-light text-center

              .. math::

                 (a + b)^2 = a^2 + 2ab + b^2

                 (a - b)^2 = a^2 - 2ab + b^2

            .. column::
              :width: 6
              :column-class:

              This second row is split between two columns, each have width of 6. 6 + 6 = 12 which is maximum value in the row.

**Result**

.. point-of-interest:: POI with columns

    .. row::

        .. column::
           :width: 12
           :column-class: bg-warning text-center

           First row with the width of 12. This has background color set to bg-warning which is red and text is aligned to center.

    .. row::

        .. column::
          :width: 6
          :column-class: bg-light text-center

          .. math::

             (a + b)^2 = a^2 + 2ab + b^2

             (a - b)^2 = a^2 - 2ab + b^2

        .. column::
          :width: 6
          :column-class:

          This second row is split between two columns, each have width of 6. 6 + 6 = 12 which is maximum value in the row.


**POI with nested columns**

.. code-block:: none

    .. point-of-interest:: Making nested columns

        .. row::

            .. column::
              :width: 8
              :column-class: bg-warning text-center

              See how width of 12 is separated between columns which are on the same row. Be careful with the indentation.

                .. row::

                    .. column::
                      :width: 6
                      :column-class: bg-light

                      This column has width of 6.

                    .. column::
                      :width: 6
                      :column-class: bg-secondary

                      This column also has width of 6.
                      See again how width is spread with columns 6 + 6 = 12

            .. column::
              :width: 4
              :column-class:

              This is nested. This first row is split between two columns, first have a width of 8 and this has 4.
              8 + 4 = 12 which is maximum value in the row.

**Result**

.. point-of-interest:: Making nested columns

    .. row::

        .. column::
          :width: 8
          :column-class: bg-warning text-center

          See how width of 12 is separated between columns which are on the same row. Be careful with the indentation.

            .. row::

                .. column::
                  :width: 6
                  :column-class: bg-light

                  This column has width of 6.

                .. column::
                  :width: 6
                  :column-class: bg-secondary

                  This column also has width of 6.
                  See again how width is spread with columns 6 + 6 = 12

        .. column::
          :width: 4
          :column-class:

          This is nested. This first row is split between two columns, first have a width of 8 and this has 4.
          8 + 4 = 12 which is maximum value in the row.


**POI with multiple rows and columns**

.. code-block:: none

    .. point-of-interest:: Testing column widths

        .. row::

            .. column::
              :width: 12
              :column-class: bg-warning text-center

              See how width of 12 is separated between columns which are on the same row. Be careful with the indentation.

        .. row::

            .. column::
              :width: 6
              :column-class: bg-light text-center

              This column has width of 6.

            .. column::
              :width: 6
              :column-class: bg-secondary text-center

              This column also has width of 6.
              See again how width is spread with columns 6 + 6 = 12

        .. row::

            .. column::
              :width: 4
              :column-class: text-center

              width of 4

            .. column::
              :width: 4
              :column-class: text-center bg-dark

              width of 4

            .. column::
              :width: 4
              :column-class: text-center

              width of 4

        .. row::

            .. column::
              :width: 3
              :column-class: text-center

              width of 3

            .. column::
              :width: 3
              :column-class: text-center bg-danger

              width of 3

            .. column::
              :width: 3
              :column-class: text-center

              width of 3

            .. column::
              :width: 3
              :column-class: text-center bg-danger

              width of 3

        .. row::

            .. column::
              :width: 2
              :column-class: text-center bg-success

              width of 2

            .. column::
              :width: 2
              :column-class: text-center bg-success

              width of 2

            .. column::
              :width: 2
              :column-class: text-center bg-success

              width of 2

            .. column::
              :width: 2
              :column-class: text-center bg-success

              width of 2

            .. column::
              :width: 2
              :column-class: text-center bg-success

              width of 2

            .. column::
              :width: 2
              :column-class: text-center bg-success

              width of 2

        .. row::

            .. column::
              :width: 1
              :column-class: text-center bg-info

              width of 1

            .. column::
              :width: 1
              :column-class: text-center

              width of 1

            .. column::
              :width: 1
              :column-class: text-center bg-info

              width of 1

            .. column::
              :width: 1
              :column-class: text-center

              width of 1

            .. column::
              :width: 1
              :column-class: text-center bg-info

              width of 1

            .. column::
              :width: 1
              :column-class: text-center

              width of 1

            .. column::
              :width: 1
              :column-class: text-center bg-info

              width of 1

            .. column::
              :width: 1
              :column-class: text-center

              width of 1

            .. column::
              :width: 1
              :column-class: text-center bg-info

              width of 1

            .. column::
              :width: 1
              :column-class: text-center

              width of 1

            .. column::
              :width: 1
              :column-class: text-center bg-info

              width of 1

            .. column::
              :width: 1
              :column-class: text-center

              width of 1

**Result**

.. point-of-interest:: Testing column widths

    .. row::

        .. column::
          :width: 12
          :column-class: bg-warning text-center

          See how width of 12 is separated between columns which are on the same row. Be careful with the indentation.

    .. row::

        .. column::
          :width: 6
          :column-class: bg-light text-center

          This column has width of 6.

        .. column::
          :width: 6
          :column-class: bg-secondary text-center

          This column also has width of 6.
          See again how width is spread with columns 6 + 6 = 12

    .. row::

        .. column::
          :width: 4
          :column-class: text-center

          width of 4

        .. column::
          :width: 4
          :column-class: text-center bg-dark

          width of 4

        .. column::
          :width: 4
          :column-class: text-center

          width of 4

    .. row::

        .. column::
          :width: 3
          :column-class: text-center

          width of 3

        .. column::
          :width: 3
          :column-class: text-center bg-danger

          width of 3

        .. column::
          :width: 3
          :column-class: text-center

          width of 3

        .. column::
          :width: 3
          :column-class: text-center bg-danger

          width of 3

    .. row::

        .. column::
          :width: 2
          :column-class: text-center bg-success

          width of 2

        .. column::
          :width: 2
          :column-class: text-center bg-success

          width of 2

        .. column::
          :width: 2
          :column-class: text-center bg-success

          width of 2

        .. column::
          :width: 2
          :column-class: text-center bg-success

          width of 2

        .. column::
          :width: 2
          :column-class: text-center bg-success

          width of 2

        .. column::
          :width: 2
          :column-class: text-center bg-success

          width of 2

    .. row::

        .. column::
          :width: 1
          :column-class: text-center bg-info

          width of 1

        .. column::
          :width: 1
          :column-class: text-center

          width of 1

        .. column::
          :width: 1
          :column-class: text-center bg-info

          width of 1

        .. column::
          :width: 1
          :column-class: text-center

          width of 1

        .. column::
          :width: 1
          :column-class: text-center bg-info

          width of 1

        .. column::
          :width: 1
          :column-class: text-center

          width of 1

        .. column::
          :width: 1
          :column-class: text-center bg-info

          width of 1

        .. column::
          :width: 1
          :column-class: text-center

          width of 1

        .. column::
          :width: 1
          :column-class: text-center bg-info

          width of 1

        .. column::
          :width: 1
          :column-class: text-center

          width of 1

        .. column::
          :width: 1
          :column-class: text-center bg-info

          width of 1

        .. column::
          :width: 1
          :column-class: text-center

          width of 1


**Making columns with ::newcol (Deprecated)**

The ``::newcol`` separator in points-of-interest is deprecated and you should use row and column directives for creating columns and rows.

.. code-block:: none

    .. point-of-interest:: Testing newcol
      :columns: 1 1 1

      This is on the first column. In this case columns option sets each column to be equal width. You could set it to any ratio like 3 1 1.

      ::newcol

      This is on the second column.

      ::newcol

      And this is on the third.

**Result**

.. point-of-interest:: Testing newcol
  :columns: 1 1 1

  This is on the first column. In this case columns option sets each column to be equal width. You could set it to any ratio like 3 1 1.

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

