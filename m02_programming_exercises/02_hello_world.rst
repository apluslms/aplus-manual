Hello programming
-----------------

This chapter includes two exercises on one page. Questionnaires and
submission forms can exist anywhere and as many on one page as required.
The automatic assessment of a submission is defined in the referenced
YAML file.

The configuration file ``docker-compose.yml`` should look something like this:  

.. code-block:: yaml

  version: '3'
  
  volumes:
    data:
  services:
    grader:
      image: apluslms/run-mooc-grader:1.4
      volumes:
        - data:/data
        - /var/run/docker.sock:/var/run/docker.sock
        - /tmp/aplus:/tmp/aplus
        - .:/srv/courses/default:ro
      ports:
        - "8080:8080"
    plus:
      image: apluslms/run-aplus-front:1.4
      volumes:
        - data:/data
      ports:
        - "8000:8000"
      depends_on:
        - grader
    acos:
      image: apluslms/run-acos-server
      user: $USER_ID:$USER_GID
      ports:
        - "3000:3000"
      # depends_on is only used to control the start-up order of the containers so that
      # the ACOS container would more likely be assigned the IP address hardcoded into the course configuration
      depends_on:
        - plus
        - grader
      #volumes:
      #  - ./_data/acos/:/var/log/acos
  
Note: acos is an optional component used for interactive exercises.

.. submit:: python 10
  :config: exercises/hello_python/config.yaml

.. submit:: scala 10
  :config: exercises/hello_scala/config.yaml

.. submit:: javascript 10
  :config: exercises/hello_javascript/config.yaml

Be careful with the RST and YAML syntaxes. They are too easy to break
with blank space and indentations.
