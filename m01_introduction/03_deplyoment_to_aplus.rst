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

For every exam
--------------



In A+ Exam (tentit.cs.aalto.fi):

1. Open your course and go to Exam Management page. Create a new exam session, one for every version of the exam .i.e. if you want to have thre different exams that get randomly served in Exam-room, create three new exam sessions
2. Set the exam session to point to their corresponding "exam paper" (module you created earlier)
3. Set the starting time to the EARLIEST time when the exam can be started
4. Duration should cover the whole period when the exam can be taken. If the exam is taken in Exam-rooms say over an week, set duration to 168 (7 * 24). The duration is in hours.