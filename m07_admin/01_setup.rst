Setting a course on production servers
======================================

This section discusses how to set up a course on a production server. Some
information here might be specific to Aalto University, Gitlab or other
software, not particularly A+ and mooc-grader.


Github hook to mooc-grader
--------------------------

It is possible to create a Github webhook with gitmanager: when you push the
course material to one branch, the server with mooc-grader is automatically
notified and the course will be recompiled there. However, this is out of scope
for this manual. Aalto University has mooc-grader and gitmanager on the
same server, and the web interface of gitmanager shows the update and
compilation log of the course:

.. image:: /images/aalto-gitmanager.png

\

If the compilation is successful, the course should be visible on the server
with url ``https://graderdomain/nameinst/``, where ``graderdomain`` is the
full domain name for the server running mooc-grader, and ``nameinst`` has both
the course name and instance concatenated.

.. image:: /images/course_on_grader_server.png

\

There you will see all the exercises on the course. You can also find the
course configuration URL which is needed for A+. It is typically
``https://graderdomain/nameinst/aplus-json``.

Setting the course on A+
------------------------

Next you have to create the course on A+. If there are no previous course
instances yet, maybe your A+ system administrator will help with it.

If there is an old course instance, go to *the course teacher's view*.

.. image:: /images/aplus-left-menubar-edit-course.png

\

If you have an old instance of the course, go there first. In the menu left you
should have a link "Muokkaa kurssia" (Edit course). It leads to
``https://aplusdomain/name/inst/teachers/``, where ``aplusdomain``
is the full domain name for the server running A+, ``name`` is the short name
of the course and ``inst`` is the name of the most recent instance of the
course. This leads to the following view:

.. image:: /images/aplus-teachers.png

\

Unfortunately, the user interface is currently in Finnish only. Here are the
essential translations:

- Kurssikerrat: course instances
- Kurssi: edit current instance of the course
- Etusivu: edit the front page of the course
- Sisältö: contents of the course
- Valikko: edit the course menu on the left
- Merkinnät: notes for students (unknown)
- Määräajan muutokset: change of deadlines
- Joukkoarviointi: group grading of exercises

Go to the tab "Kurssikerrat" (course instances).

.. image:: /images/aplus-course-instances.png

\

This page shows all instances of the course: The name of the instance,
the instance identifier in the course URL, and the opening and closing time of
the course. In the picture above, the instance named "2018" is chosen. We want
to clone all course modules and exercises to a new course instance. Write the
new *course URL identifier*, like "2019", to the field "Uusi URL-osoitteessa
käytettävä tunniste kurssikerralle:" and click the orange "Kopioi uudeksi
kurssikerraksi" button (copy as a new course instance).

The course data is now copied and you will be directed to the "edit current
instance" tab of the new instance.

.. image:: /images/aplus-edit-course-instance.png

\

This part is documented in the next chapter, `Course settings <02_settings>`_.


Updating the course instance
----------------------------

Sometimes you need to alter the course material when the teaching is already
begun. This means modifying the RST documents, or the exercise descriptions or
unit tests for grading. Normally, you can just push the course material to the
git branch you have set. Only mooc-grader will know about this in this case.

However, if you have add new exercise to the course or alter the opening and
closing dates of the exercises, you have to update the course on A+ as well.
This is done on the "Sisältö" (contents) tab on the teacher's view on A+. The
field "Tuo ja korvaa sisältöasetukset URL-osoitteesta" has the course
configuration URL from mooc-grader, the one having form
``https://graderdomain/nameinst/aplus-json``. Next to it is the button
"Tuo" (import). Click on it and the course configuration will be updated from
mooc-grader.
