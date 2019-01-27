Hello programming
-----------------

This chapter includes two exercises on one page. Questionnaires and
submission forms can exist anywhere and as many on one page as required.
The automatic assessment of a submission is defined in the referenced
YAML file.

This is the configuration file ``docker-compose.yml`` (the file is shown here using the ``include`` directive):  

.. include:: ../docker-compose.yml
  :code: yaml

Note: acos is an optional component used for interactive exercises.

.. submit:: python 10
  :config: exercises/hello_python/config.yaml

.. submit:: scala 10
  :config: exercises/hello_scala/config.yaml

.. submit:: javascript 10
  :config: exercises/hello_javascript/config.yaml

Be careful with the RST and YAML syntaxes. They are too easy to break
with blank space and indentations.
