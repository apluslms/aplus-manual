Course settings
===============

.. styled-topic::

  Main questions:
      How to alter the course menu on the left, set deadlines and add
      course staff?

  Topics?
      Course settings in A+

  What you are supposed to do?
      If you have already installed aplus-manual, these features
      should work just ok.

  Difficulty:
      Easy.

  Laboriousness:
      Half an hour.


The course settings page in A+
------------------------------

A+ has a *Course settings page* which is only visible to the teacher. Log in
with an account having teacher privileges. If you want to test this with
aplus-manual, this is the username ``root`` and password ``root``. Next click
the **Edit course** link from the menu on the left as shown in the picture
below.

.. image:: /images/aplus-edit-course-eng.png

\

The course settings page has several tabs.

**Instances** alter the course instances. This is described in the
`earlier chapter <01_setup>`_.

The **Course** tab allows editing the course details.

The fields are in English and quite self-explanatory.

**Visible to students**: this checkbox allows hiding the course from students.
This is useful when you are setting up a new instance of your course on a
production server, but don't want the students to enroll and see the contents
yet.

**Instance name**: this is shown in the list of current and old courses
(``https://aplusdomain/archive``) to distinguish different instances from
each other.

**Url**: this is the identifier of course instance in the A+ url, for example
in URL ``https://plus.cs.hut.fi/a1141/2018/`` the ``2018/`` is the instance.

**Image** is the image showing on the A+ front page. See
`Gallery of features <../m01_introduction/0X_gallery/#front-page>`_ for
an example. With a running copy of aplus-manual, try to set the course image
to file ``fireworks.jpg`` found in the subdirectory ``images`` of the manual.

**Language** is a two-alphabet country code in lowercase, such as ``en``,
``fi``, or ``se``.


Course content visibility and date settings
...........................................



Students enroll to the course in A+. Enrollment is required for submitting
solutions to exercises. Note that there is no integration to other university
systems, such as WebOodi in Aalto University. In case of WebOodi, the student
must both enroll to the course in WebOodi *and* to the course in A+.

**Enrollment starting time** and **Enrollment ending time** in the course
settings indicate when the students can enroll to the course.

**Starting time** and **Ending time** define when enrolled students can submit
exercises and receive automatic grades from them.

The times and dates have the format ``YYYY-MM-DD HH:MM:SS``, that is, year-month-day
hours-minutes-seconds in the 24 hour clock. For example, ``2016-06-01 12:00:00``
means 1st June 2016 Noon.

Enrollment starting and ending times do not need to be enclosed within the
course starting and ending times. If the enrollment starting or ending times are
not defined, the course starting and ending times are used as default values.
Enrollment is possible between the enrollment starting and ending times for the
enrollment audience: logged-in internal or external user (the target audience is
configurable).

The *Allow unofficial submissions* setting in exercise categories enables
students to submit solutions to exercises after the deadline, but those
submissions are unofficial and their points are ignored. The submissions are
stored in the database and the student may view the feedback.

**Lifesupport time**: after this, the model answers are not visibile for
students.

**Archive time** is used to prevent exercise submissions at a certain time.
This is relevant for unofficial submissions.

Chronologically, the times should be set as follows:

::

  Course starting time < course ending time < lifesupport time < archive time



Course content visibility based on audience
...........................................

The view content to setting of a course instance controls who may view the course content.
Alternatives:
Enrolled students
Enrollment audience (internal or external logged-in user; enrollment audience is configured separately)
All registered users (any logged-in user)
Public to internet (anonymous user)

Bug: when set to “enrolled students”, unenrolled logged-in users may still view course content chapters and exercises. They may not open their old submissions, the course materials page nor the course results page, but they see everything on the course front page anyway and they can open the chapters and exercises.


- Enrollment audience: "Paikalliset käyttäjät" means local users. "Ulkoiset
  käyttäjät" means external users, such as students at open Summer courses.
  "Paikalliset ja ulkoiset käyttäjät" means both.

- View content to: "Ilmoittautuneet opiskelijat" is enrolled students,
  "Ilmoittautumisen kohdeyleisö" is potentially enrolling students,
  "Kaikki rekisteröityneet käyttäjät" means all users registered on A+, and
  "Julkisesti internetissä" is publicly visible to the Internet.

- Head urls have description "External CSS and JS resources that will be
  included into course pages. Separate the URLs by a newline."

- Technical error emails has description "The technical errors of the exercises
  will be sent to the course teachers' e-mails by default. If you want to
  override this, write here the actual recipients' e-mails separated by
  commas."

The difference between teachers and assistants is that assistants can view
students' exercise submissions and grade them, but they cannot edit the course.
