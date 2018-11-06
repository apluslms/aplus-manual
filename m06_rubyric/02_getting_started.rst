Getting Started with Rubyric
============================

.. styled-topic::

  Main questions:
      How to create courses and assignments in Rubyric? How they can be linked
      to A+?

  Topics?
      Creating and modifying courses, course instances and assignments.

  Difficulty:
      Easy

  Laboriousness:
      An hour at most

Add Rubyric to the course menu in A+
------------------------------------

You can login to Rubyric through A+ after adding Rubyric as a menu item. To add
a new menu item in A+ choose Edit course and Menu and press Add new menu item.
You can also choose to use Rubyric through Haka login. In that case you don't
need to add Rubyric to menu.

Configure course at Rubyric
---------------------------



Create course and course instance
.................................

Login to Rubyric. If course has yet to be created at Rubyric when logging in
with lti, you will be redirected to create course form. When logging in with Haka,
choose to create new course. Create course button might not be visible if you
have previously only been a student or a reviewer in some course. In that case
you can find a "create course" form at
`https://rubyric.cs.hut.fi/course_instances/new <https://rubyric.cs.hut.fi/course_instances/new>`_.

Creating a new *course* in Rubyric automatically also creates a new
*course instance* for the course. There can be several course instances for a
course: if the course is taught every year, each year can be its own instance.
Each course instance have their separate assignments, reviewers and students.
To create a new course instance to existing course, navigate to course by
clicking its name on the front page and click on "Create new course instance".
The *instructors* of the course are persons who have rights to all the
instances of the course.

.. image:: /images/rubyric-create-course.png

Fill in the form. If you wish to connect Rubyric and A+, choose
"LTI integration" as the submission policy. The option
"Anybody can submit without authenticating" allows anyone to submit to
assignments after they have provided their email address. This can be useful
on MOOCs. "Any authenticated user can submit" requires the students to login to
Rubyric before they can submit. When choosing "only enrolled students can
submit", the instructor needs to provide list of students who are allowed to
submit.

To properly connect Rubyric course to an A+ course, you need to fill in the
*LTI consumer ID* and the *LTI context ID*. These can be given, if you have
chosen an LTI integration as the submission policy. You can find the right
context id and consumer id in A+ by choosing Rubyric at the menu, and then
clicking "Show shared variables". The consumer id is shown in A+ as
``oauth_consumer_key`` and the context id is shown as ``context_id``.

If you are redirected straight to Rubyric instead of having chance to
choose "Show shared variables", or you do not want to include the LTI login,
you can try using ``plus.cs`` as consumer id and the address of your course
``plus.cs.hut.fi/something/something/`` as the context id. Notice the missing
``https://`` at the beginning and the slash ``/`` at the end.

.. warning::

  If the LTI login directs you to create course form again after you have
  configured an LTI course, there is probably some mistake in LTI context ID or
  the LTI consumer ID, and you should fix them by updating course instance
  (see below).

Updating the course
...................

You can change the course settings going to the front page of the course on
Rubyric, clicking the link *Settings* under *Course* at the menu on the left.
The settings of the course instance are in the same menu below the corresponding
title *Instance*.

At the *course settings page* you can change the name of the course, as well as
the contact email, the course code and the time zone. At the
*course instance settings* page you can change the name, the language and
the submission policy of the course *instance*. You can also switch the course
instance to *inactive* so that it won't accept any more submissions.

Creating an assignment
......................

Click the name of the course instance at the course front page. Now Rubyric
shows the list of the assignments for this course instance. Click on
*Create new assignment* button to create a new assignment. Fill in the form.

Each assignment must have a unique *name*. You can define a *deadline* for
the exercise. Students can submit to assignment even after defined deadline,
but late submissions will be shown red for reviewers.

The *Group size* settings defines the size of group (persons) allowed to make
submissions. The *Submission type* affects what kind of submissions Rubyric
asks for from students. You can choose submissions to be made as files, written
in text area or both together.

Review mode affects on what kind of reviews will be done. More about reviews on
`Rubrics and reviews <03_rubrics_and_reviews>`_. If you cross "Allow reviewers
to send reviews immediately", reviewers are allowed to send reviews back to
students right after finishing review. Otherwise instructors will have to
send reviews afterwards. Rubyric also allows students to conduct peer reviews.
If peer review count is left empty, no peer review is expected. On the other
hand collaborative mode allows students to construct feedback for each other but
they are not required to review other people's submissions.

Check out the chapter `LTI configuration in A+ <../m05_lti/configuration>`_
to find out how to configure an LTI exercise in A+. At Rubyric, the "LTI
resource link ID" of the assignment should be same as Resource link id in A+
exercise. You don't have to fill in "LTI resource link ID for peer review" and
"LTI resource link ID for viewing feedback" unless you want to use Rubyric's
peer review or want students to view the feedback at Rubyric. The service url
for assignment is shown on assignment page after you have created assignment.

.. image:: /images/rubyric-create-assignment.png

Submissions
...........

Once you have configured exercise in both A+ and Rubyric, submissions should be
delivered to Rubyric where they can be assessed.

If you want students to submit straight to Rubyric, you can provide students
with submission url which they can use. Submission url is shown at assignment
page.
