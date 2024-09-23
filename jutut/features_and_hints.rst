Overview of some features of the Jutut teacher portal
=====================================================

When you have opened the Jutut teacher portal and selected the correct course instance, you are taken to the page listing unread feedback.
Here you can read, respond and tag feedback that is considered unread.

.. hint::
    If you would like to mark a feedback as read without responding, respond with an empty message.
    This does not send a notification to the student and the message will be considered read.

You can access most of the other features through the menu by clicking on **More**:

.. figure:: /images/jutut/unread_with_moremenu_open.png
    :width: 100%
    :alt: The page displays unread feedback. The button "More" in the navigation bar has been pressed, and the dropdown menu it toggles is open.

Both the green "Filter feedback" button on the page displaying unread feedback and the link with the same name in the *More* menu take you to the page where you can see all feedback and filter/search them.

.. figure:: /images/jutut/feedbacklist_overview.png
    :width: 100%
    :alt: The filtering page with the filter bar displaying the filters: "Student", "Exercise", "Exercise identifier", "Student content", "Teacher content", "Display only feedback with text content", "Feedback tags", and "Sort". There are buttons "More options" and "Filter". Beneath the filter bar, there is a pagination menu and some feedback panels.

    *Overview of the feedback filtering page.*

Many of the filters have help texts explaining what they do.
These are displayed as tooltips when you hover on the filter label.

There are additional filters for advanced searching.
These can be accessed by clicking the *More options* button in the filter view.

.. figure:: /images/jutut/feedbackfilter_expanded.png
    :width: 100%
    :alt: The filter view including the additional filters of "Timestamp", "Responder", "Response grade", flag filters (Read/Both/Unread, Graded/Both/Ungraded, Manually graded / Both / Automatically graded, Responded/Both/Unresponded, Upload has error / Both / Upload ok) as well as the student tag filter.

    *Feedback filtering page with the additional filter options visible.*

Feedback message view
---------------------

The feedback message panel displays student information, exercise information, as well as the feedback response and a text box for a teacher to respond to the feedback.
Information about `feedback tags`_ and `context tags`_ can be found under their own headings.

.. figure:: /images/jutut/feedback_message_annotated.png
    :width: 100%
    :alt: Feedback message with different zones annotated. The panel heading contains student information. Beneath it is exercise information and context tags. On the right are feedback tags.

    *Feedback panel with annotations.*

Student information
...................

* The student name is a link to the student page in A+.
* The student tags are listed after the student name
* The filter button in the student info updates the page to show all the conversations with that particular student.
* The button with an eye opens a popover, which shows all the converstations with the particular student
  (i.e. the same content as the previous button, but in a preview mode without updating the page)

  .. hidden-block:: conv-popover
    :label: Show/hide image of conversation preview popover

    .. figure:: /images/jutut/feedback_conv_prev.png
        :width: 70%
        :alt: The conversation preview popover appears on the right side of the page and shows the conversations with the student compactly.

* The *Background* button shows a popover of the student's response to the background questionnaire (enrollment exercise)

  .. hidden-block:: conv-background
    :label: Show/hide image of background popover

    .. figure:: /images/jutut/feedback_conv_prev.png
        :width: 70%
        :alt: The background popover appears on the right side of the page and shows the student's response to the background questionnaire compactly. Only the questions the student has responded to and the student's responses are visible.

* The *Points* button shows a popover of the student's points for the entire course, the module and the chapter.

  .. hidden-block:: points
    :label: Show/hide image of points popover

    .. figure:: /images/jutut/feedback_points.png
        :width: 70%
        :alt: The points popover appears on the right side of the page and shows the student's points as progress bars for the point categories (for the entire course), as well as the module and the chapter. The progress bars are color coded.

The popovers are opened when hovered, clicked or focused (keyboard navigation).

.. hint::
    If you need to scroll a popover, make sure to open the popover by clicking or moving the focus onto the button.
    You can scroll the popover when your cursor is on top of it.
    If you open a popover by hovering on top of the button, the popover closes as soon as you move your cursor away from the button (even if onto the popover).

Message display
...............

By default, the feedback responses are displayed compactly with only the text responses being shown.
If you want to see the responses to other questions, the question keys, or what the questions actually asked, you can expand the message by clicking on the timestamp / down icon.

.. figure:: /images/jutut/feedback_message_expanded.png
    :width: 100%
    :alt: The feedback message is expanded and displays all the field names and responses to them.

    *The expanded version of the feedback message.*

.. hint::

    If you want to send another member of course staff a link directly to a feedback conversation, you can copy the link to you clipboard by pressing "Copy link to this conversation".

    .. figure:: /images/jutut/feedback_link.png
        :width: 100%
        :alt: The button for getting the link is after the chapter title and the button for filtering feedback for the given exercise.

You as the teacher can respond to student feedback through the Jutut teacher portal.
The teacher responses support HTML styling.
You can use the styling buttons to automatically provide correct tags for bold, italics, monospace, and hyperlinks.
Also keyboard shortcuts are supported for bold (CTRL/⌘ + B), italics (CTRL/⌘ + I), and underline (CTRL/⌘ + U).
You can preview how the message appears and that the styling works by clicking the preview button.

.. figure:: /images/jutut/message_editing.png
    :width: 100%
    :alt: The message editing view includes the potential html tags within the text. At the bottom of the response box, there is a toolbar of buttons for styling the message.

    *The message response box in the editing view displays included html tags.
    There is a button at the bottom left for previewing the content.*

