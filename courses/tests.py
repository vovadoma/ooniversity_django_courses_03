from django.test import TestCase
from django.core.urlresolvers import reverse_lazy

from courses.models import Course
from pybursa.db_seed_lib import Db_seed

class CoursesListTest(TestCase, Db_seed):

    def test_empty_course(self):
        response = self.http_client.get(reverse_lazy('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'IT courses main page')
        self.assertContains(response, reverse_lazy('courses:add'))

    def test_add_course(self):
        # test add course by POST request
        response = self.http_client.post(reverse_lazy('courses:add'), {
                            'name': 'Course name',
                            'short_description': 'Short description',
                            'description': 'Description of course',
                            'coach': self.new_coach('coach').id,
                            'assistant': self.new_coach('assistant').id})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.all().count(), 1)

        response = self.http_client.get(reverse_lazy('index'))
        self.assertContains(response, 'Course name'.upper())
        self.assertContains(response, 'Short description'.title())
        self.assertContains(response, reverse_lazy('courses:edit', kwargs={'pk': 1}))
        self.assertContains(response, reverse_lazy('courses:remove', kwargs={'pk': 1}))

    def test_edit_course(self):
        course = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        response = self.http_client.get(reverse_lazy('courses:edit', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, 200)
        for label in ('Name', 'Short description', 'Description', 'Coach', 'Assistant'):
            self.assertContains(response, label)
        for field in ('name', 'short_description', 'description', 'coach', 'assistant'):
            self.assertContains(response, course.__getattribute__(field))

    def test_delete_course(self):
        course = self.new_course('Course2', self.new_coach('c2'), self.new_coach('a2'))
        response = self.http_client.post(reverse_lazy('courses:remove', kwargs={'pk': course.id}))
        self.assertEqual(Course.objects.all().count(), 0)
        self.assertEqual(response.status_code, 302)
        response = self.http_client.post(reverse_lazy('courses:remove', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, 404)

    def test_student_course(self):
        course1 = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        course2 = self.new_course('Course2', self.new_coach('c2'), self.new_coach('a2'))
        student = self.new_student('Student1')
        student.courses.add(course1)
        response = self.http_client.get(reverse_lazy('students:detail', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)
        self.assertNotContains(response, course2.name)

        student.courses.add(course2)
        response = self.http_client.get(reverse_lazy('students:detail', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)
        self.assertContains(response, course2.name)

    def test_coach_course(self):
        coach = self.new_coach('c1');
        assistant = self.new_coach('a1')
        course = self.new_course('Course1', coach, assistant)

        response = self.http_client.get(reverse_lazy('coaches:detail', kwargs={'coach_id': coach.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course.name)

        response = self.http_client.get(reverse_lazy('coaches:detail', kwargs={'coach_id': assistant.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course.name)



class CoursesDetailTest(TestCase, Db_seed):

    def test_empty_course(self):
        response = self.http_client.get(reverse_lazy('courses:detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 404)

    def test_get_course(self):
        course = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        response = self.http_client.get(reverse_lazy('courses:detail', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, 200)
        for field in ('name', 'description'):
            self.assertContains(response, course.__getattribute__(field))

    def test_link(self):
        course = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        response = self.http_client.get(reverse_lazy('courses:detail', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse_lazy('courses:add-lesson', kwargs={'pk': course.id}))

    def test_coach_course(self):
        coach = self.new_coach('c1');
        assistant = self.new_coach('a1')
        course = self.new_course('Course1', coach, assistant)
        response = self.http_client.get(reverse_lazy('courses:detail', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, coach.first_name.upper())
        self.assertContains(response, assistant.first_name.upper())

    def test_add_lesson(self):
        course = self.new_course('Course1', self.new_coach('c1'), self.new_coach('a1'))
        self.new_lesson('Lesson1', course)
        response = self.http_client.get(reverse_lazy('courses:detail', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lesson1')