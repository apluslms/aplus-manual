Technical details of interactive code
=====================================

.. styled-topic::

  Main questions:
      How does thebe work, and how do I troubleshoot problems?

  Topics?
      Technical details of interactive code

  Difficulty:
      Medium

  Laboriousness:
      Around 5 minutes of reading


Technical architecture
----------------------
The interactive code is run in a `jupyter notebook <https://jupyter.org/>`_. Each time a student activates the interactive code enviroment, they request a new kernel from a `binderhub <https://binderhub.readthedocs.io/en/latest/>`_ server. This is done with the help of the javascript library `thebe <https://thebe.readthedocs.io/en/latest/>`_ that takes care of the communication with the binderhub server. The sphinx extension provided by aplus-rst-tools is based on the code of a sphinx extension `sphinx-thebe <https://sphinx-thebe.readthedocs.io/>`_.

Since the kernel is requested by the user's browser, any changes made disappear when the user refreshed the page.

The testing environment is provided by `mybinder <https://mybinder.org/>`_, but this shouldn't be used for live courses. When your course is going public, you should change the settings to use a binderhub server provided by your institution.

Using other programming languages
---------------------------------
Only support for python has been tested, but Jupyter supports other programming languages as well. As documented `here <https://sphinx-thebe.readthedocs.io/en/latest/configure.html#setting-the-kernel>`_, it is possible to set the kernel using a meta tag. In aplus, this would mean adding the lines

.. code-block:: rst

  .. meta::
    :thebe-kernel data-aplus=yes: <KERNEL-NAME-HERE>

to the top of every page where you want to use a different kernel.

Troubleshooting
---------------
Since requesting a kernel is taken care of by a javascript library called from the browser, a good way of getting information about possible issues is by looking at the developer console of your browser.
