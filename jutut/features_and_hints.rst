Overview of some features of the Jutut teacher portal
=====================================================

When you have opened the Jutut teacher portal and selected the correct course instance, you are taken to the page listing unread feedback.
Here you can read, respond and tag feedback that is considered unread.

.. hint::
    If you would like to mark a feedback as unread without responding, respond with an empty message.
    This does not send a notification to the student and the message will be considered read.

You can access most of the other features through the menu by clicking on **More**:

.. figure:: /images/jutut/unread_with_moremenu_open.png
    :width: 100%

Both the green "Filter feedback" button on the page displaying unread feedback and the link with the same name in the *More* menu take you to the page where you can see all feedback and filter/search them.

.. figure:: /images/jutut/feedbacklist_overview.png
    :width: 100%

    *Overview of the feedback filtering page.*

Many of the filters have help texts explaining what they do.
These are displayed as tooltips when you hover on the filter label.

There are additional filters for advanced searching.
These can be accessed by clicking the *More options* button in the filter view.

.. figure:: /images/jutut/feedbackfilter_expanded.png
    :width: 100%

    *Feedback filtering page with the additional filter options visible.*

The feedback message panel displays student information, exercise information, as well as the feedback response and a text box for a teacher to respond to the feedback.
Information about `feedback tags`_ and `context tags`_ can be found under their own headings.

.. figure:: /images/jutut/feedback_message_annotated.png
    :width: 100%

    *Feedback panel with annotations.*

By default, the feedback responses are displayed compactly with only the text responses being shown.
If you want to see the responses to other questions, the question keys, or what the questions actually asked, you can expand the message by clicking on the timestamp / down icon.

.. figure:: /images/jutut/feedback_message_expanded.png
    :width: 100%

.. hint::

    If you want to send another member of course staff a link directly to a feedback conversation, copy the link from the "Show feedback for this exercise by this student" button.

    .. figure:: /images/jutut/feedback_link.png
        :width: 100%
        :alt: The button for getting the link is after the chapter title and the button for filtering feedback for the given exercise.

You as the teacher can respond to student feedback through the Jutut teacher portal.
The student receives a notification in A+, but also can see the conversation history at the questionnaire embedded in the material. The student can respond by sending another submission.

.. figure:: /images/jutut/conversation_student.png
    :width: 60%

    *The student perspective of the conversation.*

The responses by the same student to the same questionnaire are grouped together and displayed as a conversation.

.. figure:: /images/jutut/conversation_teacher.png
    :width: 100%

    *The teacher perspective of the conversation.*


Feedback tags
-------------

Feedback tags allow you to tag feedback conversations with custom tags.
Feedback responses can be filtered based on these taggings.
You can create and edit feedback tags for the course instance the their own page (*More* -> *Manage feedback tags*).

.. figure:: /images/jutut/feedbacktags_manage.png
    :width: 100%
    :alt: Screenshot of the feedback tags management page titled "List of feedback tags"


.. hint:: 

    If you have a lot of feedback tags and use some more often than others and would like them to be "pinned" to the top / displayed before the others, edit the slug so it begins with a small number (e.g. '0' or '1'), as the tags are ordered alphabetically by the slugs.

When filtering using feedback tags, you can select whether the conversations *should have* the specified tag (by clicking once on the tag button) or should *NOT* have the specified tag (by clicking twice on the tag button).
(The feedback tag buttons in the filter view have three states: (0) inactive ->  (1) include -> (2) exclude -> back to (0) inactive.)

If you select multiple feedback tags to filter using the included criterion, you can specify whether it's enough that the conversations have *any* of the specified tags (use the **OR** operator) or if they should have *all* of the specified tags (use the **AND** operator).
Despite which operator is being used, if a conversation has any of the tags specified to be excluded, it will not show up in the results.

.. figure:: /images/jutut/feedbacktag_filtering.png
    :width: 100%
    :alt: If the user selects that the *DONE* tag is to be excluded and the *Respond* tag to be included in the search, when filtering, conversations that have been tagged with the *Respond* tag and do not have the *DONE* tag will be returned.

    *Filter conversations excluding those with the **DONE** tag and including those with the **Respond** tag.*


Context tags
------------

Some questions in the feedback questionnaires provide valuable context for understanding the textual feedback provided by students.
The teacher can create context tags, which appear by feedback responses if they contain a specified response value to a certain question (with a given question key).

These context tags can be created, edited and deleted for the course instance on their own page (*More* -> *Manage context tags*). 

.. image:: /images/jutut/contexttags_manage.png
    :width: 100%
    :alt: Screenshot of the context tags management page titled "List of context tags"

For example, feedback questionnaires can have a question **“I feel that I have understood the most important things in this chapter.”** with the key ``understood``, and answer options of "a: fully agree", "b: somewhat agree", "c: somewhat disagree", "d: fully disagree", and "e: I’m unable to answer or don’t want to comment."
Now if a feedback questionnaire contains that question, the responses will contain a tag to indicate which option the student chose, as seen in the image below. If you move your cursor on top of the context tag, the tooltip displays what the question and the response were.

.. image:: /images/jutut/contexttags_feedback.png
    :width: 100%
    :alt: Screenshot of feedback responses with context tags, including the timespent tag and a tag indicating the response to the "understood" question.

.. hint::
    The response values can be defined as regex patterns, so you can have context tags appear if the responses contain certain content.
    For example, if you would like, you can have different color timespent tags for different lengths of times. 

Student tags
------------

Student tags are created, edited and added to students through A+ (*Edit course* -> *Tags*).
In order to import the student tags to Jutut (or update the tags or taggings), you need to update them manually by pressing the **Update tags now** button on the *Update student tags* page (*More* -> *Update student tags*).

When filtering using student tags, the same things apply as described for filtering using feedback tags above.

.. questionnaire::
  :feedback:
  :title: Feedback questionnaire
  :category: feedback

  .. pick-one::
    :required:
    :key: understood

    **“I feel that I have understood the most important things in this chapter.”**

    a. fully agree
    b. somewhat agree
    c. somewhat disagree
    d. fully disagree
    e. I’m unable to answer or don’t want to comment.

  .. freetext::
    :main-feedback:
    :key: 
    :length: 100
    :height: 8

    Does something seem unclear? Should something be expanded or clarified?
    Or should something else be explained or demonstrated?