.. figure:: /images/jutut/message_preview.png
    :width: 100%
    :alt: The message preview displaying the content. The content appears in a span rather than a textbox, so it's not editable. The styling buttons are disabled.

    *The message response box in the preview view displays the content as it would appear to a student.
    There is a button at the bottom left for going back to the editing view.*

If a feedback assignment is worth a non-zero amount of points and the text field is marked as required, the student is not automatically given the points for the feedback exercise.
Instead, the teacher has to grade the submission.
The "Respond" button is replaced by a segmented dropdown button that implements the grading.
The default green "Good" option awards the student full points.
If you wish to give half points or zero points, click on the dropdown and select either "Accepted" (half points) or "Rejected" (zero points).

.. figure:: /images/jutut/feedback_grade_menu.png
    :width: 100%
    :alt: There is a green button with the text "Good" with a dropdown toggle next to it. There is a dropdown toggle which opens a dropdown menu with the options "Accepted" and "Rejected". The dropdown is open.

    *The open grading dropdown.*

The responses by the same student to the same questionnaire are grouped together and displayed as a conversation.

.. figure:: /images/jutut/conversation_teacher.png
    :width: 100%
    :alt: In the message panel there is a message from a student, the teacher response, and a second message from the student.

    *The teacher perspective of the conversation.*


The student perspective
.......................

The student receives a notification in A+, but also can see the conversation history at the questionnaire embedded in the material. The student can respond by sending another submission.

.. figure:: /images/jutut/conversation_student.png
    :width: 60%
    :alt: The student sees the feedback as an embedded exercise. The student's previous responses to the text field (and the teacher's response) appear above the text field.

    *The student perspective of the conversation.*

.. hint::
    If the questionnaire has more than one text field, the teacher's responses are displayed by the "primary" feedback field.
    If a text field has the flag `main-feedback` in the source rst, that field is considered the primary feedback field.
    If the `main-feedback` flag doesn't appear, the last text field is considered the primary feedback field by default.

    .. figure:: /images/jutut/conversation_student_multiple_text.png
        :width: 70%
        :alt: The student's responses are displayed above the respective text fields. The teacher response is displayed above the last text field.

        *The student perspective of the conversation when there are multiple text fields.*

    .. figure:: /images/jutut/conversation_teacher_multiple_text.png
        :width: 100%
        :alt: The student's responses are displayed in a single "bubble".

        *The teacher's perspective of the conversation when there are multiple text fields.*

    If a questionnaire has no text field, potential teacher responses are displayed at the beginning of the form.


Feedback tags
-------------

Feedback tags allow you to tag feedback conversations with custom tags.
Feedback responses can be filtered based on these taggings.
You can create and edit feedback tags for the course instance the their own page (*More* -> *Manage feedback tags*).

.. figure:: /images/jutut/feedbacktags_manage.png
    :width: 100%
    :alt: Screenshot of the feedback tags management page titled "List of feedback tags"

If you would like a feedback tag to be "pinned" to the top / displayed before the others, you can select the "Pin" option.
This can be especially useful if you have a lot of feedback tags and use some very frequently.

.. hint::

    The tags are ordered alphabetically by the slugs.
    If you have a lot of feedback tags and want to group some of them, you can begin their names or just the slugs with the same prefix.

When filtering using feedback tags, you can select whether the conversations *should have* the specified tag (by clicking once on the tag button) or should *NOT* have the specified tag (by clicking twice on the tag button).
(The feedback tag buttons in the filter view have three states: (0) inactive ->  (1) include -> (2) exclude -> back to (0) inactive.)
The tag states can also be toggled in the *opposite* direction by using right click.

.. figure:: /images/jutut/colortag_toggle_viz.png
    :width: 60%
    :alt: Normal clicks toggle button state from default to include to exclude to default. Right clicks toggle button state in the opposite direction: default to exclude to include to default.

If you select multiple feedback tags to filter using the included criterion, you can specify whether it's enough that the conversations have *any* of the specified tags (use the **OR** operator) or if they should have *all* of the specified tags (use the **AND** operator).
Despite which operator is being used, if a conversation has any of the tags specified to be excluded, it will not show up in the results.

.. figure:: /images/jutut/feedbacktag_filtering.png
    :width: 100%
    :alt: The user has selected that the *DONE* tag and *Other teacher* tag are to be excluded, and the *Respond* tag and *URGENT!* tag are to be included in the search. The OR-option has been selected, so when filtering, conversations that have been tagged with the *Respond* tag or the *URGENT!* tag will appear as long as they don't also have either of the tags *DONE* nor *Other teacher*.

    *Filter conversations excluding those with the 'DONE' and 'Other teacher' tags and and including those with the 'Respond' or 'URGENT!' tag.
    Since the OR-operator has been selected, results appear as long as they have at least one of the tags to be included.*

Feedback tags can be imported also from other courses (or course instances) that are visible to you.
This can be cone on the *Import feedback tags from another course* page (*More* -> *Import feedback tags*).

.. _jutut_context_tags:

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
For courses that have not ended yet, the student tags should automatically updated once a day (around 1 A.M.).
You can also manually update the tags (i.e. update the tags or taggings from A+), by pressing the **Update tags now** button on the *Update student tags* page (*More* -> *Update student tags*).

When filtering using student tags, the same things apply as described for filtering using feedback tags above.

.. questionnaire::
  :feedback:
  :title: Feedback questionnaire
  :category: jututfeedback

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
    :key: comments
    :length: 100
    :height: 8

    Does something seem unclear? Should something be expanded or clarified?
    Or should something else be explained or demonstrated?
