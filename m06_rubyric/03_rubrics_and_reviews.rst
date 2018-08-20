Rubrics and Reviews
===================

.. styled-topic::

  Main questions:
      How to create rubrics and how reviewing submissions work

  Topics?
      Creating rubric and reviewing submissions

  Difficulty:
      Easy

  Laboriousness:
      ???

Rubrics
-------

Settings
........

Rubyric rubrics have four grading modes: No grade, Mean, Sum and Always pass
(only lti exercises). No grade mode does not give any grade for the submission
instead it gives pure textual feedback. Normal requirements to finalize the
review don't hold and review can be finalized at any point. In mean mode you can
define set of grades that can be either numbers or strings. You set grade to the
feedback phrases and at end of each page mean of grades is calculated. Rubyric
offers the mean as a suggestion although reviewer can also choose one of the
other given grades for the page. At the final page of review reviewer chooses
the final grade. If set of grades are "Good", "ok" and "Needs improvement" (in
this order), the mean of "Good", "ok", "Needs improvement", "Needs improvement"
and "Good" is "ok". In sum mode the final grade is sum of given points.

You can also define feedback categories if you wish to but you don't need to.
Feedback categories can be for example "Strengths", "Weaknesses" and "Other".
In plain text reviews chosen feedback phrases are sorted by by their chosen
category. In final text everything written under one category is collected
together.

.. image:: /images/rubyric-rubric-settings.png

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

Review type is defined in exercises settings as Review mode and is chosen when
you create the exercise. It can be changed afterwards but the change will not
have any effect on reviews that have already been started. You can generate
example submissions from fake students to test out reviewing and your rubrics.
You can do this by pressing generate example submissions at exercise view.
Button should be on display if exercise hasn't yet received any real
submissions. Generate example submissions is also found at dropdown at top right
of exercise page.

Reviews have several different statuses. Started means that review has already
some content but is not yet finished. Finished means that review is done and
it is ready to be delivered. Mailed means that review has been delivered to
student. Finished status can be achieved by reaching finalize page while
reviewing. In no grade mode finalize page in accessible all the time as review
will receive no grade. In sum and mean modes finalize page is accessible once
reviewer has chosen one phrase for every criteria and defined grade for every
page.

.. warning::

  Moving to finalize page finalizes the review and previous pages can no longer
  be edited. Finalization can be cancelled, however that will destroy all
  changes reviewer has done to the final text on finalize page.

Plain text
..........

The review is done by clicking fitting phrase under criterion. Once phrase has
been clicked it will be added to text field on the right side of page and its
associated grade is taken into account when calculating the final grade.
Reviewer can add multiple phrases per criterion to text field but only last
one's grade will be acknowledged thus choosing only one is recommended. At least
one phrase must be chosen for every criterion to be able to finalize the review.
Phrases can be modified and more comments can be added by writing in the text
field.

If rubric defines feedback categories there will be one separate text field for
every category present in the page. The phrases will be directed to the right
text field. If feedback categories are defined contents of text fields will be
shown as their own sections in the final text, otherwise phrases will be
arranged by page they were on.

.. image:: /images/rubyric-review-plaintext.png

Annotation
..........

Annotation review is done by dragging fitting phrases to the submission.
Alternatively in mean mode reviewer can click on grade/points of phrase to
choose it. However if phrase is not dragged to the submission students cannot
see it. More comments can be added by clicking the place you want to add them
to. The comments can be modified by clicking on the text on them and modifying
the text. They can be deleted by clicking the small cross in the bottom right of
the comment. Feedback categories don't have much effect in annotation reviews.
On finalize page reviewer can write some final feedback on text field.

.. image:: /images/rubyric-review-annotation.png

Send reviews
............

At assignment page instructor can choose reviews they want to deliver to
students. If submission has been made through A+, the review should be delivered
back to A+. If submission is regular submission, the review will be send to
student's email. The review will be delivered in both cases with slight delay
and review will be shown with status "mailing". After a little while status
should change to "mailed" and review should have been delivered (reload page
to see status change).
