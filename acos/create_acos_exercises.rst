Create Acos exercises
=====================

.. styled-topic::

  Main questions:
    How to create and test Acos exercises locally?

  Topics:
    In this section, we will talk about:

    * `Introduction`_
    * `Create an Acos exercise`_
    * `Test Acos activities locally`_
    * `Test Acos activities with Docker`_
    * `Additional resources`_

  Requirements:
    #. You need intermediate to advanced computing and programming skills.
    #. Prior knowledge about npm packages, JSON, HTML, and JavaScript may be beneficial.
    #. :download:`Download  </course_material/acos_drag_and_drop/Acos-drag-and-drop-activity.zip>` the images and code files used
       in this chapter.

  Estimated working time:
    60-90 min.

Introduction
------------
Acos exercises are basically an `npm package <https://docs.npmjs.com/about-packages-and-modules>`_ which, if desired, it can be
published publicly under the npm package manager environment or simply published privately for your own course. Acos exercises
are grouped under the "Acos content packages" as is shown in the :ref:`Acos environment <acos-concept>`. In order words, the Acos
content packages are basically a container for the Acos exercises, which are presented as activities to the end-user.

In this chapter, we will show you how to create a "drag and drop" exercise. Notwithstanding, the concepts as well as the ideas
presented in this chapter are reproducible for creating other types of Acos exercises.

.. figure:: /images/gallery/acos_concept.jpg
  :name: acos-concept
  :width: 60 %
  :align: center
  :class: img-responsive img-thumbnail

  Acos server Team, (2016), **Acos architecture** [ONLINE]. Available at: https://www.npmjs.com/package/acos-server [Accessed 13
  May 2020].

.. _create-acos-exercise:

Create an Acos exercise
-----------------------
Usability aspects
.................
Create an exercise is relatively easy. Basically, you only need to create an HTML file, add the content you would like to have and
finally create a JSON configuration file with the `drag and drop settings <https://github.com/acos-server/acos-draganddrop#notation>`_.
However, the most challenging part is to design the flow and the appearance of your exercises.

.. hint::

  If you want to look for inspiration, you can review some of the `exercises <https://acos.cs.aalto.fi/>`_  that has been
  used in some of the A+ courses.

Unfortunately, we cannot give you suggestions about the usability and the optimal flow of your exercises. Yet, we can provide you
with a list of tools that may help improve the appearance of the Acos exercises. First, we suggest using a CSS framework for
styling your activities such as `Bootstrap <https://getbootstrap.com/>`_, `Material <https://material.io/>`_, or
`Foundation <https://get.foundation/>`_. Secondly, we suggest making use of the
`style editor <https://developer.mozilla.org/en-US/docs/Tools/Style_Editor>`_ embedded in your web browser. Finally, we suggest
researching about `usability <https://www.nngroup.com/articles/usability-101-introduction-to-usability/>`_, especially usability
related to the exercise you are developing. In this case, we should read about the main considerations needed while using
`drag and drop <https://uxdesign.cc/drag-and-drop-for-design-systems-8d40502eb26d>`_ elements.

.. rst-class:: text-end

:glyphicon-info-sign:`\ ` **Read more about**  `How to use the web inspector <https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to>`_

|

Set up your new Acos content package
....................................

Creating Acos exercises only requires you to follow a couple of steps. First, download one of the Acos content packages examples,
published under the `Acos GitHub organization <https://github.com/acos-server/>`_. In this case, we are going to use the
`drag and drop example <https://github.com/acos-server/acos-draganddrop-example>`_. Secondly, read the documentation related to
the content type under which you are going to work. In this case, read the
`Acos drag and drop <https://github.com/acos-server/acos-draganddrop>`_ documentation. Thirdly, edit the source code and create
your own Acos content package. Fourth and last, publish your exercises.

The process of creating Acos exercises looks quite straightforward. However, we have some steps in between that need to be
considered. But do not worry, we will explain those steps in more detail in the following sections of this chapter. For now, let's
start configuring the Acos content package of the `drag and drop example <https://github.com/acos-server/acos-draganddrop-example>`_.

1. Open the ``package.json`` file and change the name of the package. Remember to keep the content type name at the beginning,
   in this case, *draganddrop-* is the name of the package. Therefore, you will have something like
   ``draganddrop-<name-of-your-acos-content-package>``.
2. Change the meta-information declared in the ``index.coffee`` file (name, description, author, version and some other
   information that you consider relevant).
