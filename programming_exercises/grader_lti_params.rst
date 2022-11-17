Using the student's name, student id and email in the grader
============================================================

In MOOC-Grader assignments, it is possible to use the student's name, student id and email address in the grading container.
If an assignment is configured as an LTI assignment, then MOOC-Grader receives personal information
about the student (name, student id, email) via the :abbr:`LTI (Learning Tools Interoperability, a standard protocol)` parameters from the A+ platform.

How to use:

* In the assignment config.yaml settings, set ``lti: Grader``.
* The assignment settings must also set ``lti_aplus_get_and_post`` to ``True``.
* The grading container may read the parameters from the file ``/submission/user/lti.json`` (inside the container).

The JSON object has the following keys:

- ``user_id``
- ``custom_student_id``
- ``lis_person_name_full``
- ``lis_person_name_given``
- ``lis_person_name_family``
- ``lis_person_contact_email_primary``

A+ still uses the A+ grading protocol to connect to the grader,
but the protocol parameters include additional information about the user.
The extra parameters are named after the LTI standard.

Note: MOOC-Grader does not support the full LTI protocol
and you can not use the grader via the standard LTI version.


Example assignments
-------------------

These two assignments read the submitter's name from the ``lti.json`` file in the container and print it in the feedback.

.. submit:: moocgraderltiform 10
  :config: exercises/moocgraderltiparams/config.yaml
  :submissions: 99


.. submit:: moocgraderltifile 10
  :config: exercises/moocgraderltiparams/config_file.yaml
  :submissions: 99

