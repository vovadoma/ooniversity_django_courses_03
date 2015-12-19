from django.test import TestCase
from django.core.urlresolvers import reverse_lazy

from students.models import Student
from pybursa.db_seed_lib import Db_seed

class StudentsListTest(TestCase, Db_seed):

    def test_empty_course(self):
        response = self.http_client.get(reverse_lazy('students:list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'IT courses students page')
        self.assertContains(response, reverse_lazy('students:add'))

    def atest_add(self):
        # test add student by POST request
        response = self.http_client.post(reverse_lazy('students:add'), {
                                    'name': 'Name',
                                    'surname': 'Surname',
                                    'date_of_birth': '1980-01-01',
                                    'email': 'email@email.com',
                                    'phone': '777',
                                    'address': 'Address',
                                    'skype': 'Skype'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.all().count(), 1)

        response = self.http_client.get(reverse_lazy('students:list_view'))
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Surname')
        self.assertContains(response, reverse_lazy('students:edit', kwargs={'pk': 1}))
        self.assertContains(response, reverse_lazy('students:remove', kwargs={'pk': 1}))

    def test_edit(self):
        student = self.new_student('Student1')
        response = self.http_client.get(reverse_lazy('students:edit', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, 200)
        for field in ('name', 'surname', 'address', 'skype'):
            self.assertContains(response, student.__getattribute__(field))

    def test_delete(self):
        student = self.new_student('Student1')
        response = self.http_client.post(reverse_lazy('students:remove', kwargs={'pk': student.id}))
        self.assertEqual(Student.objects.all().count(), 0)
        self.assertEqual(response.status_code, 302)
        response = self.http_client.post(reverse_lazy('courses:remove', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, 404)

    def test_student_course(self):
        course1 = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        course2 = self.new_course('Course2', self.new_coach('c2'), self.new_coach('a2'))
        student = self.new_student('Student1')
        student.courses.add(course1)
        response = self.http_client.get(reverse_lazy('students:list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)
        self.assertNotContains(response, course2.name)

        student.courses.add(course2)
        response = self.http_client.get(reverse_lazy('students:list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)
        self.assertContains(response, course2.name)


class StudentsDetailTest(TestCase, Db_seed):

    def test_empty(self):
        response = self.http_client.get(reverse_lazy('students:detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        student = self.new_student('Student1')
        response = self.http_client.get(reverse_lazy('students:detail', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, 200)
        for field in ('name', 'surname', 'address', 'skype', 'email', 'phone'):
            self.assertContains(response, student.__getattribute__(field))


    def test_course(self):
        course1 = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        course2 = self.new_course('Course2', self.new_coach('c2'), self.new_coach('a2'))
        student = self.new_student('Student1')
        student.courses.add(course1)
        response = self.http_client.get(reverse_lazy('students:detail', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)
        self.assertNotContains(response, course2.name)

    def test_students_course(self):
        course1 = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        course2 = self.new_course('Course2', self.new_coach('c2'), self.new_coach('a2'))
        student = self.new_student('Student1')
        student.courses.add(course1)
        response = self.http_client.get(reverse_lazy('students:list_view'), {'course_id':course1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)
        self.assertNotContains(response, course2.name)

    def test_template(self):
        student = self.new_student('Student1')
        response = self.http_client.get(reverse_lazy('students:detail', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')