from django.shortcuts import render, redirect
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    data = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', data)

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course %s has been successfully added.' % course.name)
            return redirect('index')
    else:
        form = CourseModelForm()
    data = {'form': form}
    return render(request, 'courses/add.html', data)

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=course)
    data = {'form': form}
    return render(request, 'courses/edit.html', data)

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        messages.success(request, '"Course %s has been deleted.' % course.name)
        course.delete()
        return redirect('index')
    data = {'course': course}
    return render(request, 'courses/remove.html', data)

def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % lesson.subject)
            return redirect('courses:detail', course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    data = {'form': form}
    return render(request, 'courses/add_lesson.html', data)