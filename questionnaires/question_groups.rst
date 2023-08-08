Question groups
===============

Questions in a questionnaire can be grouped.
It is possible to change normal grading so that
students earn points from a question group only
if they answer all questions inside the question group correctly.
This grading behavior is enabled by the setting ``group_errors``
in the config.yaml file of the questionnaire.

.. admonition:: Broken feature
  :class: danger

  The feature is currently broken.
  Even though they shouldn't,
  students receive points from question groups that have not been fully answered correctly
  and they see which questions were answered incorrectly.

  This will be fixed in August 2023.

.. admonition:: Only YAML
  :class: warning

  Question groups can currently only be defined in the YAML format, not directly in RST directives.


Below, there is an example questionnaire that has two question groups.
The ``group_errors`` setting is enabled in both question groups.
The config.yaml file of the questionnaire is also highlighted below.

.. literalinclude:: /exercises/quiz_question_group/config.yaml
  :language: yaml
  :emphasize-lines: 11,53
  :caption: Example config.yaml file of the questionnaire shown below on this page.


.. rst-tabs::

  .. tab-content:: tab-html-questiongroups
    :title: HTML visualisation

    .. submit:: questiongroups 15
      :config: exercises/quiz_question_group/config.yaml
      :quiz:

  .. tab-content:: tab-rst-questiongroups
    :title: RST code

    .. code-block:: rst

      .. submit:: questiongroups 15
        :config: exercises/quiz_question_group/config.yaml
        :quiz:
