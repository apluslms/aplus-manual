First Steps
===========

In the start there was A-Plus.
That was good, but developer though we needed something more.
Thus, MOOC-Grader was created.
Time passed and now we have many micro services that provice our new way of life, A+ LMS.

.. admonition:: File format
  :class: alert alert-info

  Everything is defined in
  `RST syntax <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.


Getting started
---------------

Good way to start is by cloning this repository and working on it.

In aalto, you could use `version.aalto.fi repo <https://version.aalto.fi/gitlab/course/aplus-manual>`_.
Please note that if you don't have access, then you can request one.
In that case, you probably should be part of :code:`apluslms-cs@aalto.fi` email list too.
So, to clone, execute command:

.. code-block:: sh

    git clone git@version.aalto.fi:course/aplus-manual.git
    cd aplus-manual

In public, you could use `github repo <https://github.com/apluslms/course-templates/tree/manual>`_.

.. code-block:: sh

    git clone --branch manual https://github.com/apluslms/course-templates.git
    cd course-templates

Next step, you need to get :code:`a-plus-rst-tools`.

.. code-block:: sh

    git submodule init
    git submodule update

Everytime the rst part changes, you need to recompile it.

.. code-block:: sh

    ./docker-compile.sh

You can start test servers with:

.. code-block:: sh

    ./docker-up.sh

The end
-------

.. image:: /images/apluslogo.png

Above there is an example image.

Final words and end of chapter.
