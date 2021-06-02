Extending the default feedback template
=======================================

Paths to custom Jinja2 HTML templates that extend or replace the default
template at `graderutils_format/templates/feedback.html
<https://github.com/apluslms/python-grader-utils/blob/master/graderutils_format/templates/feedback.html>`_
can be defined in the **test_config.yaml** as follows:

::

  feedback_template: my_feedback_template.html

.. submit:: template 10
  :config: exercises/template_extension/config.yaml
