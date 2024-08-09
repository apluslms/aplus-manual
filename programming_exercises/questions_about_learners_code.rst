Questions about learners' code
==============================

This chapter demonstrates how to use the `questions about learners' 
code <https://github.com/apluslms/grader_qlc>`_ (QLC) feature to 
automatically generate questionnaires about details of the student's 
own solution to an exercise. If a followup QLC questionnaire has been
configured, after getting full points in an exercise, the student will
be presented with a generated questionnaire with questions about their
own code.


QLC pre-requisite configuration
-------------------------------

The initial setup to enable the system requires a
couple of steps as described in https://github.com/apluslms/grader_qlc
and https://github.com/apluslms/grader_qlc/tree/main/aplus_followups,
but below are the steps summarised.

1. Clone the grader_qlc repository anywhere on your machine:
   
   ``git clone https://github.com/apluslms/grader_qlc.git /tmp/grader_qlc``

2. Copy the ``aplus_followups`` directory from the repository to your
   exercise directory:
   
   ``cp -r /tmp/grader_qlc/aplus_followups <course-dir>/exercises/followups``

3. Copy the ``followups.js`` file to your static files:
   
   ``cp <course-dir>/exercises/followups/followups.js <course-dir>/_static/followups.js``

4. Add the following line to your course's HTML template, e.g. to 
   ``<course-dir>/_templates/layout.html``:
   
   ``<script src="{{ pathto('_static/followups.js', 1) }}" data-aplus></script>``

This will enable you to use QLC followup exercises anywhere on the course.

Enabling QLC for an exercise
----------------------------

1. In your exercise's yaml configuration file:

   * Use ``apluslms/grade-python:3.11-4.9-4.9u1`` or newer as the grading image
   
   * Prefix your grading command with ``qlc_wrap``, e.g. if your command is
     ``/exercise/run.sh``, change it to ``qlc_wrap /exercise/run.sh``
   
   * Add a ``qlc`` section:
     
     .. code-block:: yaml
        
        # ... other parts as before
        container:
          # ... as instructed
        qlc:
          cmd: ["qlcpy", "--json", "-un", "5", "submitted_file_name.py"]
     
     Further configuration options for the ``qlcpy`` command are listed 
     `here. <https://github.com/apluslms/grader_qlc?tab=readme-ov-file#configuring-an-exercise>`_
     
2. In your chapter rst, include a followup section right after the exercise:
   
   .. code-block:: rst
      
      Submit the programming assignment
      ---------------------------------
      .. submit:: hello_world 75
        :config: exercises/hello_world/config.yaml

      Follow up questions
      -------------------
      .. submit:: followup 15
        :ajax:
        :config: exercises/followups/config.yaml

Python example
--------------

Here is an example file you can submit for the exercise below:

.. include:: ../exercises/qlc_python/sample.py
  :code: python

The exercise below has been configured to give full points on any
(valid) python file to always generate the followup questinnaire.

.. submit:: python 10
  :config: exercises/qlc_python/config.yaml

After getting full points from the exercise above, questions about the
submitted code will be generated below. The followup exercise must be 
the next exercise in the chapter's material.

.. submit:: followup 15
  :ajax:
  :config: exercises/followups/config.yaml

