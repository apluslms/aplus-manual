""" This script is used by the run-aplus-front container,
which is used for local testing of the A+ course.
This script modifies the course database with some course-specific settings.
It may be mounted into the container in docker-compose.yml.
(If not mounted, this script does not do anything.)
"""

import os
import sys
import datetime
from datetime import timedelta
import random
import time

import django
from django.utils import timezone

def modify_default_courses():
    from course.models import Course, CourseInstance, Enrollment, StudentGroup

    # The container has already created the default database, but we
    # modify some settings of the course instance here.
    course = Course.objects.get(
        url="def",
    )

    instance = CourseInstance.objects.get(
        course=course,
        url="current",
    )

    #instance.head_urls =
    #        "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_CHTML-full&delayStartupUntil=onload"
    #instance.view_content_to = CourseInstance.VIEW_ACCESS.ENROLLED
    #instance.view_content_to = CourseInstance.VIEW_ACCESS.PUBLIC
    #if not instance.description:
    #    instance.description = '<p><b>TESTing</b> course instance description.</p><p>Hello course!</p>'
    #instance.save()

    from django.contrib.auth.models import User

    teacher = User.objects.get(username="teacher")

    course2, created = Course.objects.get_or_create(
        name="Test course 2",
        code='testcourse2',
        url='testcourse2',
    )
    if created:
        course2.teachers.set([teacher.userprofile])
        course2.save()
    now = timezone.now()
    try:
        instance2 = CourseInstance.objects.get(
            course=course2,
            instance_name="Test instance",
            url='test',
        )
        instance2.starting_time = now
        instance2.ending_time = now + timedelta(days=365)
        instance2.save()
    except CourseInstance.DoesNotExist:
        instance2 = CourseInstance.objects.create(
            course=course2,
            instance_name="Test instance",
            url='test',
            starting_time = now,
            ending_time = now + timedelta(days=365),
        )

    # enroll students
    for i in range(2, 100):
        user = User.objects.get(username="student" + str(i))
        Enrollment.objects.get_or_create(course_instance=instance, user_profile=user.userprofile)

    # student groups
    for i in range(2, 90, 3):
        group = StudentGroup(course_instance=instance)
        group.save()
        member1 = User.objects.get(username="student" + str(i))
        member2 = User.objects.get(username="student" + str(i + 1))
        group.members.add(member1.userprofile, member2.userprofile)

    # UserTags
    create_user_tags(instance)

    ###########################################################
    # add submissions for testing
    from course.models import CourseModule
    from exercise.exercise_models import BaseExercise, LearningObject
    from exercise.submission_models import Submission
    time.sleep(4) # let the database initialize the course (JSON import from the mooc-grader)

    student1 = User.objects.get(
        username='student',
    )
    # module from the aplus-manual course
    course_module = CourseModule.objects.get(
        url='m01_introduction',
        course_instance=instance,
    )
    exercise = BaseExercise.objects.get(
        course_module=course_module,
        url='m01_introduction_07_questionnaires_questionnaire_demo',
        #order=1,
    )
    for i in range(300):
        new_submission = Submission.objects.create(
            exercise=exercise,
            #submission_data={},
        )
        new_submission.submitters.set([student1.userprofile])
        if random.random() > 0.3: # randomly grade some submissions
            new_submission.set_points(random.randint(0, 50), 50)
            new_submission.set_ready()
            new_submission.save()


def create_user_tags(instance):
    # instance is a CourseInstance
    # UserTags
    from course.models import UserTag, UserTagging
    tag_tomato, created = UserTag.objects.get_or_create(
        course_instance=instance,
        name="Tomato",
        slug="tomato",
        description="Eats tomatoes",
        color="#FF0000",
    )
    tag_apple, created = UserTag.objects.get_or_create(
        course_instance=instance,
        name="Apple",
        slug="apple",
        description="Eats apples",
        color="#FFB6C1",
    )
    tag_orange, created = UserTag.objects.get_or_create(
        course_instance=instance,
        name="Orange",
        slug="orange",
        description="Eats oranges",
        color="#FFA500",
    )
    tag_banana, created = UserTag.objects.get_or_create(
        course_instance=instance,
        name="Banana",
        slug="banana",
        description="Eats bananas",
        color="#FFFF00",
    )
    tags = (tag_tomato, tag_apple, tag_orange, tag_banana)
    # UserTaggings
    from django.contrib.auth.models import User
    for i in range(2, 100):
        user = User.objects.get(username="student" + str(i))
        UserTagging.objects.set(user.userprofile, random.choice(tags))


FIRST_NAMES = ("Adam", "Ben", "Charlotte", "David", "Eliot", "Felicia", "Gregory", "Hanna", "Ilona", "Joe")
LAST_NAMES = ("Arbitrator", "Bond", "Cauliflower", "Dazed", "Ephemeral", "Fig", "Gabby",
    "Honeydew", "Impeccable", "Student")
EMAIL_DOMAINS = ("plus.domain", "local.domain", "example.org", "example.domain", "school.domain")

def create_new_users():
    from django.contrib.auth.models import User

    for i in range(2, 121):
        if User.objects.filter(username="student" + str(i)).exists():
            continue
        new_student = User.objects.create(
            pk=498 + i, # set the ID manually so that user.id is different than profile.id
            username="student" + str(i),
            email="student{0}@{1}".format(i, random.choice(EMAIL_DOMAINS)),
            first_name=random.choice(FIRST_NAMES),
            last_name=random.choice(LAST_NAMES),
        )
        new_student.set_password("student" + str(i))
        new_student.save()
        if i < 110:
            # some students do not have a student id
            new_student.userprofile.student_id = "".join(random.choices("0123456789", k=6))
            new_student.userprofile.save()


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aplus.settings")
    sys.path.insert(0, '')
    django.setup()

    create_new_users()
    modify_default_courses()

