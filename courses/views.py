from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    data = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', data)