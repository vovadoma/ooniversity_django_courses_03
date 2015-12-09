from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course, Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseCreateView, self).get_context_data(**kwargs)
        lessons = Lesson.objects.filter(course=self.object).order_by('order')
        data['title'] = 'Course creation'
        data['lessons'] = lessons
        return data

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Course %s has been successfully added.' % form.cleaned_data['name'])
        return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseUpdateView, self).get_context_data(**kwargs)
        data['title'] = 'Course update'
        return data

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:edit', None, [self.object.id])

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    course_name = ''

    def get_context_data(self, **kwargs):
        data = super(CourseDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Course deletion'
        self.course_name = self.object.name
        return data

    def get_object(self, queryset=None):
        object = super(CourseDeleteView, self).get_object()
        self.course_name = object.name
        return object

    def get_success_url(self):
        messages.success(self.request, 'Course %s has been deleted.' % (self.course_name))
        return reverse_lazy('index')

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        data = super(LessonCreateView, self).get_context_data(**kwargs)
        data['title'] = 'Lesson creation'
        return data

    def form_valid(self, form):
        lesson = form.save()
        messages.success(self.request, 'Lesson %s has been successfully added.' % (lesson.subject))
        return super(LessonCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_url()




