Personalized exercises
======================

Personalized exercises contain some parts that are not the same
for every student. Usually, the structure of the exercise is the same
for everyone, but, for example, some input data is different
in each instance of the exercise. The instances are usually
randomly generated. Each student is assigned one instance and
multiple students may be assigned the same instance.
The instance assigned to the student remains the same even after
refreshing the exercise page.

A personalized exercise defines a generator program that generates N instances
to the exercise. The instances are generated before the start of the course.
An instance contains some files that the grader program can
use while grading (the implementation of the exercise may decide freely how
those instance files are used). The instance files may also be used to add content
to the exercise description shown to the student. A student is connected to
one instance (the choice feels random but is based on their user IDs).
It is also possible to force the instance to change for the student, e.g., after
every five submissions ("you get five attempts before you must start over").
That kind of regeneration of the instance is disabled by default.


Example exercises
-----------------

The submit directives below are commented out in the RST code because
personalized exercises require that the instances are generated
beforehand in the MOOC grader. However, the current version of the
``run-mooc-grader`` container does not generate any instances and
thus, the personalized exercises do not work.

.. no :: after submit

.. submit personalized_number 10
  :config: exercises/personalized_number/config.yaml

.. submit personalized_python 10
  :config: exercises/personalized_python/config.yaml
