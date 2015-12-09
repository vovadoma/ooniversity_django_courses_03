from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student
from django.contrib import messages

class StudentDetailView(DetailView):
    model = Student

class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentCreateView, self).get_context_data(**kwargs)
        data['title'] = 'Student registration'
        return data

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentUpdateView, self).get_context_data(**kwargs)
        data['title'] = 'Student info update'
        return data

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('students:edit', None, [self.object.id])

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    student_name = ''
    student_surname = ''

    def get_context_data(self, **kwargs):
        data = super(StudentDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Student info suppression'
        return data

    def get_object(self, queryset=None):
        object = super(StudentDeleteView, self).get_object()
        self.student_name = object.name
        self.student_surname = object.surname
        return object

    def get_success_url(self):
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (self.student_name, self.student_surname))
        return self.success_url
