LTI in A+
=========

Learning Tools Interoperability (LTI) is a standard created by IMS Global
Learning Consortium, later rebranded as 1EdTech Consortium. It connects
learners from learning management systems (LMS) to learning objects (such as
exercises, visualizations, or e-books) hosted in external services, which are
called Learning Tools in the current LTI terminology. The LMS is called a
Learning Platform. Many widely used learning management systems and content
providers support the LTI standard. Learners may easily access different
learning objects from the course site within the LMS without knowing which
external service is really providing the content.

There are different versions of the LTI specifications. The current family of
specifications are called **LTI Advantage**, that includes the LTI Core
Specification version 1.3 and the services that are built on top of it. Earlier
LTI versions are version 1.0 that only defines the launch of the external tool
and LTI version 1.1 that adds the **Basic Outcomes Service** enabling Tool
Providers to also send grades back to the LMS. Starting from A+ version 1.19, A+
supports all of these versions, but LTI 1.3 should be preferred when possible, as
the earlier versions are technically incompatible with it and are expected to be
rolled out eventually. For more information, you may see `an overview`_ of LTI
1.3 and LTI Advantage services by the 1EdTech Consortium. A+ versions prior to
1.19 only support LTI 1.0 and LTI 1.1 (more specifically, LTI 1.3 Tool
implementation was introduced already in A+ version 1.18).

When LTI 1.3 is used, A+ can be used as an LTI Platform, i.e., as an LMS that
uses external learning services for providing assignments and other content, or
as an LTI Tool, in which case the content and assignments implemented in A+ can
be used from another LMS, such as Moodle. In addition to the LTI Core
Specification, A+ supports parts of the Assignment and Grades services, to allow
transfer of scores and grades from different LTI Tools to the A+ Platform, or
from an A+ as an LTI Tool to another LMS acting as the LTI platform. Currently
the LTI Deep Linking Service is supported only by the A+ LTI Tool
implementation, but not by the LTI Platform. The other LTI Advantage services,
such as the Names and Role Provisioning Services are not supported at the
moment.

When user launches an LTI service from an LMS, they interact directly with the
LTI Tool. The LMS is only involved in preparing the launch parameters and
potentially receives the grade of the submission if the Tool sends it back to
the LMS. The user does not submit her solution to the LMS. In normal A+
exercises, the user submits the solution to A+ and A+ uploads it to the exercise
service for grading using the A+ protocol. LTI works differently; consequently,
A+ has less control over the process and it can not keep track of the user's
activity as closely. Furthermore, normal A+ exercises enable A+ to store the
contents of the submission (such as the submitted file) and the feedback,
whereas they are not available to the LMS in LTI exercises.

An LTI service is launched from the LMS by basically submitting a form in the
LMS web page. The LTI launch parameters are defined in the form as hidden inputs.
The form is posted to the launch URL of the LTI Tool, not the LMS.
The Tool launch page may be opened in a new browser window or in an iframe element
within the LMS page, depending on the target of the HTML form. The launch
parameters identify the user, role (Learner, Instructor), context (course),
and learning object among other details.

The launch operation in LTI 1.3 is based on the OAuth2 standard and the OpenID
Connect protocol. The LTI Tool and the LTI Platform must be configured in
advance by the system administrators by setting up the needed public/private key
information, and the shared client and deployment identifiers. When A+ is used
as the LTI Platform, sharing user's name and email from A+ to the LTI Tool is
optional, and can be configured separately for each LTI Tool. The A+ source
repository contains a separate document about LTI configuration for A+
administrators. Note that the earlier versions of LTI are based on OAuth1 and
are incompatible with LTI 1.3, and are thus configured in a different way.

.. warning::

  LTI exercises do not support group submissions. Students may only
  submit as individuals.

.. warning::

  For LTI exercises the number of submissions cannot be tracked, and some LTI Tools
  may not even have a similar concept of submission as A+ has. For example, an
  LTI exercise can be composed from a series of small tasks in a longer
  interactive learning activity in the Tool's environment. In LTI's Assignments
  and Grades Service the score updates are sent from the Tool asynchronously,
  and there may be several score updates for each exercise, for example as the
  student progresses in an interactive activity. In some cases the score update
  from the Tool may also be delayed, depending on the Tool implementation.
  Therefore, for LTI 1.3 exercises, A+ shows only one submission for each
  student, that is based on the most recent score update received from the Tool for
  the particular exercise. The submission time shown in A+ for LTI exercises is
  taken from the most recent score update from the tool, and depending on the
  Tool implementation, may not accurately reflect the time the student actually
  "submitted" the exercise. It is recommended that when a new LTI Tool is taken
  into use, the Tool's grading behavior is tested properly before the start of a
  course. The LTI messages, e.g. regarding grading, can be seen in the A+ logs
  by the system administrators.

  For the reasons described above, the LTI Exercises cannot be sent for
  regrading from A+. It is possible, though, that the LTI Tool supports
  regrading of assignments in its own environment, and consequently sends a
  score update message to A+.

LTI 1.0 and LTI 1.1
-------------------

While the LTI 1.0/1.1 exercises may seem similar from A+ user's point of view
than LTI 1.3 exercises, and are used similarly, they are technically quite
different, use different terminology and configuration attributes, and are
incompatible with LTI 1.3. In earlier LTI versions, the LMS is called Tool
Consumer (TC), and the external service is Tool Provider (TP). A+ implements the
Tool Consumer part of LTI 1.1 and 1.0. Technically, these are separate
implementations in A+, and are configured in a different way.

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

Basic Outcomes Service in LTI 1.1.
----------------------------------

Basic Outcomes Service is the part of LTI 1.1 that enables Tool Providers to send
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

  As with LTI 1.3, LTI 1.1 exercises have limitations for tracking the number of
  submissions and the submission time. This is relevant when strict deadlines
  and submission limits are used. Since the Basic Outcomes Service does not
  explicitly include these data fields, A+ cannot track them completely
  accurately. If the Tool Provider sends a replaceResult request to A+ for each
  submission and the requests are sent quickly without a delay when the
  student uploads the submission, then A+ may track the correct number of
  submissions and the recorded submission times do not differ much from the real
  submission times.

.. _an overview: https://www.imsglobal.org/activity/learning-tools-interoperability