3. Change the namespace of the package declared in the ``index.coffee`` file. Again, remember to keep the content type name at the
   beginning. Therefore, you will have something like ``draganddrop-<name-of-your-acos-content-package>``.
4. Change the name of the module from ``DragandDropExample`` to whichever name you prefer for your exercise, e.g.,
   ``DragandDropDataManagement``.

After making all the changes mentioned above, your ``index.coffee`` should look something like :ref:`the image below <acos-changes>`.
Note that in this example, we did not change the meta-information, but you should change it.

.. figure:: /images/gallery/index.coffee.png
  :name: acos-changes
  :width: 95%
  :align: center

  Diff view. Original file (left) and edited one(right).

Now that you have edited some of the source files, you can proceed to install the ``coffeescript`` module and compile the
``index.coffee`` file. Therefore, you should run the following command in your project directory.

.. code-block:: bash

  npm install

Verify that a ``node_modules`` folder and the ``index.js`` file are created. If the ``index.js`` file is not created, you should
run the following command in your project directory.

.. code-block:: bash

  npm run prepare

Now, if you want to visualise the `drag and drop example <https://github.com/acos-server/acos-draganddrop-example>`_ in your web
browser, you should follow the instructions provided in the :ref:`local-test` or the :ref:`docker-test` sections.

Create your own Acos exercise
.............................
Now that your project has been properly set up, it is time to start creating your own exercise. In this chapter, we will create a mock
data management exercise so that you could follow the process of creating Acos exercise step-by-step. Remember that all the
exercises you want to create should be located inside the ``exercises`` folder. You can also group them and organise them in
subfolders. For example, in the current ``exercises`` folder, there is an ``images`` folder and an ``articles`` folder containing
specific exercises.

For now, let's delete all the current examples and the related static files. Once, the ``exercises`` folder is empty we will start
creating new *XML* and *JSON* files. In this case, we will name the exercises ``data_structure``. Therefore, we will have
two files:``data_structure.xml`` and ``data_structure.json``. Remember, that the name of those files should **NOT CONTAIN**
hyphens and it is preferred to use an underscore to separate words in the name of the files. Finally, we will add our images to
the ``static`` folder, and as an end result, we should have a project structure like the one
:ref:`shown below <acos-exercise-folder-structure>`.

.. code-block:: bash
  :name: acos-exercise-folder-structure
  :caption: Structure of the Drag and Drop exercise.
  :emphasize-lines: 3,4,11-21

  .
  ├── exercises
  │   ├── data_structure.json
  │   └── data_structure.xml
  ├── index.coffee
  ├── index.js
  ├── LICENSE
  ├── node_modules
  ├── package-lock.json
  ├── README.md
  └── static
      ├── data_folder.png
      ├── date_folder.png
      ├── exp_folder.png
      ├── file.png
      ├── link_folder2.png
      ├── link_folder.png
      ├── project_folder.png
      ├── readme.png
      ├── scripts.png
      └── src_folder.png

Now, it is time to add some content to our *XML* and *JSON* files. We will not go into detail about the syntax we used on this
particular example. Nevertheless, you can find more information about the drag and drop syntax in the
`official documentation <https://github.com/acos-server/acos-draganddrop>`_.

For now, the only thing we need to know is that the drag and drop exercises need one *XML* file and one *JSON* file. The *XML*
file contains HTML tags which define the view of the exercise, on the other hand, the *JSON* file contains the configuration of
the of the draggable files, the droppable placeholders defined in the *XML* file, and the feedback. The code below show how the
``data_managment`` mock exercise is implemented. As you can observe, the :ref:`data_structure.xml <data-structure-xml>` file
define the structure of the exercise view and the placeholders of the droppables. On the other hand, the
:ref:`data_structure.json <data-structure-json>` file, has declared the configuration and behaviour of the draggables.

