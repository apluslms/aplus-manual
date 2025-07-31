Setting submission tags in grading containers
=============================================

Submission tags are used to categorize or label submissions in A+.
These tags can be set either manually in A+ or automatically by grading containers based on
`grading-base <https://github.com/apluslms/grading-base>`_ version 4.12 or newer.

In grading containers, the submission tags can be set by outputting them directly or by writing them to a file.
Below are the detailed methods for setting submission tags.

1. **Setting submission tags by output**:
  - This method involves printing the submission tags along with the points and maximum points.
  - Example (in Python unittests):

    .. code-block:: python

      ...
      submission_tags = "tag1slug,tag2slug"
      print(f"TotalPoints: {result.points}\nMaxPoints: {result.max_points}\nSubmissionTags: {submission_tags}")

2. **Setting submission tags by writing to a file**:
  - This method requires writing the submission tags to a specific file (`/feedback/submission_tags`) and is typically used when tests are run with root user permissions.
  - Example (in Python unittests):

    .. code-block:: python

      ...
      submission_tags = "tag1slug,tag2slug"
      with open("/feedback/points", "w") as f:
        f.write(f"{result.points}/{result.max_points}")
      with open("/feedback/submission_tags", "w") as f:
        f.write(submission_tags)

  - Ensure that the tests are executed with the necessary permissions to write to the `/feedback` directory.

**Important notes**:

- Make sure the submission tags have been created in the A+ course settings before using them in grading containers.
- Use submission tag slugs instead of names. The slugs can be viewed in the A+ course settings.
- Submission tag slugs must be separated by commas without any whitespace between them.
- Proper formatting of the output or file content is crucial for the grading system to correctly interpret the submission tags.
