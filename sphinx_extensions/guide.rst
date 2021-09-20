Making a Sphinx extension work with A+
======================================

*(Written in 8/2021, things might change)*

In the best case scenario, using a Sphinx extension with an A+ course just requires you to ask the people maintaining the A+ server to install your extension and
enabling it in ``conf.py``.
If this change is also added to the :ref:`Docker images used for testing <modifydockerimage>`,
then testing would work as expected: you add the extension to ``conf.py``, and it just works.

If the extension isn't added to the Docker images, testing gets more complicated.

* You may :ref:`install the extension locally <localsphinx>` and compile RST with locally installed Sphinx.
  The Docker container used for compiling can not access the locally installed extension and thus, the container fails to build the course.
* You may include the extension in a subdirectory under the course.
  Then, the course can be built with the Docker container without installing anything new in the container itself.
  See the section `Adding extensions`_.

The rest of the document goes to some detail on how everything works, so that you can troubleshoot in case something goes wrong.
One thing is important enough to state here:

  If the extension uses JavaScript, it will not (as of 14.8.2021) work out of the box.
  The A+ server removes all html tags from the ``<head>`` of the final html page if it does not have the ``data-aplus`` attribute.
  You will have to include the JavaScript yourself: see the section titled :ref:`"including JavaScript" <includejs>`.

Sphinx versions used by a-plus-rst-tools
----------------------------------------

Note that Sphinx extensions need to be compatible with the used Sphinx version.
A-plus-rst-tools itself is one Sphinx extension and A+ courses built in the RST format depend on it.
In other words, the Sphinx version supported by the a-plus-rst-tools restricts other Sphinx extensions.
In addition, old Sphinx versions might not work on the latest Python versions.

* a-plus-rst-tools v1.3 and earlier support only Sphinx v1.6. They work on Python 3.5.
* a-plus-rst-tools v1.4 supports Sphinx v4.1. They work on Python versions 3.7 and later.

Adding extensions
-----------------

- Adding as submodule

  - a-plus-rst-tools works as a submodule
  - You might be able to do the same by including the git repository of an extension as a submodule
  - You will have to add the path to the submodule in ``conf.py`` with the line ``sys.path.append(os.path.abspath('PATH/TO/EXTENSION'))``
  - And add the extension to the list of extensions in ``conf.py``

- Adding as plain files

  - You can just place the files of the extension in your course repository (you should find these from the GitHub repository of the extension)
  - You will have to add the path to the submodule in ``conf.py`` with the line ``sys.path.append(os.path.abspath('PATH/TO/EXTENSION'))``
  - And add the extension to the list of extensions in ``conf.py``

- Installing through pip

  - Here you will need the A+ team to install the extension on their server.
    Otherwise, the course can not be built in the production servers.
  - For building the course locally, either :ref:`install Sphinx locally <localsphinx>` or :ref:`build a new Docker image <modifydockerimage>`.

.. _localsphinx:

Compiling RST locally without docker-compile.sh
-----------------------------------------------

If you compile RST and build the A+ course locally without using Docker and the ``docker-compile.sh`` script,
you need to install a Python virtual environment in your computer and Sphinx in it.
You can also easily install any other Python packages with ``pip`` in the virtual environment.

Create a new Python virtual environment in a directory named ``venv_sphinx`` with these commands.
The command creates the directory ``venv_sphinx`` under the current working directory.
You can name the directory as you wish.

.. code-block:: bash
  :caption: Set up a Python virtual environment in the directory venv_sphinx

  python3 -m venv venv_sphinx
  source venv_sphinx/bin/activate
  pip install --upgrade pip
  pip install --upgrade setuptools
  pip install wheel
  pip install 'Sphinx~=4.1.2'
  pip install 'PyYAML~=5.4.1'

You can activate an existing virtual environment in the current terminal by running ``source path/to/venv/bin/activate``.
You can create multiple virtual environments in different directories.

When the virtual environment is active, you can compile RST text by running the command ``make html`` in the A+ course directory.

.. code-block:: bash
  :caption: Compile RST

  make html
  # or
  make touchrst html

``make touchrst`` touches all RST files so that Sphinx compiles them again.
Otherwise, Sphinx may reuse build output for unchanged files from a previous build.
This may cause issues with exercises since Sphinx is unable to detect changes in the exercise YAML files.
If the RST files are not touched, then changes to exercises may be ignored in the new build.
A clean build can also be forced by deleting the ``_build`` directory first.

.. _modifydockerimage:

Installing new packages in the compile-rst image used by docker-compile.sh
--------------------------------------------------------------------------

If you want to install new (pip) packages to the ``apluslms/compile-rst`` Docker image used by the ``docker-compile.sh`` script,
you need to create a new Dockerfile and build the new image with the ``docker build`` command.

