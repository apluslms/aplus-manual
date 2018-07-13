LTI in A+
=========

Learning Tools Interoperability (LTI) is a standard created by IMS Global
Learning Consortium. It connects learners from learning management systems (LMS)
to learning objects (such as exercises, visualizations, or e-books) hosted in
external services, which are called Tool Providers (TP) in the LTI terminology.
The LMS is called a Tool Consumer (TC). Many widely used learning management
systems and content providers support the LTI standard. Learners may easily
access different learning objects from the course site within the LMS without
knowing which external service is really providing the content.

The LTI version 1.0 only defines the launch of the external tool, which basically
logs the user into the system without an explicit log-in (the user is already
logged into the LMS). The version 1.1 adds the **Basic Outcomes Service** that
enables Tool Providers to also send grades back to the LMS. The A+ platform
supports the LTI version 1.1 (as of A+ version 1.3, August 2018). (The LTI
standard has also already released a newer version 1.3 and there is also the
deprecated, architecturally different version 2.0.) The LTI 1.1 implementation
in A+ follows `the official standard`_ from IMS Global. A+ does not implement
all of the optional nor recommended LTI launch parameters and may also include
some custom parameters used by other systems in the A+ family. Nonetheless,
A+ should operate with any standards-compliant LTI 1.1 Tool Provider.

When a user launches an LTI service from an LMS, the user interacts directly
with the Tool Provider. The LMS is only involved in preparing the launch
parameters and potentially receives the grade of the submission if the TP sends
it back to the LMS using the Basic Outcomes Service. The user does not submit
his/her solution to the LMS. In normal A+ exercises, the user submits the
solution to A+ and A+ uploads it to the exercise service for grading using
the A+ protocol. LTI works differently; consequently, A+ has less control over
the process and it can not keep track of the user's activity as closely.
Furthermore, normal A+ exercises enable A+ to store the contents of the
submission (such as the submitted file) and the feedback, whereas they are not
available to the LMS in LTI 1.1 exercises.

An LTI service is launched from the LMS by basically submitting a form in the
LMS web page. The LTI launch parameters are defined in the form as hidden inputs.
The form is posted to the launch URL of the Tool Provider, not the LMS.
The TP launch page may be opened in a new browser window or in an iframe element
within the LMS page, depending on the target of the HTML form. The launch
parameters identify the user, role (Learner or Instructor), context (course),
and learning object among other details.

Before an LMS may operate with a Tool Provider, the TP must allow access for the
LMS by setting up a key and a secret. They are comparable to an account name and
a password between the LMS and the TP and they are used for securing the
communications between the LMS and the TP as well as restricting unauthorized
access to the TP. LTI 1.1 uses the OAuth1 standard for securing the messages by
signing them with the shared secret. Attackers can not forge valid signatures
without knowing the secret.

.. warning::

  The OAuth1 parameters in the LTI launch include a one-time use nonce value
  as well as a timestamp. If the user opens an LTI launch page and leaves it
  open for a long time without submitting the launch form, the nonce and
  timestamp will likely expire. In that case, the Tool Provider rejects the
  launch with an error. The user may gain a fresh nonce by refreshing the launch
  page in the LMS. The exact expiration time of the nonce depends on the Tool
  Provider.


Basic Outcomes Service
----------------------

Basic Outcomes Service is the part of LTI that enables Tool Providers to send
grades back to the LMS (i.e., A+). The LTI protocol supports only numeric grades
0.0–1.0 with no textual feedback. The grade is scaled to actual points based on
the maximum points of the exercise in A+.

Basic Outcomes Service defines three operations: setting, reading, and deleting
results. They are named *replaceResult*, *readResult*, and *deleteResult*,
respectively. A typical Tool Provider probably sends a replaceResult request
to the LMS when it has finished grading the student's submission, which could
take place soon after the the student has uploaded the submission to the TP or
much later. The LTI specification does not require the TP to immediately send
the results back to the LMS, hence it is possible in theory that the TP waits
with the results and only sends one replaceResult request to the LMS after the
student has submitted multiple times in a short time. In that case, A+ would not
know that there have been multiple submissions and not just one. Furthermore,
A+ does not know the exact time when the TP received the submission since the
Basic Outcomes Service does not include a submission time field. Therefore,
A+ uses the receiving time of the replaceResult request as the submission time.

A+ creates a new submission to the exercise for the submitting
student every time a valid replaceResult request is received. That is to say,
A+ stores the LTI exercise grade in a submission once the Tool Provider sends
the grade back to A+. A+ does not overwrite existing submissions even when
multiple replaceResult requests are received for the same student and exercise.
Since the LTI protocol version 1.1 does not support any textual feedback in the
Basic Outcomes Service, the submissions in A+ do not include any feedback;
they only show the points of the submission. Depending on the TP, it may show
information about the preceding submission(s) with more feedback to the student
when he/she launches the service. Likewise, the contents of the submission,
such as files uploaded by the student, are not visible in A+ since A+ never
receives them.

A+ responds to readResult requests with the current best points of the student
in the exercise. A+ has decided to not implement the delete operation so that
no submission history is lost. Consequently, A+ responds to deleteResult requests
with the "unsupported" message defined in the LTI specification.

.. warning::

  LTI exercises do not currently support group submissions. Students may only
  submit as individuals. Group submissions could be implemented
  for LTI exercises in the future.

.. warning::

  A submission to an LTI exercise can not be sent to the exercise service for
  (automatic) regrading. (Normal exercises could be regraded from the teacher's
  inspect submission page.) The LTI protocol does not support any kind regrading
  initiated by the LMS. However, if the Tool Provider stores the submission data,
  then it could provide its own regrading functionality that would also send the
  new results to the LMS via normal replaceResult requests. It depends on the
  TP whether such functionality is supported. Remember though that the
  replaceResult requests do not overwrite the previous submissions already
  stored in A+.
  
  **N.B.** A+ stores the submission history and uses the best submissions for
  computing the total points in the course. If an exercise has been faulty and
  submissions have earned too many points, the submissions must be reset by hand
  in order to remove the incorrect points since LTI exercises do not support
  automatic regrading.

.. warning::

  LTI exercises have limitations for tracking the number of submissions and
  the submission time. This is relevant when strict deadlines and submission
  limits are used. Since the Basic Outcomes Service does not explicitly include
  these data fields, A+ can not track them completely accurately. If the Tool
  Provider sends a replaceResult request to A+ for each submission and the
  requests are sent quickly without delay at the time the student uploads the
  submission, then A+ may track the correct number of submissions and the
  recorded submission times do not differ much from the real submission times.


.. _the official standard: https://www.imsglobal.org/specs/ltiv1p1/implementation-guide

