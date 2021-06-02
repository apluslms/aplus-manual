Submit from Git
===============

A-plus supports exercises where student solutions are retrieved
from their personal Git repository.

.. warning::

  To test grading from Git, **a private RSA key MUST be appened to
  the file at ``exercises/git_hello_python/git_rsa``.**
  In May 2021, the access script in `grading-base`_ requires RSA key
  that is used in cloning the repository via ssh URL.
  Furthermore, it may require the repository is in `version.aalto.fi`_.

  Inserting the private key has the consequence that any users having
  access to these course source files can run git commands in the system
  authenticated as the user whose account is linked to the private key
  via the matching RSA public key configured in GitLab.

.. _grading-base: https://github.com/apluslms/grading-base/blob/master/bin/git-clone-submission
.. _version.aalto.fi: https://version.aalto.fi

.. admonition:: Notice

  Following is the Hello Python -exercise previously presented in this
  manual except that the submission is configured via git. Students must
  be instructed at the beginning of the course to add the grading account
  (linked via the RSA key) as a reporter to their project members.
  **Without ``require_gitlab`` configuration students must use SSH URLs**.

.. submit:: python 10
  :config: exercises/git_hello_python/config.yaml


Other remarks
.............

*  The setting ``require_gitlab`` in ``/exercises/git_hello_python/config.yaml``
   allows to input GitLab HTTP URLs for the given domain.
   Presumably it should reject other domains but doesn't in May 2021.

*  GitLab API token may be inserted as the file ``/exercises/git_hello_python/git_api_token``
   and ``gitlab-api-query`` uncommented in the script ``/exercises/git_hello_python/run.sh``.
   These optional checks can ensure, before cloning, that the repository exists
   and is private. There is also an option to check that the repository is forked
   from a given source repository (see grading-base `readme`_). Note that anyone
   having access to the API token can access the API and it's features
   authenticated as the token owner.

*  When there are multiple exercises graded from git the ``/build.sh``
   script can be used to distribute the necessary key files to all the necessary
   exercise directories that get mounted to the grading image.

.. _readme: https://github.com/apluslms/grading-base/
