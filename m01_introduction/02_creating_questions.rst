Creating exam questions
=======================

This section describes how you can create new exam questions either from scratch or using existing questions that for example have been part of the course.

Creating completely new questions
---------------------------------

The A+ manual has nice intructions how to write your own exercises. For programming exercsies ahve a whole chapter :ref:`programming` for them can instructions for questionnaires are in :ref:`questionnaires` document.

When creating new exercises for an exam it is generally good idea to place them to one folder in the root of your repository. Inside that folder you should organise them based on what's most convinient and logical for your particular course. Examples of good grouping locig are topic, difficulty or if the exam has usually the same structure, you can store all exercises that can be used a first question to  an own folder, all essay questions to another and so on.

All exercises should be their separate files to allow better reusability. For example rst file for questionnaire should contain one  questionnaire directive. Then these exercises can be linked easily to your exam sheet with include directive, e.g. `.. include:: /exercises/example_category/intro_1.rst`. 

This reposotory has some examples of questions and how they should be stored in the exercises -folder.

Using old questions
-------------------

You likely have exercises that you have used in your course previously and now would like to use tham in your exam. To reuse them easily, they should be in their own files like described in the previous section. After that they are easy added to your exam with the include directive `.. include:: /module_ex/exercise_4.rst`

This system allows using of old exercises without any copying of files. However the's at least one caveat to this system, exercises cannot modified at all or it will be modified in all instances where it is used. Say you would like to adjust amximum points for an exercise to add or reduce its weight compared to others. After the adjustment all old exams that used the same question semm to have the new points instead of the original. This doesn't however affect previously graded submissions in A+ so you can always check there the original points.