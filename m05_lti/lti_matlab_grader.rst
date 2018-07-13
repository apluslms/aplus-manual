Exercise in MATLAB Grader
=========================

This documentation explains how to create a new exercise with the MATLAB grader service.
MATLAB grader is developed by MathWorks and it is connected to learning management
systems via the standard LTI protocol.

Enabling an LTI service in the A+ site
--------------------------------------

An A+ site administrator must first add the LTI service with its credentials to the site and then,
in a course instance, a teacher may add exercises that connect to the LTI service.
The LTI service needs to enabled only once for the site.

The admin interface is located in the URL path `/admin <//localhost:8000/admin>`_.

1. Find "Lti services" under "External services" and click "add".
2. In the form, enter the URL of the service as well as the consumer key and secret.
3. Click "save".

Launching an exercise
---------------------

In A-plus environment:

1. Add a new learning object
2. Choose 'LTI Exercise'
3. Enter the exercise settings and select 'MathWorks learning tool pilot' (https://learningtool.mathworks.com/launch) as the LTI Service.
   LTI-specific settings "context id", "resource link id", "resource link title", and "service url" can be left empty in order to use the defaults.
4. Launch the exercise

Defining the exercise parameters in MATLAB grader
-------------------------------------------------

MATLAB grader provides such an easy user interface for teacher to develop exercises.
In MATLAB grader, there are multiple fields to define for the exercise:

- Title
- Problem Description and Instructions
- Files Referenced
- Problem Type (script or function)
- Code (Reference Solution and Learner Template)
- Assessment

More help is available by clicking ``?`` icon next to each field name.

Next, set up required values.

In *Learner template*, it is possible to lock some rows (click the lock icon). It is helpful when there should be some rows that are not allowed to be edited by the student.

Setting up the assessment
-------------------------

Assessment can be executed with four different type:

- Variable Equals Reference Solution (compares a certain variable to the same variable in the reference solution)
- Function or Keyword is Present (for example, the student's code should have an if-statement)
- Function or Keyword is Absent (for example, the student's code should not have a for-loop)
- MATLAB code (Assessment system includes three built-in functions to check if answer is correct (assessVariableEqual, assessFunctionPresence, assessFunctionAbsence)).

Examples of these methods can be found in 'Examples'.

Use 'Validate Reference Solution' to check that reference code and assessments are really working.

The image shows an example of assessment written in MATLAB code for a function type exercise.
The student's function is called ``newton`` and it is called one hundred times with random input parameters.
The return value is compared to the return value of the reference solution.

.. image:: /images/matlab_grader_assessment.png

Examples
--------

Some examples of different exercise types:

- Example of function: https://plus.cs.hut.fi/test/matlab-test/round1/newtonA/
- Example of script working with function given as a file: https://plus.cs.hut.fi/test/matlab-test/round1/newtonB/
- Example of script to handle images: https://plus.cs.hut.fi/test/matlab-test/round1/kuvankasittely/

Notes
-----

There are currently some issues with grader.

- LaTeX doesn't support ``\matrix``, but matrices can be inserted to the problem description using the LaTeX editor like this:

  .. code-block:: latex
  
    mat=\left\lbrack \begin{array}{cc}
      1 & 2\\
      3 & 4\\
      5 & 6
    \end{array}\right\rbrack

  The matrix above is rendered like this:
  
  .. math::
  
    mat=\left\lbrack \begin{array}{cc}
      1 & 2\\
      3 & 4\\
      5 & 6
    \end{array}\right\rbrack

- Syntax check in the beginning of assessment would be nice. Now syntax errors trigger the first assessment defined by the teacher, which is a little misleading since the syntax error in the submission probably has nothing to do with the first assessment test.

More information and full documentation
---------------------------------------

More information can be found in MathWorks Learning Tool Documentation (in a MATLAB grader exercise, click ``?`` icon next to 'DRAFT').

