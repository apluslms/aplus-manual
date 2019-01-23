How to debug a container
========================

Problem: sometimes python-grader-utils will just return:
"Something went wrong with the grader tests... Please contact course staff."
Trying `exec 2>> /feedback/err` in run.sh does not help. In this case, you
have to run the grading container manually and see what goes wrong.

See https://docs.docker.com/engine/reference/commandline/exec/#try-to-run-docker-exec-on-a-paused-container

Find out the image id of the grade-python container. The repository and tag
must match the one in the config.yaml file of the exercise directory.

.. code-block:: none

    $ docker image ls
    REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
    apluslms/grade-python      3.5-2.2             fa937c720836        13 days ago         188MB
    apluslms/grading-base      2.2                 a3112e45cc52        13 days ago         174MB
    apluslms/grading-base      latest              e4ad231b939c        2 weeks ago         174MB
    bokeh                      latest              7fd091aa6822        3 weeks ago         275MB
    apluslms/grade-python      3.5-2.1u1           f46d6a864f86        4 weeks ago         189MB
    apluslms/grade-python      3.5                 985bf93588fe        4 weeks ago         189MB
    hello-world                latest              e38bc07ac18e        6 weeks ago         1.85kB
    apluslms/run-aplus-front   latest              54b9cd98d92d        3 months ago        433MB
    apluslms/run-mooc-grader   latest              66a4d60254d9        4 months ago        729MB
    apluslms/compile-rst       latest              0024d657c5e5        7 months ago        510MB

Go to the directory where the programming exercise is.

.. code-block:: none

    $ cd traky-docker/exercises/palindrome

Print the absolute path.

.. code-block:: none

    $ pwd
    /u/79/atilante/unix/ohj/a-ole/traky-docker/exercises/programming/palindrome

Start the grading container. Replace the X in with your absolute
path of working directory (output of ``pwd`` command) and Y with the image id.

.. code-block:: none

    $ docker run --name grade_python_test --mount type=bind,source=X,destination=/exercise --rm -i -t Y bash

(example: $ docker run --name grade_python_test --mount type=bind,source=/u/79/atilante/unix/ohj/a-ole/traky-docker/exercises/programming/palindrome,destination=/exercise --rm -i -t fa937c720836 bash)

In another terminal:

.. code-block:: none

    $ docker exec -it grade_python_test bash

Now you are in a shell inside the container. The exercise files are in
``/exercise``.

You can replicate the commands of run.sh one by one.

.. code-block:: none

    # cd /exercise
    # cat run.sh
    # cat config.yaml

File config.yaml defines what files the mooc-grader has received.

.. code-block:: none

    ...
    files:
      - field: file1
        name: palindrome.py
    ...

In this case the submitted file would be placed in
``/submission/user/palindrome.py``. However, because now you are not running mooc-
grader, you have to create that file by yourself. Let's say there is already
file /exercise/model.py, which has the correct answer. In this case, copy
this to /submission/user.

.. code-block:: none

    # mkdir /submission/user
    # cp /exercise/model.py /submission/user

Next, replicate the actions of run.sh. Let's assume you need two unit test files
from ``/exercise`` : tests.py and grader_tests.py.

.. code-block:: none

    # cd /submission/user
    # cp /exercise/{grader_tests,tests}.py .

Then execute the unit tests. Do it without ``capture`` to actually print all
error messages instantly:

.. code-block:: none

    # python3 -m graderutils.main /exercise/test_config.yaml

If you still see the message "Something went wrong with the grader tests...
Please contact course staff.", try next commenting out some parts of
test_config.yaml with # characters. For example, run only one unit test module
at a time.

.. code-block:: none

    test_modules_data:
      - module: tests
        description: Local tests
    #  - module: grader_tests
    #    description: Grader tests

    validation:
      - type: python_import
        file: palindrome.py
      - type: python_syntax
        file: palindrome.py
      - type: python_blacklist
        file: palindrome.py
        message: "You are not allowed to reverse sequence"
        node_name:
          sequence_reverse: reverse string


You can also run individual unit tests without python-grader-utils.
In the example, there is still files tests.py and grader_tests.py.

.. code-block:: none

    # python3 tests.py
    test_with_empty_string (__main__.TestIsPalindrome)
    Empty strings are palindromes. (1p) ... ok
    test_with_length_one_strings (__main__.TestIsPalindrome)
    Strings containing one character are palindromes. (1p) ... ok
    test_with_palindromes_and_non_palindromes (__main__.TestIsPalindrome)
    is_palindrome returns True for a palindrome and False for a non-palindrome. (1p) ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK

    # python3 grader_tests.py
    Traceback (most recent call last):
      File "grader_tests.py", line 12, in <module>
        from constants import update_settings_profile
    ImportError: No module named 'constants'

Now we clearly see that tests.py executes nicely, but grader_tests.py has an
error.

You can exit from the container by simply:

.. code-block:: none

    # exit

In the other terminal, where you gave the ``docker run`` command, just press
Ctrl+C to terminate the container.
