Development on Apple macOS computers
====================================

.. styled-topic::

  Main questions:
    How do I get the local development environment working on an Apple macOS computer?

  Topics:
    In this section, we will present the following topics:

    * `A+ Docker containers and macOS`_
    * `Troubleshooting`_

  Material:
    In this chapter, we do not provide additional material.

  Requirements:
    These instructions only apply to computers with the macOS operating system.
    Therefore, you should have an Apple computer.

  Estimated working time:
    From 10 min to 30 min.


A+ Docker containers and macOS
------------------------------

A+ works out-of-the-box on macOS, except for the MOOC-Grader, which is used for fetching and automatically grading
assignments. Getting MOOC-Grader to work requires some extra configuration in the course's ``docker-compose.yml`` file.
The next section introduces a ``socat`` solution that fixes the problems with the Unix sockets that behave differently
on "Docker Desktop for Mac" than Linux/Ubuntu.

Configuration of the A+ Docker containers on macOS for local testing and development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that you have installed `Docker Desktop for Mac <https://docs.docker.com/desktop/install/mac-install/>`_
and opened the application before trying to run the A+ Docker containers.

Open the ``docker-compose.yml`` file after you have cloned the course repository from Git.

Add the following under the service ``grader`` (indented inside the grader service settings):

.. code-block:: yaml

  environment:
    - DOCKER_HOST=tcp://socat:2375
  links:
    - socat

Add a new service in ``docker-compose.yml`` after the existing services (``plus`` and ``grader``):

.. code-block:: yaml

  socat:
    image: alpine/socat
    command: TCP4-LISTEN:2375,fork,reuseaddr UNIX-CONNECT:/var/run/docker.sock
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    expose:
      - "2375"

Your ``docker-compose.yml`` file should now look similar to the following example:

.. code-block:: yaml
  :emphasize-lines: 16, 17, 18, 19, 29, 30, 31, 32, 33, 34, 35

  version: '3'

  volumes:
    data:

  services:
    grader:
      image: apluslms/run-mooc-grader:1.19
      volumes:
        - data:/data
        - /var/run/docker.sock:/var/run/docker.sock
        - /tmp/aplus:/tmp/aplus
        - .:/srv/courses/default:ro
      ports:
        - "8080:8080"
      environment:
        - DOCKER_HOST=tcp://socat:2375
      links:
        - socat
    plus:
      image: apluslms/run-aplus-front:1.19
      volumes:
        - data:/data
      ports:
        - "8000:8000"
      depends_on:
        - grader
        - redis
    socat:
      image: alpine/socat
      command: TCP4-LISTEN:2375,fork,reuseaddr UNIX-CONNECT:/var/run/docker.sock
      volumes:
        - /var/run/docker.sock:/var/run/docker.sock
      expose:
        - "2375"
    redis:
      image: redis:6
      command: redis-server --save 60 1 --loglevel warning

When you open the A+ site in the web browser (address http://localhost:8000/) you should now
be able to view and submit assignments and also receive the feedback in A+.

Troubleshooting
---------------

If you receive a ``PermissionError`` from the MOOC-Grader container after starting the A+
containers with ``docker-up.sh``, you may need to change the owner of the Docker socket
(Unix socket, a file in the filesystem) inside the MOOC-Grader container.

First, run ``docker-up.sh`` in a terminal. Then, open the grader command-line in another terminal and change
the Docker socket owner:

.. code-block:: bash

  docker exec -it aplus_grader_1 /bin/bash
  chown grader /var/run/docker.sock

The MOOC-Grader Docker socket permissions are now fixed on macOS and you should be able to view
and submit assignments and also receive the feedback in A+.
