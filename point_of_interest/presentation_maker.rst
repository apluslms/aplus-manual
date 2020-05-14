Presentation Maker
==================

.. styled-topic::

  Main questions:
      Quick guide to Presentation Maker.

  Topics?
      Introduction, why you should use it, how it works and how to use it.

  Difficulty:
      Difficult

  Laboriousness:
      Reading takes about 5 minutes. Learning how to use Presentation Maker about 1 hour or more.

What is it?
-----------

Presentation Maker is a tool for making HTML & PDF presentations from the point of interest summary blocks (POI).

Presentation Maker finds all used POI directives from the reStructuredText (RST) course material and makes a presentation out of them.

More at the `Presentation Maker documentation <https://github.com/apluslms/presentation-maker>`_.

Why to use Presentation Maker?
------------------------------

Purpose of the Presentation Maker is to **eliminate separate process of creating presentation slides.** It all comes down to creating good POI which can be used as a slides.

If you start creating POI summary blocks with the same mindset as creating presentation slides you can just run Presentation Maker and in seconds you have a set of slides ready.

How it works
------------

In order to use Presentation Maker effectively you will need to know how it works.

**Each POI represents a slide.**

When you make POI keep in mind that it creates a slide. So make content to look like a slide.

**Presentation Maker systematically searches POI from the start of the course materials to the end**

Presentation Maker does not care about links between POI. It just adds POI to the presentation in the order as they appear on the content. You can of course choose what rounds will be included in the presentation.

**How can I edit the last slide?**

You can edit the last slide from the Presentation Maker configuration file :code:`(presentation_config.yaml)`. You will find the presentation_config.yaml at the root of your course directory.

If presentation_config.yaml file is not there, run the Presentation Maker for the first time and the configuration file should appear.

Here is a snippet from the presentation_config.yaml. Feel free to edit contents of the content option. Just keep the indentation and "|" character after the content option.

.. code-block:: none

  last_slide:
  data-scale: 1
  class: center_text
  content: |

    Last slide title
    ----------------

    Here is the content of the last slide.


Making a good POI
-----------------

If you want to make good presentation slides with the Presentation Maker you will need to keep these tips in mind:

- Keep it short, like making actual presentation slides.
- Test what works. Presentation Maker makes slides relatively fast so testing is easy and fast.
- Use ``:not_in_slides:``, ``:not_in_book:``, ``:no_poi_box`` to select what is included in the presentation slides.

.. admonition:: Sometimes POI and the slides do not look the same

  We are trying our best to make POI and the slides look exactly the same in layout wise. But sometimes things look different.


How to use it?
--------------

Presentation Maker works with `Roman <https://github.com/apluslms/roman>`_. If you have Roman installed Presentation Maker should work too. If you don't have Roman installed, see the installing part in the `documentation <https://github.com/apluslms/presentation-maker#installing>`_.

So how to use it:

1. Edit course.yml to add parameters. Or change settings in the presentation_config.yaml.
2. Open terminal.
3. Make sure you are in the root of your A+ course directory.
4. Run roman command.
5. Presentation directory was created inside the _build directory. a+course/_build/presentation

For more detailed instructions see the documentation, especially the part: `Making presentations <https://github.com/apluslms/presentation-maker#making-presentations>`_.
