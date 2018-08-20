Getting Started with Rubyric
============================

.. styled-topic::

  Main questions:
      How to create courses and exercises in Rubyric, how they can be linked to
      A+

  Topics?
      Create and modify courses, course instances and exercises

  Difficulty:
      Easy

  Laboriousness:
      An hour at most

Add Rubyric to menu
-------------------

You can login to Rubyric through A+ after adding Rubyric as a menu item. To add
a new menu item in A+ choose Edit course and Menu and press Add new menu item.
You can also choose to use Rubyric through Haka login. In that case you don't
need to add Rubyric to menu.

Configure course at Rubyric
---------------------------

Create course and course instance
.................................

Login to Rubyric. If course has yet to be created at Rubyric when logging in
with lti, you will be redirected to create course form. If logging in with Haka
choose to create new course. Creating a new course automatically creates also a
course instance for the course. There can be several course instances at courses.
To create new course instance to existing course navigate to course by clicking
its name on front page and choose create new course instance. Course instances
have their separate assignments, reviewers and students. Course has the
instructors who have rights to all the courses instances the course have.

Fill in the form. Choose "LTI integration" as submission policy if you wish to
connect Rubyric and A+. "Anybody can submit without authenticating" allows anyone
to submit to assignments after they have provided their email address. "Any
authenticated user can submit" requires students to login to Rubyric before they
submit. When choosing "only enrolled students can submit", instructor needs to
provide list of students who are allowed to submit.

To properly connect Rubyric course to A+ course you need to fill in LTI consumer
ID and LTI context ID. They can be filled in if you have chosen LTI integration
as submission policy. You can find the right context id and consumer id at
A+ by choosing Rubyric at the menu and clicking "Show shared variables".
Consumer id is shown as oauth_consumer_key and context id as context_id.

.. image:: /images/rubyric-create-course.png

.. warning::

  If lti login directs you to create course form again after you have configured
  lti course, there is probably some mistake in LTI context ID or LTI consumer
  ID and you should fix them by updating course instance (See below).

Update
......

You can change course's settings by choosing course and settings under course at
side menu. Courses instance's settings are found by choosing course instance and
settings under course instance from side menu. At course settings you can change
course name and course's contact email as well as assign course code and time
zone. At course instance settings you can change name, language and submission
policy of course instance. You can also make course instance inactive so that it
won't accept any more submissions.

Create assignment
.................

Choose create new assignment. Fill in the form.

You can define deadline for exercises. Students can submit to assignment even
after defined deadline but late submissions will be shown red for reviewers.
Group size defines the size of group allowed to make submissions. Submission
type affects what kind of submissions Rubyric asks for from students. You can
choose submissions to be made as files, written in text area or both together.
Review mode affects on what kind of reviews will be done. More about reviews on
`Rubrics and reviews <03_rubrics_and_reviews>`_. If you cross "Allow reviewers
to send reviews immediately", reviewers are allowed to send reviews back to
students right after finishing review. Otherwise instructors will have to
send reviews afterwards. Rubyric also allows students to conduct peer reviews.
If peer review count is left empty, no peer review is expected. On the other
hand collaborative allows students to construct feedback for each other but they
are not required to review other people's submissions.

Check out
`LTI configuration in A+ <../m05_lti/configuration>`_
to find out how to configure LTI exercise in A+. At Rubyric assignment "LTI
resource link ID" should be same as Resource link id in A+ exercise. You don't
have to fill in "LTI resource link ID for peer review" and "LTI resource link ID
for viewing feedback" unless you want to use Rubyric's peer review or want
students to view the feedback at Rubyric. Service url for assignment is shown on
assignment page after you have created assignment.

.. image:: /images/rubyric-create-assignment.png

Submissions
...........

Once you have configured exercise in both A+ and Rubyric, submissions should be
delivered to Rubyric where they can be assessed.

If you want students to submit straight to Rubyric, you can provide students
with submission url which they can use. Submission url is shown at assignment
page.
