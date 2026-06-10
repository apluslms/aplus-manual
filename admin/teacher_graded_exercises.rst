Teacher-graded exercises
========================

.. styled-topic::

  Main questions:
      How to create exercises that are graded only by teachers via the API
      with students unable to submit directly?

  Topics?
      The ``noSubmission`` exercise type, teacher submissions via API

  What you are supposed to do?
      Create a teacher-graded exercise configuration

  Difficulty:
      Easy.

  Estimated working time:
      10 min.


Overview
--------

The ``access.types.stdsync.noSubmission`` exercise type is designed for
assignments where:

- Students cannot submit answers directly through the A+ user interface or API
- Teachers grade submissions exclusively through the `Batch assess` button on the Participants page (easiest)
  or manually via `Edit course → Batch assess` or the A+ API
- The exercise displays instructions and information to students
- Max points are defined for grading purposes

This is useful, for example, for tracking class attendance or other work
that is collected outside the A+ system (e.g., by email or through a different platform)
and later graded by instructors through the A+ API.

Configuration
-------------

Creating a teacher-graded exercise requires only a few essential settings in
your exercise configuration file:

.. code-block:: yaml

  ---
  title: Class Attendance
  description: Class attendance tracking exercise
  max_points: 50
  view_type: access.types.stdsync.noSubmission

  instructions: |
    <h2>Class Attendance</h2>
    <p>
      This exercise is graded by the course staff only. You cannot submit an answer
      through this interface.
    </p>
    <p>
      Class attendance will be tracked through a separate system.
    </p>

The required fields are:

- **title**: The exercise title shown to students
- **max_points**: The maximum points for this exercise
- **view_type**: Must be set to ``access.types.stdsync.noSubmission``

Optional fields:

- **description**: A short description of the exercise
- **instructions**: HTML instructions for students explaining how to submit
  (since they cannot submit through A+, you should explain the alternative
  submission method if there is one)
- **template**: Custom template name (defaults to ``access/no_submission_default.html``)

The RST configuration for a ``noSubmission`` exercise looks like this:

.. code-block:: rst

  .. submit:: exercise_key 50
    :config: path/to/config.yaml
    :quiz:

The ``exercise_key`` is a unique identifier for the exercise, and ``50`` is the max points.
The config path points to the YAML file containing the exercise configuration as shown above and the ``:quiz:``
option makes it so that A+ shows the staff feedback for the exercise after grading, instead of the exercise title,
description and instructions. The ``:quiz:`` option can be omitted if you want to always show the exercise details
(in that case the staff feedback will only be visible when viewing a specific submission).

How it works
------------

1. **Student view**: When a student visits the exercise page they will see:

   - An alert message stating the exercise is graded by course staff only
   - The exercise instructions (from the ``instructions`` field)
   - No submission form or input fields

2. **Teacher grading**: Teachers grade submissions via the `Batch assess` button on the Participants page (easiest)
   or manually via `Edit course → Batch assess` or the A+ API:

   .. code-block:: bash

      curl -X POST https://plus.cs.aalto.fi/api/v2/exercises/<exercise_id>/submissions/ \
        -H "Authorization: Token YOUR_API_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "students": [
            {"id": 123}
          ],
          "points": 45,
          "feedback": "Excellent essay with good citations and critical analysis."
        }'

   See `A+ REST API <https://plus.cs.aalto.fi/api/v2/>`_ for more details.

Example
-------

Here is a functional example of a teacher-graded exercise:

.. submit:: teacher_graded 50
  :config: exercises/teacher_graded/config.yaml
  :quiz:

This creates a 50-point exercise that students can view but cannot submit through the A+ user interface or API.

Configuration details
.....................

The exercise configuration shown above (in ``exercises/teacher_graded/config.yaml``) contains:

.. code-block:: yaml

  ---
  title: Teacher-graded essay exercise
  description: An essay exercise where students cannot submit but teachers grade via the API
  max_points: 50

  view_type: access.types.stdsync.noSubmission

  instructions: |
    <h2>Essay Assignment</h2>
    <p>
      This is a teacher-graded exercise. You cannot submit your answer directly through
      this interface. Your essay will be collected and graded by the course staff.
    </p>
    <p>
      Please follow these instructions:
    </p>
    <ul>
      <li>Write a 2-3 page essay on the given topic</li>
      <li>Use proper academic formatting and citations</li>
      <li>Submit your essay through email to the course staff</li>
    </ul>

When you use this exercise type:

- The exercise appears in the course module but does not include any submission form or input fields
- Students can see the instructions and are informed that the exercise is graded by course staff
- Students cannot submit answers through the A+ interface or API
- A teacher grades the work through the API
