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

Rubyric has roles for student, reviewer and instructor. One user can have
different role for different courses, for example user can be student in one
course, reviewer in another and instructor in third.

Students can submit to assignments, view their own submissions and reviews done
to them. If assignment uses peer review or collaborative mode student can also
view and review others' works. User becomes student once they have submitted to
some of course instance's assignments or instructor has added them to the course
instance. Students belong to course instances, not courses.

Reviewer can view and review submissions of groups that have been assigned to
them. Reviewers can view and modify reviews created by themselves. Reviewer is
a role for course instance.

When you create a new course you become instructor for the course. Instructor
has rights to course and all of its course instances. Instructor can create new
course instances and assignments, add instructors for the course and reviewers
for the course instances and also assign reviewers to groups. Instructor can
view all submissions and reviews and review any submission. Instructor has
access to results.

Add reviewers and instructors
.............................

Reviewers can be added on reviewers page and instructors on instructors page.
You need to search user by typing at least part of their name or writing their
email address. Once you find the user you want, click on the button next to user
and choose to add user to role. You can remove user from the role by clicking
the trash can next to user's name (trash can appears only after you reload the
page). If user does not exist yet you can send invitation by giving email
address or you can ask your assistants to log in once so that their account gets
created.

.. image:: /images/rubyric-assign-role.png

Groups
------

Submissions are done in groups which can contain one or more students. One
student can be part of several groups. Instructor can view groups by navigating
to groups page. Groups can be assigned to reviewers who then can view and review
group's submissions.

Assign group to reviewer
........................

At groups page choose 'Assign groups to reviewers'-tab. There you can see all
groups that your course instance has. Group can be assigned to reviewer by
clicking 'Add reviewer'-button on right side of group. Assigned reviewers can be
removed by clicking 'x' next to reviewer's name. There is an option to filter
groups above group list. Groups can be filtered by the assignment they have
submitted something to by choosing assignment name on pressing 'Filter'. You
may also assign several groups at the same time by choosing groups and choosing
option at 'Assign selected groups to'. Once you are done with assigning, press
Save.

.. image:: /images/rubyric-assign-groups.png

Batch upload
............

Batch upload is way to manually provide Rubyric's course instance with the
student list. Students can be given as studentnumber or email. One line equals
one group. You can also assign reviewer with batch upload by adding reviewer at
end of the line after semicolon ';'. Group members are separated by comma ','.

.. image:: /images/rubyric-batch-upload.png

In the above example first group consist of students with studentnumbers
'00001' and '00002' and it has reviewer whose studentnumber is '00020'. Batch
upload also adds students with studentnumbers '00003' and '00004' to the course
instance. You can safely upload same list many times as same group won't be
created twice.