.. hidden-block:: data-structure-xml
  :label: Show/Hide data_structure.xml
  :visible:

  .. code-block:: xml
    :linenos:

    <html>
      <head>
        <style>
      body {
        margin-left: 5px;
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,
        "Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji",
        "Segoe UI Symbol";
        font-size: 16px;
        font-weight: 400;
        line-height: 1.6;
        color: #212529;
        text-align: left;
        background-color: #fff;
      }
      table, th, td {
        border: none;
      }
      table {
        margin-bottom: 0.5em;
      }
      img {
        max-height: 80px;
        width: auto;
      }
      .droppable {
        height: 80px;
        min-width: 80px;
        display: inline-block;
        overflow: hidden;
      }
      .folder-link {
        height: 80px;
        display: table-cell;
        vertical-align: middle;
      }
      </style>
      </head>
      <body>
        <h1>How do we manage multiple versions of data files?</h1>
        <p>Before start working on this exercise, review the
          <a href="https://www.youtube.com/watch?v=3MEJ38BO6Mo">Data Management lecture</a>.
        </p>
        <p>This exercise requires you to organise the project folder in the best possible manner
        by dragging and dropping the files and folder into the correct space.</p>
        <table>
          <thead>
            <tr>
              <th colspan="4">The "Big Picture" project</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <img src="/static/draganddrop-data-management/project_folder.png" alt=""/>
              </td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>
                <img src="/static/draganddrop-data-management/link_folder2.png" alt=""/>
              </td>
              <td>{source:}</td>
              <td>
                <img src="/static/draganddrop-data-management/scripts.png" alt=""/>
              </td>
              <td></td>
            </tr>
            <tr>
              <td>
                <img src="/static/draganddrop-data-management/link_folder2.png" alt=""/>
              </td>
              <td>{experiments:}</td>
              <td>
                <img src="/static/draganddrop-data-management/date_folder.png" alt=""/>
              </td>
              <td>{files:}</td>
            </tr>
            <tr>
              <td>
                <img src="/static/draganddrop-data-management/link_folder.png" alt=""/>
              </td>
              <td>
                <img src="/static/draganddrop-data-management/data_folder.png" alt=""/>
              </td>
              <td>{readme:}</td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td>
                <img src="/static/draganddrop-data-management/link_folder.png" alt=""/>
              </td>
              <td>{date_folders:}</td>
              <td>{files:}</td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td>
                <img src="/static/draganddrop-data-management/link_folder.png" alt=""/>
              </td>
              <td>{readme:}</td>
            </tr>
          </tbody>
        </table>
      </body>
    </html>

.. hidden-block:: data-structure-json
  :label: Show/Hide data_structure.json
  :visible:

  .. code-block:: json
    :linenos:

    {
      "draggables":{
        "source":{
          "content":"<img src=\"/static/draganddrop-data-management/src_folder.png\" alt=\"folder\">",
          "reuse":false,
          "feedback":{
            "folder":"Correct!, this folder contains the source files.",
            "DEFAULT":"This folder only contain the source files."
          }
        },
        "date_folder":{
          "content":"<img src=\"/static/draganddrop-data-management/date_folder.png\" alt=\"folder\">",
          "reuse":false,
          "feedback":{
            "folder":"Correct!, this folder contains information organised by date",
            "DEFAULT":"This folder contains information organised by date."
          }
        },
        "experiment":{
          "content":"<img src=\"/static/draganddrop-data-management/exp_folder.png\" alt=\"folder\">",
          "reuse":false,
          "feedback":{
            "folder":"Correct!, this folder contain the results of different experiments",
            "DEFAULT":"This folder contains the results of different experiments."
          }
        },
        "file":{
          "content":"<img src=\"/static/draganddrop-data-management/file.png\" alt=\"folder\">",
          "reuse":true,
          "feedback":{
            "folder":"Correct!, this is a group of files",
            "DEFAULT":"This is a list of different files."
          }
        },
        "readme":{
          "content":"<img src=\"/static/draganddrop-data-management/readme.png\" alt=\"folder\">",
          "reuse":true,
          "feedback":{
            "folder":"Correct!, This is a readme file",
            "DEFAULT":"This is a readme file that contains meta data.."
          }
        }
      },
      "droppables":{
        "source":{
          "correct":[
            "source"
          ]
        },
        "date_folders":{
          "correct":[
            "date_folder"
          ]
        },
        "experiments":{
          "correct":[
            "experiment"
          ]
        },
        "files":{
          "correct":[
            "file"
          ]
        },
        "readme":{
          "correct":[
            "readme"
          ]
        }
      }
    }

Once your Acos exercise is ready, and the exercise files have been created, you will have two choices for running your code
locally in the browser. :ref:`The first option <local-test>` is to run the exercise with a copy of the Acos-server in your
computer. :ref:`The second option <docker-test>` is to run the exercise by using a pre-installed docker container which is
downloaded after you have compiled an A+ course for the first time.

