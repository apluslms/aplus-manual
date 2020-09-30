Example Rubyric exercise
========================

The following examples will allow you to submit a test exercise. However, these
exercises will not be reviewed by the A+ team, and you won't get a grade. The
only intention of having these test exercises heres is to show you how the UI of
the Rubyric exercises looks like, and how the settings added in the RST
directives affect the actual Rubyric exercise.

Worth mentioning that the first exercise was set up using only RST, while the
second exercises was set up using a **config.yaml** file. As you can
see both exercises work just fine. However, we **STRONGLY** recommend setting up
your exercises using RST, and avoid the use of the **config.yaml** file.

.. _rubyric-exercise:

.. submit:: rubyric_example 10
  :title: Rubyric example
  :lti: Rubyric
  :lti_aplus_get_and_post:
  :url: /aplus_exercise

.. submit:: rubyric 10
  :config: exercises/hello_rubyric/config.yaml
