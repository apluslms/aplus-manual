Creating a new course instance
==============================

This section discusses how to create a new course instance on an already existing
course. In the case that you need to create an entirely new course,
contact A+ support at aplusguru@cs.aalto.fi.
Some information here might be specific to Aalto University, Gitlab or other
software, not particularly A+.


Part 1: Creating the course instance
------------------------------------

New course instances can be created by a teacher in the **Instances** section
under **Edit course**. After filling in the required information and submitting
the form, the course build begins automatically. This may take several minutes
to complete, during which the course appears empty. You can check the build log
at **Edit course -> Content -> Retrieve latest build log**.

Part 2: Setting up the Git webhook in GitLab
--------------------------------------------

Head over to the **Git manager** section under **Edit course** and get ready to copy the
**Hook** and **Webhook secret** to the GitLab repository in the web interface of the project.

In the project home page, go to **Settings -> Webhooks** in the left-side menu.
Fill in the form:

- Enter the hook URL in the **URL** field.
- Enter the webhook secret in the **Secret token** field.
- Select trigger for **Push events**, enter the Git branch name in the field
  (the same branch that you input previously in the course instance creation form) and
  select **Enable SSL verification**.
- Click the **Add webhook** button.