.. important::

  Before proceeding to test your Acos exercise, you should :ref:`configure the localhost <acos-docker-mac-windows>`
  in your computer. Therefore, you should verify that your host file have the ``127.0.0.1 acos`` configuration.


.. _local-test:

Test Acos activities locally
----------------------------
In order to test Acos exercises locally, you should download the `acos-server repository <https://github.com/acos-server/acos-server>`_
from GitHub. Once you have downloaded this repository, you should link the :ref:`Acos exercise you have developed <create-acos-exercise>`
to the local Acos-server.

#. Open the terminal in the exercise project directory that you created :ref:`above <create-acos-exercise>`, and type:

   .. code-block:: bash

     sudo npm link

#. Open a terminal in the Acos server project directory and type:

   .. code-block:: bash

     sudo npm link acos-draganddrop-data-management

   (The ``acos-draganddrop-data-management`` name will vary according to the name of your package.)

#. Now, it is time to run Acos server locally. For that, you need to open the terminal again in the Acos server project directory
   and type:

   .. code-block:: bash

     npm start

#. You can now open a web explorer and visit http://acos:3000. Your exercise should be running under the draganddrop-data-management
   package.

   .. figure:: /images/gifs/AcosServerLocal.gif
     :width: 100 %
     :align: center

.. important::

  #. Once you have created the `npm link <https://docs.npmjs.com/cli/link.html>`_ to the Acos package folder (npm package), all
     the changes in your exercises will be reflected in the ``node_modules`` folder of the Acos-server.
  #. Normally, you will have to stop/start the node module every time you make changes in your exercise. (:kbd:`Ctrl` + :kbd:`c` to
     stop the module and ``npm start`` to start).

.. _docker-test:

Test Acos activities with Docker
--------------------------------
After you have compiled your A+ course in your computer for the first time, the Acos docker image is downloaded and installed
locally. It means that you can make use of that docker image to test your Acos exercises in a docker container.

Once you have :ref:`created your activity <create-acos-exercise>`. You should create a ``docker-compose.yml`` file, in the root of
your project exercise, with the following information in it. You can also find that file in the zip file provided in this chapter.

.. code-block:: yaml
  :caption: docker-compose.yml file
  :name: target-name
  :linenos:

  version: '3'

  services:
  acos:
      image: apluslms/run-acos-server
      ports:
      - "3000:3000"
      volumes:
      - .:/usr/src/acos-server/node_modules/acos-draganddrop-data-management

After adding the ``docker-compose`` file, the structure of your folder should looks like follows.

.. code-block:: bash
  :caption: The structure of the project should look like this.
  :emphasize-lines: 2

  .
  ├── docker-compose.yml
  ├── exercises
  │   ├── data_structure.json
  │   └── data_structure.xml
  ├── index.coffee
  ├── index.js
  ├── LICENSE
  ├── node_modules
  ├── package-lock.json
  ├── README.md
  └── static
      ├── data_folder.png
      ├── date_folder.png
      ├── exp_folder.png
      ├── file.png
      ├── link_folder2.png
      ├── link_folder.png
      ├── project_folder.png
      ├── readme.png
      ├── scripts.png
      └── src_folder.png

Now, it is time to run the Acos server using the docker container, and visualise your exercise in your
`web browser <http://acos:3000>`_. Therefore, you should open the terminal in the Acos package you are developing and run the
following command.

.. code-block:: bash
  :caption: Start the Acos server docker container

  docker-compose up

Once you have run the ``docker-compose up`` command, you will be able to see the Acos exercises in the browser.

.. image:: /images/gifs/AcosServerDocker.gif
  :width: 100 %
  :align: center

.. warning::

  Every time you make some changes to your exercises, you should stop and start the docker container in order to visualise the
  changes you have made. You can stop the docker container by typing :kbd:`Ctrl` + :kbd:`c` in the terminal that is running the
  container, and you can start the container by typing ``docker-compose up`` in the same terminal. If for some reason you do not
  stop and start the container, your changes will not be reflected on the web browser.

Additional Resources
--------------------

You can find more information on how to develop Acos exercises in the following links:

#. `Acos drag and drop <https://github.com/acos-server/acos-draganddrop>`_

#. `Acos repositories <https://www.npmjs.com/package/acos-server#related-repositories>`_

#. `Acos server development <https://github.com/acos-server/acos-server/blob/HEAD/doc/development.md>`_

#. `Examples of Parson exercises <https://js-parsons.github.io/>`_

#. `More examples of Parson exercises <http://parsons.problemsolving.io/>`_



