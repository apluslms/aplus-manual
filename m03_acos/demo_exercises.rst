Examples of Acos exercises
==========================

This page contains examples of various Acos exercises.
When you are running the Acos container locally in your computer,
you may also access these and other demo exercises directly in the Acos server
at http://localhost:3000.

If the exercises on this page do not load in A+, the exercise URLs are
probably broken. In Mac and Windows computers, you can fix the issue by following
the :ref:`instructions <acos-docker-mac-windows>` on the previous page.
In Linux computers, you may either follow the same instructions or set static
IP addresses to the containers in docker-compose.yml. Then the IP address set
in ``acos_submit_base_url`` in the conf.py file corresponds to the real
IP address of the Acos container.
(Conf.py has the following line: ``acos_submit_base_url = 'http://172.21.0.4:3000'``.)
Note that normal A+ exercises may break when you set static IP addresses to
the containers, hence the static addresses should only be used when experimenting
with the Acos exercises.

Static IP addresses are set to containers with the following docker-compose.yml file.
It configures a network and sets a specific IP address to each container in the network.

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
      networks:
        static_net:
          ipv4_address: "172.21.0.2"
    plus:
      image: apluslms/run-aplus-front:1.4
      volumes:
        - data:/data
      ports:
        - "8000:8000"
      depends_on:
        - grader
      networks:
        static_net:
          ipv4_address: "172.21.0.3"
    acos:
      image: apluslms/run-acos-server
      user: $USER_ID:$USER_GID
      ports:
        - "3000:3000"
      networks:
        static_net:
          ipv4_address: "172.21.0.4"
      volumes:
        - ./_data/acos/:/var/log/acos

  networks:
    static_net:
      ipam:
        config:
          - subnet: 172.21.0.0/24


JSVEE program visualization: Python while loop
----------------------------------------------

.. acos-submit:: 1 10
  :title: JSVEE Python while loop
  :url: /aplus/jsvee/jsvee-python/ae_python_while


Parson's problem: Python while loop
-----------------------------------

.. acos-submit:: 2 10
  :title: jsparsons Python while loop
  :url: /aplus/jsparsons/jsparsons-python/ps_python_iteration_addition


Point and click
---------------

.. acos-submit:: 3 10
  :title: Point and click Aalto
  :url: /aplus/pointandclick/pointandclick-example/Aaltodemo

.. acos-submit:: 4 10
  :title: Point and click algorithms
  :url: /aplus/pointandclick/pointandclick-example/Algorithms

.. acos-submit:: 5 10
  :title: Point and click Creative Commons
  :url: /aplus/pointandclick/pointandclick-example/cc-Creative_commons

.. acos-submit:: 6 10
  :title: Point and click commas
  :url: /aplus/pointandclick/pointandclick-example/commas-Commas

.. acos-submit:: 7 10
  :title: Point and click fruit images
  :url: /aplus/pointandclick/pointandclick-example/images-fruit


Drag and drop
-------------

.. acos-submit:: 8 10
  :title: Drag and drop short
  :url: /aplus/draganddrop/draganddrop-example/short

.. acos-submit:: 9 10
  :title: Drag and drop onto text
  :url: /aplus/draganddrop/draganddrop-example/dragontext

.. acos-submit:: 10 10
  :title: Drag and drop long gibberish
  :url: /aplus/draganddrop/draganddrop-example/longgibberish

.. acos-submit:: 11 10
  :title: Drag and drop reveal demo
  :url: /aplus/draganddrop/draganddrop-example/revealdemo

.. acos-submit:: 12 10
  :title: Drag and drop algorithms
  :url: /aplus/draganddrop/draganddrop-example/articles-Algorithms

.. acos-submit:: 13 10
  :title: Drag and drop fruit images
  :url: /aplus/draganddrop/draganddrop-example/images-fruit

