Active elements
===============

Active elements are interactive tools embedded in content chapters that process
user input asynchronously in the same way as exercise graders do. However, active
elements are usually not graded with points. Instead, they are used as
visualizations or other such tools that support the students' learning of the
content.

Active elements consist of input and output elements. The user enters some values
into the input elements and the output elements display feedback from the grader
backend once the asynchronous computation has completed. The computation should
ideally finish within a few seconds since the user is likely waiting for it.
The input and output elements may be scattered around the chapter page since
they do not have to be grouped together. Several input elements may be linked to
the same output element and a single input may be used by multiple output
elements. An output element may also be an input to another output element.

The grading of active elements is configured in the same way as normal
asynchronous exercises (that is to say, similar config.yaml files are used).
Likewise, active elements require a grader program that produces the feedback.
If the grader produces feedback in HTML, the current implementation of active
elements in the A+ frontend requires that the feedback is wrapped in
a ``<div id="feedback">`` element.

The active element RST directives, ``ae-input`` and ``ae-output``, are documented in the
`a-plus-rst-tools <https://github.com/Aalto-LeTech/a-plus-rst-tools#6-active-element-input>`_.


Minimal example
---------------

This active element comprises one input and one output field.
The output simply echoes the input.

.. ae-input:: min_input
  :title: Give some input
  :width: 50%
  :height: 34px
  :class: active-element left

.. ae-output:: min_output
  :config: aelements/minimal/config.yaml
  :inputs: min_input
  :title: Output element
  :width: 50%
  :class: active-element left
