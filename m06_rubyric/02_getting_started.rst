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
You can also choose to use Rubyric through Haka login. Then you don't need to
add it to menu.

TODO: Image of Add menu item

.. warning::

  At Rubyric the account you login with Haka login is not the same account you
  are using when you login through A+. Which means you might not have access to
  same courses with both login methods.

Configure course at Rubyric
---------------------------

Create course and course instance
.................................

Login to Rubyric. Note that course needs to exist
in Rubyric for the LTI login to succeed. Thus you should login for the first
time with Haka login. Choose to create new course. Creating a new course
automatically creates also a course instance for the course. You can create many
course instances to the course. Course instance is part of course while
students, assistants and assignments belong to course instances.

TODO: Image of filled create course form

Choose LTI integration as submission policy if you wish to connect Rubyric and
A+.

Update
......

Next we should add course code and lti settings to your new course. Course
code can be added by choosing Settings under title course. Lti settings are
configured by course instance. To update these attributes choose Settings under
title course instance. You need to fill in lti consumer id and context id to
access the course from A+. You can find the right context id and consumer id at
A+ by choosing Rubyric at the menu and clicking Show shared variables. Consumer
id is shown as oauth_consumer_key and context id as context_id.

TODO: image of shared variables with ids underlined and settings filled


Create assignment
.................

Check out
`LTI configuration in A+ <http://localhost:8000/def/current/m05_lti/configuration/>`_
to find out how to configure LTI exercise in A+. To create exercise to Rubyric
choose create new assignment. Fill in the form. LTI resource link ID should be
same as Resource link id in A+ exercise. You don't have to fill in LTI resource
link ID for peer review and LTI resource link ID for viewing feedback. They are
used if you wish for students to use Rubyric to give peer reviews to each other.
Service url is shown on exercise page after you have created exercise.

TODO: create assignments

Submissions
...........

Once you have configured exercise in both A+ and Rubyric submissions should be
delivered to Rubyric where they can be assessed. The reviews in lti assignment
should be delivered back to A+. If you want students to submit straight to
Rubyric you can provide students with submission url which they can use. In
non-lti course submission url is found where service url would be in lti course.
When using regular submission the review will be delivered to student's email.
