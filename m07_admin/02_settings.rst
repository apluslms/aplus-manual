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

- **Instances** alter the course instances. This is described in the
  `earlier chapter <01_setup>`_.

- The **Course** tab allows editing the course details.

- The **Index** tab controls how the table of contents of the course is shown
  to the students.

- The **Content** tab allows reorganising the course material and setting its
  availability.

- The **Menu** tab allows adding new items to the course menu on the left.

- The **Tags** tab allows tagging students for specific purposes.

- The **Deviations** tab allows setting deadline deviations for individual
  students.

- The **Batch assess** is left undocumented. It is related to the A+ API.


The Course tab
---------------

The **Course** tab allows editing the course details. The fields are in English
and quite self-explanatory.

**Visible to students**: this checkbox allows hiding the course from students.
This is useful when you are setting up a new instance of your course on a
production server, but don't want the students to enroll and see the contents
yet.

**Instance name**: this is shown in the list of current and old courses
(``https://APLUSDOMAIN/archive``) to distinguish different instances from
each other.

**Url**: this is the identifier of course instance in the A+ URL, for example,
in the URL ``https://plus.cs.hut.fi/a1141/2018/``, the ``2018/`` part is the instance.

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

**Starting time** and **Ending time** define the starting and ending times for
the course. They are also the default opening and closing times for course modules.

The times and dates have the format ``YYYY-MM-DD HH:MM:SS``, that is, year-month-day
hours-minutes-seconds in the 24-hour clock. For example, ``2016-06-01 12:00:00``
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

**Lifesupport time**: after this, the model answers are not visible to students.

**Archive time** is used to prevent all exercise submissions after a certain time.
This is relevant for unofficial submissions.

Chronologically, the times should be set as follows:

::

  Course starting time < course ending time < lifesupport time < archive time


Module (exercise round) open and close times do not need to be enclosed within
the course starting and ending times.

.. admonition:: Bugs (fixed in the Autumn 2019 release)
  :class: warning

  Bug: Student may submit after the archive time if the module is still open.

  Bug: Student can view the exercise model solution after the module deadline
  even if he has a personal deadline extension and may submit and gain points.

  Bug: the module late submission close time may be earlier than the module
  close time, which makes no sense and also allows students to view the model
  solution while the module is normally open.


Student's access to course material over time
.............................................

.. table:: Student's access to course material over time
  :widths: auto

  +-------------------+-------------+--------+---------------------+---------------------+------------------+--------------------+-------------------------+--------------+
  |                   | Before      | Module | After module close  | After module close  | After module     | During personal    | From course lifesupport | After course |
  |                   | module open | open   | (no late sbms)      | (enabled late sbms) | late sbms close  | deadline extension | to archive time         | archive time |
  +===================+=============+========+=====================+=====================+==================+====================+=========================+==============+
  | Can view chapter  | No          | Yes    | Yes                 | Yes                 | Yes              | Yes                | Yes                     | Yes          |
  +-------------------+-------------+--------+---------------------+---------------------+------------------+--------------------+-------------------------+--------------+
  | Can view exercise | No          | Yes    | Yes                 | Yes                 | Yes              | Yes                | Yes                     | Yes          |
  +-------------------+-------------+--------+---------------------+---------------------+------------------+--------------------+-------------------------+--------------+
  | Can submit to     | No          | Yes    | No (1)              | Yes                 | No (1)           | Yes                | Yes/No (2)              | No           |
  | exercise          |             |        |                     |                     |                  |                    |                         |              |
  +-------------------+-------------+--------+---------------------+---------------------+------------------+--------------------+-------------------------+--------------+
  | Can open model    | No          | No     | Yes                 | No                  | Yes              | No                 | No                      | No           |
  | solution          |             |        |                     |                     |                  |                    |                         |              |
  +-------------------+-------------+--------+---------------------+---------------------+------------------+--------------------+-------------------------+--------------+
  | Can view his own  | No          | Yes    | Yes                 | Yes                 | Yes              | Yes                | Yes                     | Yes          |
  | old submissions   |             |        |                     |                     |                  |                    |                         |              |
  +-------------------+-------------+--------+---------------------+---------------------+------------------+--------------------+-------------------------+--------------+


(1) If the category has unofficial submissions enabled, the student may submit but no points will be gained.
(2) Yes, may submit normally if the module is open. Unofficial submissions without points are allowed after the module deadline if the category has enabled unofficial submissions.


Course content visibility based on audience
...........................................

**Enrollment audience** has three options.

- *Internal users* means only internal students of the university may enroll.
- *External users* means the course is MOOC only (users log in with Google accounts).
- *Internal and external users* means both of the above groups can enroll.


The **View content to** setting of a course instance controls who may view the
course content.

Alternatives:

- Enrolled students: this is obvious.
- Enrollment audience: this configured in the setting above.
- All registered users: this is any logged-in user
- Public to internet: anonymous user

.. admonition:: Bug (fixed in the Autumn 2019 release)
  :class: warning

  When set to “enrolled students”, unenrolled logged-in users may still
  view course content chapters and exercises. They may not open their old
  submissions, the course materials page nor the course results page, but
  they see everything on the course front page anyway and they can open the
  chapters and exercises.

**Head urls** define external CSS and JavaScript resources that are included on
all course pages.

**Assistants** is a list of course assistants. The assistants do not need to be
enrolled on the course. To add an assistant, enter their login in form
``user@domain``, for example, ``userid@aalto.fi`` or ``userid@gmail.com``
(not firstname.lastname@aalto.fi).

**Technical error emails**. By default exercise errors are reported to teacher
email addresses. Set this field as comma separated emails to override the
recipients.

The difference between teachers and assistants is that assistants can view
students' exercise submissions and grade them, but they cannot edit the course.


The Index tab
--------------

The **Index** tab controls how main page of the course is shown to the students.

**Index mode** has several options.

- *User results* is an exercise-oriented view. It shows each course module
  (usually a weekly chapter) separately and inside them, the submodules.
  In addition to that, it lists all the exercises on the course, and student's
  submissions and highest scores for each exercise.

- *Table of contents* shows the same information, but without exercises.
  Thus, it is more compact. This is the same view as the `Course materials
  <http://localhost:8000/def/current/toc/>`_ in the course menu.

- *Link to last visited content* allows the student continue from the same
  content submodule they were viewing last time.

**Description** is a text shown on the main page of the course in top of
the index. One can enter either plain text or HTML here.

**Footer** is similarly content shown after the index.


The Menu tab
------------

A+ always shows the following menu items in the course menu on the left side of
the page.

Students see the *Course* menu group, which includes:

- the course main page (a home symbol and course code)
- table of contents (a book symbol and text "Course materials")
- Exercise results for the student

The teacher and assistants see in addition the *Course staff* menu group:

- Participants: enrolled students
- Groups: possible student groups
- All results: table of scores for each student and each exercise
- Visualizations: learning analytics visualisations
- Edit news: add a news item which is shown in the course main page and e-mailed to the enrolled students
- Edit course: the course settings

The **Menu** tab in the course settings allows adding new items to the course
menu. When you click the *Add new menu item* button, a form is shown to
create a menu item.

**Access** defines who can see the menu item.

**Service** allows to define an external web server where A+ links to *and*
which `exchanges data with A+ via the LTI protocol <../m05_lti/introduction/>`_.
Services described in this manual are
`Radar <../m02_programming_exercises/05_radar/>`_ and
`Rubyric <../m06_rubyric/01_introduction/>`_. The Aalto University CS department
also has `Lab Queue (Neuvontajono) <../m01_introduction/0X_gallery/#lab-queue>`_
and Code Vault (Koodisäilö). Also the `Piazza forum <https://piazza.com>`_ has
been used on at least Aalto courses "Data structures and algorithms Y" and
"Tietotekniikka sovelluksissa". Ask for your A+ administrator for adding these
servises for your course.

**Menu url**: if an external service is configured for this menu item in the
Service setting, then a URL starting with ``/`` overwrites path in service URL
and extends it otherwise. Otherwise, a URL starting with ``/`` is absolute
within A+ and relative to the course path otherwise. Note that the URL entered here
can not include scheme or domain.

.. admonition:: Examples of menu urls
  :class: info

  ``m02_programming_exercises/02_hello_world/`` (note: without starting ``/``)
  is the way to make a menu link to a chapter inside the same course.
  If you are running the A+ locally at *http://localhost:8000/*, this menu
  url points to http://localhost:8000/def/current/m02_programming_exercises/02_hello_world/ .

  ``m03_acos/demo_exercises/#point-and-click`` is the same, but with an
  anchor to a header on a specific location on a course page.

  ``/archive/`` trims everything after the domain and port in the url.
  If you are running the A+ locally at *http://localhost:8000/*, this menu url
  points to *http://localhost:8000/archive/*.

  The menu urls for Radar, Rubyric, Piazza, Lab Queue, and Code Vault are left
  empty, because all of these use the LTI protocol and thus they know which
  user and which course should be used.

**Menu group label**: this works wih the **Access** setting as follows.

+------------------+--------------------------+------------------------------+
| Menu group label |  Access                  | Visible result               |
+==================+==========================+==============================+
| (empty)          | All students, assistants | Shown in group "Course" for  |
|                  | and teachers can access  | everyone                     |
+------------------+--------------------------+------------------------------+
| (empty)          | Only teachers and        | Shown in group "Course staff"|
|                  | assistants can access    | for teachers and assistants  |
+------------------+--------------------------+------------------------------+
| (empty)          | Only teachers can        | Shown in group "Course staff"|
|                  | access                   | for teachers                 |
+------------------+--------------------------+------------------------------+
| ``Groupname``    | All students, assistants | Shown between "Course" and   |
|                  | and teachers can access  | "Course staff" in group      |
|                  |                          | "Groupname" for everyone     |
+------------------+--------------------------+------------------------------+
| ``Groupname``    | Only teachers and        | Shown after "Course staff"   |
|                  | assistants can access    | in group "Groupname"         |
|                  |                          | for teachers and assistants  |
+------------------+--------------------------+------------------------------+
| ``Groupname``    | Only teachers can        | Shown after "Course staff"   |
|                  | access                   | in group "Groupname"         |
|                  |                          | for teachers                 |
+------------------+--------------------------+------------------------------+

**Menu icon class**: an icon for the menu item, if needed. Icons add decoration
and help with visual search. The icons are Glyphicons(R) from the Bootstrap web
framework; `see list of icons here <https://getbootstrap.com/docs/3.3/components/#glyphicons>`_.
Enter the individual name of the icon. For example, ``cloud`` or ``hdd`` might
be useful for external cloud storage, ``comment`` for discussion forum such as
Piazza, ``screenshot`` for Radar, ``floppy-disk`` for Code Vault, and
``question-sign`` for the Lab Queue.
