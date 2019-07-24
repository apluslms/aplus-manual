Acos - Advanced Content Server
==============================

Acos server and related sub-projects are a method of distributing browser-based smart learning content in a reusable and interoperable way. Activities created using the Acos server can be embedded both in A+ and MyCourses.

The project homepage can be found at https://acos.cs.aalto.fi/.

The source code is available in GibHub: https://github.com/acos-server/acos-server.


Example activities
------------------

The following Acos activity types were illustrated in an A+ workshop on May 30, 2018.

jsparsons-python 
  Example exercise for constructing Python code by dragging code elements.

  https://acos.cs.aalto.fi/html/jsparsons/jsparsons-python/ps_simple_function

draganddrop (content type)
  This page contains instructions and notation for using this content type.
  
  https://github.com/acos-server/acos-draganddrop
  

draganddrop-example (content package)
  Basic example exercises illustrating various features of the drag-and-drop content type.
  
  https://github.com/acos-server/acos-draganddrop-example


draganddrop-english (content package)
  A more advanced example illustrating how drag-and-drop activity type can be used in teaching writing.

  https://acos.cs.aalto.fi/html/draganddrop/draganddrop-english/given_new-SNA


pointandclick (content type)
  This page contains instructions and notation for using this content type.
  
  https://github.com/acos-server/acos-pointandclick

pointandclick-example (content package)
  Basic example exercises illustrating various features of the point-and-click content type.
  
  https://github.com/acos-server/acos-pointandclick-example


Embedding Acos activities into A+
---------------------------------

You can add Acos exercises to A+ with the ``submit`` RST directive. Specify the URL of
the exercise in the Acos server using the ``url`` option. The ``ajax`` option is used to
update the exercise points bar in the A+ page since the submission is uploaded directly
to the Acos server instead of via A+. There is an alternative to using the submit directive
since specifying the full URL of the exercise becomes awkward when one needs to test
exercises locally before deploying them to the production server.

.. code-block:: rst

  .. submit:: 1 150
    :title: Reveal demo
    :url: https://acos.cs.aalto.fi/aplus/draganddrop/draganddrop-example/revealdemo
    :ajax:


Alternatively, a custom submit directive may be used in order to avoid specifying
the domain in the URL of the Acos exercise. As a result, it is easy to change
the location of the Acos server without modifying all submit directives of the
Acos exercises in the course. This is useful when Acos exercises are first tested
locally with ``localhost`` URLs and then deployed to a production server.
The custom ``acos-submit`` directive has been installed in this course.
It enables the ``ajax`` option automatically so it need not be given.

The ``acos-submit`` directive uses the setting ``acos_submit_base_url`` (in the project's ``conf.py`` file)
to define the base URL of Acos server, for example,
``"https://acos.cs.aalto.fi"`` or ``"http://172.21.0.4:3000"``.
The ``url`` option in the directive only defines the URL path of the exercise without the domain.

.. code-block:: rst

  .. acos-submit:: 1 150
    :title: Reveal demo
    :url: /aplus/draganddrop/draganddrop-example/revealdemo

.. _acos-docker-mac-windows:

Docker and Mac or Windows computers
-----------------------------------

When running this manual course with Docker in Mac or Windows computers,
the URLs pointing to the Acos server in the Acos exercises may not function
correctly. On Mac and Windows, Docker runs containers inside an additional Linux
virtual machine. Due to the virtual machine between the Mac/Windows host machine
and the containers, the host machine can not reach the containers with their internal
IP addresses. However, the Acos exercises in A+ require that the user's web browser
can connect directly to the Acos server. A simple fix to this is to use the
internal domain names of the containers in order to connect to them from the host.
This requires some configuration in the host system so that it recognizes those
domain names and associates them with the localhost loopback address (the system
itself). Since docker-compose.yml sets port forwarding to the containers,
the host can connect to the containers using the localhost address with the
correct port number.

The localhost address can not be used directly in the exercise URLs since the
loopback address always refers to the container itself initiating a connection,
but the containers need to be able to connect to each other. Therefore,
the containers must use the internal domain names in the exercise URLs, and
the host (web browser) may connect to the containers using the localhost address
with port forwarding.


Mac computers
~~~~~~~~~~~~~

The following has been tested in the macOS High Sierra operating system.
You need to modify your ``hosts`` file settings at ``/private/etc/hosts`` by
adding these lines at the end of the file::

  127.0.0.1  acos
  127.0.0.1  plus
  127.0.0.1  grader

To ensure that the new settings work properly, you may also need to flush the
DNS cache by executing ``sudo killall -HUP mDNSResponder``.

In addition, the ``conf.py`` needs to modified as follows:

.. code-block:: python

  # comment out the existing line that sets acos_submit_base_url and add the following:
  # local testing in containers
  acos_submit_base_url = 'http://acos:3000'

After modifying the settings, execute ``./docker-compile.py``. More detailed information
about modifying the ``hosts`` file can be found at
https://www.imore.com/how-edit-your-macs-hosts-file-and-why-you-would-want and
https://www.tekrevue.com/tip/edit-hosts-file-mac-os-x/.

Linux computers
~~~~~~~~~~~~~~~

In Linux computers, it is possible to use the internal IP addresses of the
containers in order to connect to them from the host machine. However,
if you want to use the domain names of the containers instead of the IP addresses,
you may apply the instructions of the Mac section above with slight modifications.
The hosts file is usually ``/etc/hosts`` in Linux and there is no need to flush
any DNS cache after modifying it.

Windows computers
~~~~~~~~~~~~~~~~~

The A+ containers have not yet been properly working in Windows. If they work
correctly otherwise, but the Acos exercise URLs do not, then you could modify
the hosts configuration so that the internal domain names of the containers
are mapped to the localhost address. The conf.py file is modified like in the
Mac section above.

These linked instructions have not been tested and you may search the web for more instructions.

- https://gist.github.com/zenorocha/18b10a14b2deb214dc4ce43a2d2e2992


Installing Acos locally
-----------------------

If you use Docker, you do not need to install Acos server locally in your computer.

If you still want to install the Acos server locally in your computer, you need
to install Node.js (version 8 LTS) and NPM first.
Then you clone the acos-server git repository::

  git clone https://github.com/acos-server/acos-server.git

You can install dependencies of the Acos server and other content types and
content packages with NPM (in the acos-server directory)::

  npm install
  # install other packages according to your needs
  npm install acos-pointandclick
  npm install acos-pointandclick-example

Run the Acos server with::

  node bin/www

Enter the address ``http://localhost:3000`` in your web browser.


..
  Workflow for generating drag-and-drop activities
  ------------------------------------------------
  TO BE ADDED

