from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id:
        students = Student.objects.filter(courses=course_id)
    else:
        students = Student.objects.all()
    data = {'students': students}
    return render(request, 'students/list.html', data)

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    data = {'student': student}
    return render(request, 'students/detail.html', data)

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
            return redirect('students:list')
    else:
        form = StudentModelForm()
    data = {'form': form}
    return render(request, 'students/add.html', data)

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=student)
    data = {'form': form}
    return render(request, 'students/edit.html', data)

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return redirect('students:list')
    data = {'student': student}
    return render(request, 'students/remove.html', data)
