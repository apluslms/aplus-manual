Hello programming
-----------------

This chapter includes two exercises on one page. Questionnaires and
submission forms can exist anywhere and as many on one page as required.
The automatic assessment of a submission is defined in the referenced
YAML file.

If you want to test the programming exercises, you must edit the configuration
file ``docker-compose.yml``: remove comment characters (``#``). Result:

.. code-block:: yaml

    version: '3'

    services:
      grader:
        image: apluslms/run-mooc-grader
        user: $USER_ID:$DOCKER_GID
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
          - /tmp/aplus:/tmp/aplus
          - .:/srv/courses/default:ro
          - ./_data/:/srv/data
        ports:
          - "8080:8080"
      plus:
        image: apluslms/run-aplus-front
        user: $USER_ID:$USER_GID
        volumes:
          - ./_data/:/srv/data
        ports:
          - "8000:8000"
        depends_on:
          - grader

.. submit:: python 10
  :config: exercises/hello_python/config.yaml

.. submit:: scala 10
  :config: exercises/hello_scala/config.yaml

Be careful with the RST and YAML syntaxes. They are too easy to break
with blank space and indentations.