.. code-block:: dockerfile
  :caption: Custom compile-rst Dockerfile

  FROM apluslms/compile-rst:4.1
  RUN pip3 install --no-cache-dir --disable-pip-version-check \
    the_new_package

Build the image with the tag ``apluslms/compile-rst:dev``:

.. code-block:: bash
  :caption: Build a Docker image

  docker build -t apluslms/compile-rst:dev -f Dockerfile .

Modify the ``docker run`` command in the script ``docker-compile.sh`` and set the image to your new image ``apluslms/compile-rst:dev``.

The image exists locally in your computer.
It is also possible to publish it in Docker Hub so that others may easily use the same image.
That requires a user account in Docker Hub.
Read more in the `Docker Hub quickstart guide <https://docs.docker.com/docker-hub/>`_.
Others may also build the image themselves if they have the Dockerfile and Docker installed.

.. _includejs:

Including JavaScript
--------------------

The A+ server removes all html tags from the ``<head>`` of html pages if they don't have the attribute ``data-aplus``
(see https://github.com/apluslms/a-plus/blob/master/doc/CONTENT.md).
You can add these files by adding them in the ``_static`` folder of the course and creating a Jinja2 template that includes them.
The template file must be located in ``_templates/layout.html``.
The following is an example of a template file that extends the Aplus Sphinx theme by including custom JavaScript files in the ``extrahead`` block.

.. code-block:: text

  {% extends "!layout.html" %}

  {%- block extrahead %}

  <script data-aplus="yes" src="{{ pathto('_static/NAME-OF-JS-FILE.js) }}"></script>

  {% endblock %}

Sphinx extensions usually add JS and CSS files with the functions ``app.add_js_file`` and ``app.add_css_file``.
However, a-plus-rst-tools does not include all of those files in the built HTML files.

* A-plus-rst-tools v1.4 includes those files if they have the attribute ``data-aplus``.
  Functions ``app.add_js_file`` and ``app.add_css_file`` may add attributes with keyword parameters (since Sphinx v1.8).
* A-plus-rst-tools v1.3 and earlier do not include those files at all.
  They can be added manually in the course (in ``_templates/layout.html``).

Note that a-plus-rst-tools v1.3 and earlier support only Sphinx v1.6.
A-plus-rst-tools v1.4 supports Sphinx v4.1.

Everything said in this section also holds for CSS files.
You similarly have to add those manually, either as separate files or as part of a global custom CSS file for your course (``html_style`` in ``conf.py``).

Aplus architecture
------------------

The build process of an Aplus page can be thought to work in three steps:

- Sphinx

  - Builds a webpage in ``_build``, with html and static files

- Mooc-grader

  - Processes the files in ``_build`` and serves them
  - Written in Django
  - At localhost:8080 when using testing containers

- Aplus frontend

  - Serves as a front-end for mooc-grader
  - Written in Django
  - At localhost:8000 when using testing containers

If something goes wrong with how your extension works, you might want to investigate which of these steps causes the issue.

Software versions
-----------------

- The docker containers provided for testing might have different versions from the server

  - Python versions might cause issues
  - Sphinx versions might cause issues

- You can change the versions of containers by editing ``docker-compile.sh`` and ``docker-compose.yml``

Troubleshooting
---------------

- Set verbose flags (possibly multiple) in the Makefile, at the point where html processing happens
- Look at the files in ``_build`` vs the files served by mooc-grader vs the files served by aplus-front
- You can try to disable all Aplus related settings (theme, extension) and run the ``sphinx-build`` command yourself (see the Makefile for the syntax)
- Aplus removes all tags in the html head that don't have the ``data-aplus`` attribute
- In the Aplus course page, under the Edit course section, you can look at the build log for the newest version pushed to git

Documentation
-------------

This is a list of documentation that might come in handy if you need to troubleshoot a problem.

- Aplus itself

  - Frontend: See Readme and doc folder at https://github.com/apluslms/a-plus
  - https://github.com/apluslms/mooc-grader
  - https://apluslms.github.io/

- a-plus-rst-tools

  - See README at https://github.com/apluslms/a-plus-rst-tools

- The aplus manual

  - https://plus.cs.aalto.fi/aplus-manual/master/

- Containers

  - For compilation

    - See docker-compile.sh
    - https://github.com/apluslms/compile-rst
    - https://hub.docker.com/r/apluslms/compile-rst

  - For running the servers:

    - See docker-compose.yml
    - https://hub.docker.com/r/apluslms/run-mooc-grader/
    - https://github.com/apluslms/run-mooc-grader
    - https://hub.docker.com/r/apluslms/run-aplus-front/
    - https://github.com/apluslms/run-aplus-front
