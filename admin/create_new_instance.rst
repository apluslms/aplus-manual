Creating a new course instance
==============================

This section discusses how to create a new course instance on an already existing course.
In the case that you need to
**create an entirely new course with a new course code, contact the local A+ support.**
At Aalto University, use the form at
`Requests for course instances <https://wiki.aalto.fi/display/EDIT/Requests+for+course+instances>`_.


.. admonition:: Demo video
  :class: info

  `Video of creating a new course instance`_.

.. _Video of creating a new course instance: https://aalto.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=30f10643-2714-4317-bc3b-aef6007f497b

.. admonition:: Aalto GitLab
  :class: info

  At Aalto University, the GitLab server is called Aalto Version Control System, https://version.aalto.fi/


Part 1: Prepare a git repo and branch for the new instance
----------------------------------------------------------

**In the course git repository, create a new git branch for the new course instance.**
The new branch could be based on the branch of the previous course instance.
The new branch is needed for creating the new A+ course instance.
At first, the new branch may be identical to the previous branch.
You do not have to update the course contents of the new instance in the git repo
before creating the new A+ course instance.

New git branches may be created in the GitLab web user interface or
in the local clone of the git repo using the command-line:

.. code-block:: sh

  # cd into the course repository
  # Create a new branch named 2023. It is based on the currently active branch.
  git checkout -b 2023
  # Push the new branch to the GitLab server.
  git push -u origin 2023


.. admonition:: Aalto Version Control System: enable access to the course git repo
  :class: warning

  If you created a new git repo in version.aalto.fi,
  remember to grant access to the A+ support personnel and the servers.
  See
  `the instructions in the wiki <https://wiki.aalto.fi/pages/viewpage.action?pageId=159755451#A+LMS-HowdoIgetmycourseinproduction?>`_.


Part 2: Create the course instance in A+
----------------------------------------

New course instances can be created by a teacher in the **Instances** tab
under **the Edit course section**. After filling in the required information and submitting
the form, the course build begins automatically. This may take several minutes
to complete, during which the course appears empty. You can check the build log
at **Edit course → Content → Retrieve latest build log**.

Part 3: Set up the Git webhook in GitLab
----------------------------------------

Head over to the **Git manager** section under **A+ Edit course section** and get ready to copy the
**Hook** and **Webhook secret** fields to the GitLab repository in the web interface of the project.

In the GitLab project home page of your course, go to **Settings → Webhooks** in the left-side menu.
Fill in the form:

1. Enter the hook URL in the **URL** field.
2. Enter the webhook secret in the **Secret token** field.
3. Select trigger for **Push events**, enter the Git branch name in the field
   (the same branch that you input previously in the course instance creation form) and
   select **Enable SSL verification**.
4. Click the **Add webhook** button.
