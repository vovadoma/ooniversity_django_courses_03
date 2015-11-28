from django.shortcuts import render
from students.models import Student
from courses.models import Course

def list_view(request):
    course_id = request.GET.get('course_id')

    if course_id:
        students = Student.objects.filter(courses=course_id)
    else:
        students = Student.objects.all()

    data = {'students': students}
    return render(request, 'students/list_view.html', data)

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    data = {'student': student}
    return render(request, 'students/detail.html', data)
