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
It enables the ``ajax`` option automaticaly so it need not be given.

The ``acos-submit`` directive uses the setting ``acos_submit_base_url`` (in the project's ``conf.py`` file)
to define the base URL of Acos server, for example,
``"https://acos.cs.aalto.fi"`` or ``"http://172.21.0.4:3000"``.
The ``url`` option in the directive only defines the URL path of the exercise without the domain.

.. code-block:: rst

  .. acos-submit:: 1 150
    :title: Reveal demo
    :url: /aplus/draganddrop/draganddrop-example/revealdemo


Docker and Mac computers
------------------------

When running Docker in Mac computers, the URLs pointing to the Acos server may not function correctly. This has been the case with the macOS High Sierra operating system. In such case, you may need to modify your ``hosts`` file settings at ``/private/etc/hosts`` by adding these lines at the end of the file:

.. code-block:: sh
  
  127.0.0.1  acos
  127.0.0.1  plus
  127.0.0.1  grader

To ensure the new settings work properly, you may also need to flush the DNS cache by executing ``sudo killall -HUP mDNSResponder``.

In addition, the ``conf.py`` needs to modified as follows:

.. code-block:: sh

  # local testing in containers
  acos_submit_base_url = 'http://acos:3000'

After modifying the settings, execute ``./docker-compile.py``. More detailed information about modifying the ``hosts`` file can be found at https://www.imore.com/how-edit-your-macs-hosts-file-and-why-you-would-want and https://www.tekrevue.com/tip/edit-hosts-file-mac-os-x/.


Installing Acos locally
-----------------------

If you use Docker, you do not need to install Acos server locally in your computer.

TO BE ADDED

Workflow for generating drag-and-drop activities
------------------------------------------------

TO BE ADDED


