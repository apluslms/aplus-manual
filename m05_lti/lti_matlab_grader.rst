MATLAB Grader exercises
=======================

This documentation explains how to create a new exercise with the proprietary
MATLAB grader service. MATLAB grader is developed by MathWorks and it is
connected to learning management systems via the standard LTI protocol,
version 1.1.


Launching an exercise
---------------------

In the A+ course, you may add new LTI exercises manually or the configurations
may be imported from the MOOC grader (see previous chapters). The following
describes how to add them manually under the "edit course" menu.

1. Add a new learning object
2. Choose 'LTI Exercise'
3. Enter the exercise settings and select 'MathWorks learning tool pilot' (https://learningtool.mathworks.com/launch) as the LTI Service.
   LTI-specific settings "context id", "resource link id", "resource link title", and "service url" can be left empty in order to use the defaults.
4. Launch the exercise

When a teacher launches the exercise for the first time, it initializes the
exercise editor in the MATLAB grader. The teacher may then create the exercise
and save it as final in order to open it to students. Exercises in the draft mode
are not available to students.

Defining the exercise parameters in MATLAB grader
-------------------------------------------------

The MATLAB grader provides an easy-to-use user interface for teachers to develop exercises.
In the MATLAB grader, there are multiple fields to define for the exercise:

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

Examples of these methods can be found in the 'Examples' section below.

Use 'Validate Reference Solution' to check that the reference code and assessments are really working.

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

