Deploying your exams to A+
===========================

First time actions
------------------

If this is your first time using the A+ for exams, follow these intructions closely. We suppose that you are already using A+ for teaching and you have course material stored in Aalto Gitlab. If you are not familiar with the A+ altogether, we recommend you to discuss are support team first (TODO: link / contact info here)

1. In your course repository, create a new branch for exams. e.g.::
    git checkout -b exams

2. Contact A+ admins and ask them to:
* Create new grader for your course and hook it to your course
* Create new course in A+ Exam and set it to use grader created in previous step

3. In your new branch, create a new folder (module) for exams

.. _deployment:

For every exam
--------------

In the exam branch of your course repository:

1. Create a new rst file for your exam. This represents an exam sheet. Name the files appropriately, so that they can stay in git afterwards and be easily accessible for further needs. A suggestion how to name exams is "exam_20191213_a". This format displays the date of the exam and possibile revision easily. See the image below for reference.

.. image:: /images/repo_structure.png

2. Edit the index.rst of your exam module to include only the just created chapter. If you want to have different versions of the exam put each of them to separate modules.

3. Edit master index.rst file in the root of the directory so that only active exams are listed.

In A+ Exam (tentit.cs.aalto.fi):

1. Open your course and go to Exam Management page. Create a new exam session, one for every version of the exam .i.e. if you want to have thre different exams that get randomly served in Exam-room, create three new exam sessions
2. Set the exam session to point to their corresponding "exam paper" (module you created earlier)
3. Set the starting time to the EARLIEST time when the exam can be started
4. Duration should cover the whole period when the exam can be taken. If the exam is taken in Exam-rooms say over an week, set duration to 168 (7 * 24). The duration is in hours.

Archiving old exams
-------------------

It's very good idea to make every new exam to their own files instead of overwriting last exams. This allows easier access to past exams. One good solution to store these exams is to have one additional forlder in the root of the repo calles for example "arcive" where you store all past exams. This way exam modules contain always just the current exam sheet preventing confusion and the used exam sheet won't be distributed between different modules.