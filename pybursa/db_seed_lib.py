from django.test import Client

from django.contrib.auth.models import User
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach

class Db_seed(object):

    http_client = Client()

    def new_coach(self, name):
        return Coach.objects.create(
                            user=User.objects.create(username=name),
                            date_of_birth='1970-01-01',
                            gender='M',
                            phone='777',
                            address='Address',
                            skype='Scype',
                            description='Description')

    def new_course(self, name, coach, assistant):
        return Course.objects.create(
                            name=name,
                            short_description='Short description',
                            description='Description of course',
                            coach=coach,
                            assistant=assistant)


    def new_student(self, name):
        return Student.objects.create(
                            name=name,
                            surname='Surname',
                            date_of_birth='1980-01-01',
                            email='student@student.com',
                            phone='777',
                            address='Address',
                            skype='Skype')

    def new_lesson(self, name, course):
        return Lesson.objects.create(
                            subject=name,
                            description='Description Lesson',
                            course=course,
                            order=1)