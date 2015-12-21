from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course, Lesson
from pybursa.views import MixinMsg, MixinTitle

import logging
course_logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseDetailView, self).get_context_data(**kwargs)
        lessons = Lesson.objects.filter(course=self.object).order_by('order')
        data['lessons'] = lessons

        #logger
        #course_logger.debug("Courses detail view has been debugged")
        #course_logger.info("Logger of courses detail view informs you!")
        #course_logger.warning("Logger of courses detail view warns you!")
        #course_logger.error("Courses detail view went wrong!")

        return data

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseCreateView, self).get_context_data(**kwargs)
        data['title'] = 'Course creation'
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

    def get_context_data(self, **kwargs):
        data = super(CourseDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Course deletion'
        return data

    def delete(self, request, *args, **kwargs):
        ret_msg = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Course %s has been deleted.' % (self.object.name))
        return ret_msg

class LessonCreateView(MixinMsg, MixinTitle, CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lesson'
    title = 'Lesson creation'
    success_message = {'msg': 'Lesson %s has been successfully added.', 'attr': 'subject'}

    def get_success_url(self):
        return self.object.get_url()

    def get_initial(self):
        return {'course': self.kwargs['pk']}




