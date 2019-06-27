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


Course settings page in A+
--------------------------

A+ has a course settings page which is only visible to the teacher. Log in
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

- **Visible to students**: this checkbox allows hiding the course from students.
  This is useful when you are setting up a new instance of your course on a
  production server, but don't want the students to enroll and see the contents
  yet.

- **Instance name**: this is shown in the list of current and old courses
  (``https://aplusdomain/archive``) to distinguish different instances from
  each other.

- **Url**: this is the identifier of course instance in the A+ url, for example
  in URL ``https://plus.cs.hut.fi/a1141/2018/`` the ``2018/`` is the instance.

- Image is the image showing on the A+ front page.

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
