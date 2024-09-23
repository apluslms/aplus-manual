Setting up Jutut
================

Creating feedback questionnaires
--------------------------------

If you have feedback questionnaires already in your material, you can use them directly.
See the chapter :doc:`questionnaires </questionnaires/questionnaires>` for general instructions how to create questionnaires.
You can see the `documentation of a-plus-rst-tools <https://github.com/apluslms/a-plus-rst-tools?tab=readme-ov-file#3-feedback-questionnaire>`_ for more information about feedback questionnaires.

If you wish to use the same questionnaire for multiple chapters or multiple modules, you probably want to define the questionnaire in its own file and include that at the end of each chapter using the `include <https://docutils.sourceforge.io/docs/ref/rst/directives.html#include>`_ directive.
One can, of course, also directly include the feedback exercises in the chapter rst-file.

A typical feedback exercise might look like this:

.. annotated::

  .. code-block:: rst

    .. questionnaire::
      1«:feedback:»
      :title: Feedback questionnaire

      .. freetext:: 0 int
        :required:
        2«:key: timespent»
        :height: 1
        :length: 20
        :class: time-usage-question
        :extra: minimum=6;validationMessage=Please enter the time in minutes.

        **Time spent:**

        Please estimate **the total number of minutes** you spent on this chapter (reading, assignments,
        etc.). You don’t have to be exact, but if you can produce an estimate to within 15 minutes or
        half an hour, that would be great.

      .. pick-one::
        :required:
        2«:key: understood»

        **“I feel that I have understood the most important things in this chapter.”**

        a. fully agree
        b. somewhat agree
        c. somewhat disagree
        d. fully disagree
        e. I’m unable to answer or don’t want to comment.

      .. freetext::
        3«:main-feedback:»
        :required:
        :key: mainfeedback
        :length: 100
        :height: 8

        Give feedback on the chapter.

  .. annotation::

    Providing the ``feedback`` flag sets the default options to the defaults for feedback questionnaires: the category ``feedback`` and maximum points of 0.
    The exercise key is also hardcoded to ``feedback``.

  .. annotation::

    Jutut provides :ref:`context tags <jutut_context_tags>` by default for questions with the keys ``timespent`` and ``understood``.

  .. annotation::

    If there would be multiple free text fields, potential teacher replies are displayed by the question with the ``main-feedback`` flag.


Edit settings to use Jutut for feedback exercises
-------------------------------------------------

You must set the service URL of the feedback exercises to the MOOC-Jutut server, which can only be done in the project ``conf.py`` file.

.. code-block::

    override = {
        'feedback': {
            'url': 'https://jutut.cs.aalto.fi/feedback/coursekey/{key}',
        },
    }

(Replace ``coursekey`` with the key of the course.
If you are using some other category name for the feedback exercises, such as ``jututfeedback``, replace also ``feedback`` with your selected category name.)

If you have a multilingual course, you probably want to provide translations for the feedback category in the ``category_names`` dict:

.. code-block::

    category_names = {
        ... // list other categories here with their translated names
        'feedback': {
            'fi': 'Palaute',
            'en': 'Feedback',
        },
    }


Adding the link to the side menu
--------------------------------

When your course is running on A+, navigate to the course instance.

* From the side menu, select **Edit course**.
* Select the **Menu** tab.
* Click on the button **Add new menu item**.

.. figure:: /images/jutut/jutut_setup_edit_menu.png
    :width: 100%
    :alt: Screenshot of the "Menu items" page under the "Edit course" section.

Fill in the form and click "Save".

* For the *Access* field, select "Only teachers can access" or "Only assistants and teachers can access."
* For the Service field, select **(LTI) Jutut** from the dropdown.
* You may leave the URL field empty.
* If you would like the link in the side menu to be grouped under a heading, you can provide the heading in the field *Menu group label*, for example "Local Services".
* You may leave the menu label and menu icon class field empty if you would like the default values for Jutut to be used.

.. figure:: /images/jutut/jutut_setup_menu_item_form.png
    :width: 100%
    :alt: Screenshot of the filled "Add menu item" page.

Now you're all set up!
To get to Jutut, click on the link in the sidebar.
As soon as students submit responses to feedback questionnaires, you'll be able to see their responses in Jutut.
