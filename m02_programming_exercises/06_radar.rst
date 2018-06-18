Exercises with automatic similarity analysis
============================================

It is possible to enable automatic program code similarity analysis for programming exercises by adding the `Radar`_ web service for an A+ course instance.
When enabled, Radar will periodically fetch new submissions using the A+ API, and perform syntax level similarity analysis for the submissions.
The results can be viewed using the Radar UI, accessible via the A+ menu.

.. admonition:: Configuration
    :class: default

    Radar is not yet available as a Docker container, and therefore requires manual configuration in order to be used with the exercises on this course.

The following exercises are identical to the example exercises from chapter 2.2, except that we have specified the programming language used in the exercise by using the key ``radar_tokenizer`` in the ``submit`` rst directive.
Radar will track all submissions to exercises that have defined a valid language using the ``radar_tokenizer``.
Additionally, we specified the optional ``radar_minimum_match_tokens`` to lower the match length threshold in order to produce matches of the trivially short hello world exercises.
This option defaults to an arbitrary, empirically chosen value of 15, and can be adjusted if the user feels that there are too many or too few matches.

You can try the service by e.g. logging in with two different accounts and submitting the same solution using both accounts.
Then, using a teacher account, inspect the results in the Radar service.

.. submit:: python_radar 10
    :config: exercises/hello_python/config.yaml
    :radar_tokenizer: python
    :radar_minimum_match_tokens: 1

.. submit:: scala_radar 10
    :config: exercises/hello_scala/config.yaml
    :radar_tokenizer: scala
    :radar_minimum_match_tokens: 1

.. submit:: javascript_radar 10
  :config: exercises/hello_javascript/config.yaml
  :radar_tokenizer: js
  :radar_minimum_match_tokens: 1

.. _Radar: https://github.com/Aalto-LeTech/radar
