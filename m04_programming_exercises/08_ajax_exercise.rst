AJAX exercises: grading in browser JavaScript
=============================================

The following exercise is graded in the browser with custom JavaScript code.
The points are uploaded to the server using AJAX.
**Note:** it is quite easy for students to cheat in AJAX exercises like this since
they can post the points themselves with JavaScript without doing the actual
exercise.

.. raw:: html

  <script src="../_static/md5.js" data-aplus-path="/static/{course}"></script>
  <script src="../_static/ajax_exercise.js" data-aplus-path="/static/{course}"></script>


.. submit:: ajaxexercise 10
  :ajax:
  :submissions: 20
  :config: exercises/ajax_exercise/config.yaml

  Write ``abc`` into the text field.
