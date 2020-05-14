Point of Interest (POI)
=======================

.. styled-topic::

  Main questions:
      What are point of interest directives, why and how to use it.

  Topics?
      Point of interest.

  Difficulty:
      Easy

  Laboriousness:
      Around 5 minutes of reading


Introduction to the Point of Interest directive.


What is a point of interest?
----------------------------

Directive for creating a "point of interest" summary block.

A point of interest looks the same as a normal admonition ("coloured info box"), but has more functionality. Point of interest has a title, collapsible content section and
the point of interest are also linked to each other with next/previous links. The links enable
the user to quickly navigate between different points of interest. See all :doc:`POI options <examples>` available.

Point of interests may also be used to generate separate lecture slides
(not directly included in the A+ content chapters). This requires a separate
tool called :doc:`Presentation Maker <presentation_maker>`

.. point-of-interest:: This is a point of interest

  And here is the content. More examples in the :doc:`next chapter <examples>`

From now on I will refer to point of interest as a POI.

Why to use points of interest?
------------------------------

Using points of interest in your course may bring some benefits. Firstly, the points of interest can be used to highlight important parts of your course content while linking these elements together in a logical and sequential manner. Finally, the points of interest can be exported as presentation slides with the Presentation Maker.

How to use POI?
---------------

1. Point of Interest should work out of the box, but if you run into problems:

   - Try updating your a-plus-rst-tools.
     Read these `instructions <https://github.com/apluslms/a-plus-rst-tools/blob/master/README.md#upgrading-the-tools>`_

   - Try activating the extension by inserting "point_of_interest" in the project conf.py
     (``extensions = ["aplus_setup", "point_of_interest"]``).

     For more detailed instructions, read this part of the `A-plus RST tools documentation <https://github.com/apluslms/a-plus-rst-tools#9-point-of-interest>`_.

2. Next step is to start writing reStructuredText content and to use POI directives.
