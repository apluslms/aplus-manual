Roles and groups
================

.. styled-topic::

  Main questions:
      What roles users can have on Rubyric?

  Topics?
      Roles and assigning them.
      Providing student list.
      Assigning reviewers to groups.

  Difficulty:
      Easy

  Laboriousness:
      ???

Roles
-----

Rubyric has three user roles: the *student*, the *reviewer* and the
*instructor*. One user can have different role for different courses. For
example, the user can be a student on one course, a reviewer on another and an
instructor on a third one.

*Students* can submit answers to assignments, view their own submissions and
reviews they have received. If an assignment uses peer review or collaborative
mode, a student can also view and review others' work. A user becomes a student
once they have submitted their answer to some of the assignments of a course
instance, or an instructor has added them to a course instance. Note that
students belong to course instances, not courses.

When you create a new course, you will become the *instructor* for the course.
An instructor has all the rights to course and all of its course instances.
The instructor can create new course instances and assignments, add instructors
for the course and reviewers for the course instances and also assign reviewers
to groups. The instructor can view all submissions and reviews and review any
submission. The instructor has access to results.

A *reviewer* can view and review submissions of groups that have been assigned to
them. The reviewers can view and modify reviews created by themselves. A
reviewer is a role for course instance. The reviewer role is suitable for
teaching assistants who do not need to create exercises and grading rubrics,
but only give feedback for some submissions.


Add reviewers and instructors
.............................

Reviewers can be added on the *Reviewers page* and instructors on the
*Instructors page*. You need to search for an user by typing at least part of
their name or writing their email address. Once you find the user you want,
click on the button next to user and choose to add a role for the user. You can
remove user from the role by clicking the trash can next to user's name
(trash can appears only after you reload the page). If the user does not exist
yet, you can send an invitation by giving an e-mail address, or you can ask
your assistants to log in once so that their account is created.

.. image:: /images/rubyric-assign-role.png
  :align: center

Groups
------

The exercise submissions are done in *groups* which can contain one or more
students. One student can be part of several groups. The instructor can view
groups at the *Groups page*. The groups can be assigned to reviewers who then
can view and review the submissions of the group.

Assigning a group to a reviewer
...............................

At the groups page, go to the tab *Assign groups to reviewers*. There you can
see all the groups that are on your course instance. A group can be assigned to
reviewer by clicking the *Add reviewer* button on the right side of the group.
Assigned reviewers can be removed by clicking the *x* next to the reviewer's
name. The group list can be filtered by the assignment they have submitted
something to by clicking *Filter* on the name of an assignment. You may also
assign several groups at the same time by choosing groups and choosing the
option at *Assign selected groups to*. Once you are done with assigning, click
*Save*.

.. image:: /images/rubyric-assign-groups.png
  :align: center

Batch upload
............

*Batch upload* is a way to manually upload a list of enrolled students to a
course instance in  Rubyric. The students can be given by student number or by
email. One line equals one group. You can also assign reviewers with batch
upload by adding reviewer at end of the line after semicolon ``;``. Group
members are separated by comma ``,``.

.. image:: /images/rubyric-batch-upload.png
  :align: center

|

In the above example, the first group consists of students with student numbers
``00001`` and ``00002``. and it has reviewer whose studentnumber is ``00020``.
The batch upload also adds students with student numbers ``00003`` and
``00004`` to the course instance. You can safely upload same list many times
as same group won't be created twice.
