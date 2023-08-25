#!/bin/bash

# The URL for the input git repository is written in
# /submission/user/gitsource

# The repository is cloned to /submission-repo

# The mount directory from config.yaml is in /exercise.
# Append the required support files to test user solution.

#if sudo-capture gitlab-api-query -p version.aalto.fi/gitlab /exercise/git_api_token
#then
if sudo-capture pre git-clone-submission /exercise/git_rsa functions.py
then

  # The functions.py picked above is now in /submission/user directory.
  # The file was moved, so it does not exist in /submission-repo anymore.
  # The rest is grading as usual.

  export PYTHONPATH=/submission/user
  capture python3 /exercise/grader_tests.py
  err-to-out

fi
#fi
