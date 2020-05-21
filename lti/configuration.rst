LTI configuration in A+
=======================

This chapter explains how LTI content is added to an A+ course. An initial
one-time setup is required: the LTI service must be enabled in the A+ site
configuration before it may be used on courses.


Enabling an LTI service in the A+ site
--------------------------------------

Before an external LTI service may be used on any course, it must be added and
enabled in the A+ site administration. The same service is enabled only once:
it may then be used on any course. When the teacher adds LTI exercises or links
to services in a course, he/she must select the LTI service to use from the
enabled services in the site. Therefore, it is better to enable the LTI service
in the site before adding any related course content. The sitewide
configuration of the LTI service contains the key and secret obtained from the
Tool Provider.

The A+ site administrator accesses the admin interface in the URL path
`/admin <//localhost:8000/admin>`_.

1. Find "Lti services" under "External services" and click "add".
2. In the form, enter the launch URL of the service as well as the consumer key
   and secret.
3. The "menu label" is the default label for the service link if any links are
   added to the course menu (left navigation menu). "Access settings" define
   whether the LTI launch includes any identifiable, sensitive user data or
   only anonymized user data. Identifiable user data should only be sent to
   external services when it is really required and the legal and administrative
   issues concerning user data and privacy are clear. Additionally, the access
   settings control whether the LTI service gains access to the A+ API
   (application programming interface), which, for example, allows it to read
   user data and create submissions for the user.
   Usually, only LTI services developed within the A+ family know how to use
   the A+ API. The default value for access settings is to anonymize user data
   and to forbid API access.
4. Click "save".


LTI exercises and services in a course
--------------------------------------

LTI exercises are part of the course materials like normal exercises and
chapters. Exercises expect the student to submit a solution for grading.
LTI services may also be added to the course as links without any associated
grading. Such links are displayed in the course menu (left navigation menu in
the course page) and they are suitable for tools, such as forums, that typically
do not involve any grading of the student's activity.


Adding LTI service links to the course menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the "edit course" page from the course menu (left navigation menu).
   It is listed under the staff menu items.
2. Open the "menu" tab.
3. Click the "add new menu item" button.
4. Enter the settings for the menu item. A menu item may link to an LTI service
   or to any given URL without any attached LTI parameters like a normal
   hyperlink. For LTI links, you must select the LTI service in the form.
   
   The option "menu label" is the title of the menu item shown in the course
   menu. Menu items may be grouped under headings by defining the option
   "menu group label".
5. Submit the form.


Adding LTI exercises to a course
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LTI exercises may be defined in the MOOC grader course configuration that is
imported to the A+ course. It is the recommended way. The exercise configuration
in the MOOC grader differs only a little between normal exercises and LTI
exercises. LTI exercises define a few LTI-specific settings and they may ignore
the grading settings as the exercise is not graded in the MOOC grader.
LTI exercises may also be added manually in the A+ "edit course" page.

.. note::

  Note that the A+ or MOOC grader course configurations can not define the
  actual content of the LTI exercise. They only define
  *how A+ connects the user to the external service (Tool Provider)*.
  It depends on the Tool Provider whether it serves ready-made learning objects
  or whether it provides tools for the teacher to create new exercises of
  a certain type.

Here is a simple example of a MOOC grader *config.yaml* file for an LTI exercise.

.. code-block:: yaml

  name: Submit to Rubyric
  lti: Rubyric+
  lti_open_in_iframe: True


The exercise is included in the course *index.yaml* file in the normal way.
(The exercise could be defined directly in the *index.yaml* without a separate
YAML file since there are not many settings to define.)

.. code-block:: yaml

  # a partial course index.yaml
  modules:
    - key: ltiround
      name: LTI round
      children:
        - key: ltiexercise1
          category: LTI exercises
          max_points: 100
          config: exercises/lti_exercise.yaml


The LTI-specific settings are listed in the table :ref:`ltiexerciseconf`.

.. _ltiexerciseconf:

.. table:: LTI exercise settings
  :widths: auto
  :align: left

  ====================== ==========================================================
  Setting                Purpose
  ====================== ==========================================================
  lti                    Defines the LTI service. The value must match the menu
                         label of an LTI service already configured in the A+ site.
  lti_context_id         The context id for the LTI launch. A+ uses an id based on
                         the course instance by default. Usually, it is best to
                         leave this undefined in favor of the default value.
  lti_resource_link_id   Resource link id for the LTI launch. A+ uses the exercise
                         id by default. Using the default is recommended.
  lti_open_in_iframe     If ``True``, the exercise is opened in an iframe inside
                         the A+ page instead of a new browser window or tab.
  lti_aplus_get_and_post If ``True``, the exercise uses the A+ protocol to connect
                         to the service. The LTI launch parameters are appended to
                         the A+ protocol parameters. This does not work with
                         standard LTI services. This setting is intended to be
                         used with certain services developed within the A+ family.
  ====================== ==========================================================


**LTI exercises may be embedded in RST chapters**. The exercise is defined using
the normal ``submit`` RST directive with LTI-specific options. A simple example
is given below. The ``ajax`` option is needed because otherwise, the chapter
would break the launch of the exercise by redirecting the launch form submission
to A+ instead of the correct service launch URL.

.. code-block:: rst

  .. submit:: exercisekey 100
    :lti: Rubyric
    :lti_open_in_iframe:
    :ajax:


.. warning::

  Currently, A+ can not automatically update the exercise points shown in
  chapter or exercise pages when the student submits a new solution to the
  Tool Provider. The updated points are shown when the user refreshes the web
  page, assuming that A+ has at that time received the new graded submission
  from the Tool Provider.

