Rubrics and Reviews
===================

.. styled-topic::

  Main questions:
      How to create rubrics and how to review submissions?

  Topics?
      Creating rubrics and reviewing submissions.

  Difficulty:
      Easy

  Laboriousness:
      ???

Rubrics
-------

Settings
........

The rubrics of Rubyric have four grading modes: *No grade*, *Mean*, *Sum*,
and *Always pass*. The last mode is only used with the LTI-connected exercises.

The *No grade* mode does not give any grade for the submission instead it gives
pure textual feedback. The normal requirements to finalize the review don't
hold, and the review can be *finalized* at any point.

The *Mean* mode allows you to define the set of grades which can be either numbers
or strings. You set a grade to the feedback phrases, and at end of each page,
the mean of grades is calculated. Rubyric offers the mean as a suggestion,
although the reviewer can also choose one of the other given grades for the
page. At the final page of review, reviewer chooses the final grade. If set of grades
are "Good", "ok" and "Needs improvement" (in this order), the suggested mean of 
"Good", "ok", "Needs improvement", "Needs improvement" and "Good" is "ok".

The *Sum* mode allows you to type points for your phrases. The final grade is 
sum of points from the chosen phrases in the review.

The *Always pass* mode does not give any grade and can be used to give pure 
textual feedback like the No grade mode. If the grading mode is Always pass, the
points will always be sent to A+ as full points. 

You can also define *feedback categories* if you wish.
The feedback categories can be for example "Strengths", "Weaknesses" and
"Other". In the plain text reviews (explained later), the chosen feedback
phrases are sorted by their chosen category. In final text everything written
under one category is collected together.

Some courses need to be able to provide feedback in more than one language (e.g.
in Finnish and in English). Rubrics can be defined with several *languages*. By 
default all rubrics have one default language. More languages can be defined at
by clicking "Add language" button at Languages section. Languages can be renamed 
by clicking on their names and rearranged by dragging them to desired position 
in the list. The first language in the list will be used as a default language 
in reviews. For each language the rubric will have alternative text field 
for translatable content, i.a. categories, page names and phrases. Deleting a 
language deletes all texts associated with the language. 

.. image:: /images/rubyric-rubric-settings.png
  :align: center

Pages
.....

The pages contain the "rubric" itself. Pages can be used for example to separate
different parts of assessment from each other, like one page contains criteria
for style and another for content. You can create as many criteria and feedback
phrases as you want per page. Depending on the mode you have chosen you can
associate grade/points and feedback categories with phrases. The order of
criteria and phrases can be changed by dragging them to position you want them
to be at. To make assessment easier for assistants you can add grading
instructions for pages and criteria to explain what they are supposed to be
paying attention to.

.. image:: /images/rubyric-rubric-page.png
  :align: center

|

In case you have several course instances with same assignments you don't need
to manually create same rubric multiple times. You can download existing rubric
as json from Rubyric and in turn upload them back to another assignment. You
can find this functionality in button next to save-button while editing rubric.

Remember to save rubric before leaving the page!

Reviews
-------

All submissions to exercise are shown on exercise page. Reviews of submission
are next to submission. New review can be created by choosing create new review
from dropdown next to submission.

The *type of a review* is defined in the settings of each exercise as
*Review mode*. It is chosen when you create the exercise. It can be changed
afterwards, but the change will not have any effect on reviews that have already
been started. You can generate example submissions from fake students to test
reviewing and your rubrics. You can do this by pressing the *Generate example
submissions* button at the exercise view. The button should be visible if
the exercise hasn't yet received any real submissions. The "generate example
submissions" option is also found at dropdown at top right of exercise page.

If the rubric has been done in more than one language, new review defaults to
using the first language at the language list. The language of review can be 
changed at Overview page while editing review. If the language is changed, the 
review should be saved and the page reloaded so that rubric changes its 
language. The rubric and all its phrases will be loaded at only one language to 
the review editor.

Reviews have several different statuses. *Started* means that review has already
some content but is not yet finished. *Finished* means that the review is done
and it is ready to be delivered. *Mailed* means that review has been delivered
to a student by e-mail. The *finished* status can be achieved by reaching
the *finalize page* while reviewing. In the *No grade* mode the finalize page
is accessible all the time, because the review will receive no grade. In the
*Sum* and *Mean* modes the finalize page is accessible once the reviewer has
chosen one phrase for every criteria and defined the grade for every page.

.. warning::

  Moving to the finalize page finalizes the review and the previous pages can no
  longer be edited. Finalization can be cancelled on the Finalize page, but that
  will destroy all the changes the reviewer has done at the Finalize page.

Plain text
..........

The review is done by clicking a fitting phrase under criterion. Once the phrase
has been clicked, it will be added to text field on the right side of page and
its associated grade is taken into account when calculating the final grade.
The reviewer can add multiple phrases per criterion to text field, but only the
last one's grade will be acknowledged. Therefore choosing only one phrase is
recommended, if you use phrases with grades. At least one phrase must be chosen
from every criterion to finalize the review. The phrases can be modified and
more comments can be added by writing in the text field.

If the rubric defines feedback categories, there will be one separate text field
for each category present in the page. The phrases will be directed to the right
text field. If feedback categories are defined, contents of text fields will be
shown as their own sections in the final text. Otherwise phrases will be
arranged by page they were on.

.. image:: /images/rubyric-review-plaintext.png
  :align: center

Annotation
..........

An *annotation review* is done by dragging fitting phrases to the submission.
This helps the reviewer to indicate which particular part their comment
concerns. Alternatively, in the mean mode, the reviewer can click on a grade
or points of phrase to select it. However, if the phrase is not dragged to the
submission, the student cannot see it. More comments can be added by clicking
the place you want to add them to. The comments can be modified by clicking on
the text on them and modifying the text. The comments can be deleted by clicking
the small cross in the bottom right of the comment. The feedback categories
do not have much effect in annotation reviews. On the Finalize page, the
reviewer can write some final feedback on text field.

.. image:: /images/rubyric-review-annotation.png
  :align: center

Sending reviews
...............

At the assignment page, the instructor can choose reviews they want to deliver
to students. If submission has been made through A+, the review should be
delivered back to A+. If submission is a "regular submission", meaning it is
not connected to A+, the review will be sent to the student's e-mail address.
The review will be delivered in both cases with slight delay, during which
the review will be shown with status "mailing". After a little while the status
should be changed to "mailed" and the review should have been delivered.
If necessary, reload the page to see the status change.

When delivering reviews to A+, Rubyric needs to choose the number of points 
associated with review text. If the grade is numerical the points will be set 
to its value. The points will be scaled according to maximum grade of exercise 
at Rubyric and maximum points at A+ exercise when the points are delivered. If
the submission has several reviews you want to deliver, e.g. when using peer 
review, you can choose either to send the best grade or average of grades of 
reviews. Feedback from all chosen reviews for the submission will be included 
regardless of which you choose. Non-numerical grades, e.g. "Failed" or 
"Boomerang", cannot be sent to A+. Thus non-numerical grades will be ignored
when calculating the sent points although the feedback text will still be 
delivered.
