from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models import Student
from django.contrib import messages

class StudentDetailView(DetailView):
    model = Student

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()

        paginator = Paginator(students, 2)
        page = self.request.GET.get('page')
        try:
            students_list = paginator.page(page)
        except PageNotAnInteger:
            students_list = paginator.page(1)
        except EmptyPage:
            students_list = paginator.page(paginator.num_pages)
        return students_list

    def get_context_data(self, **kwargs):
        data = super(StudentListView, self).get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id')
        if not course_id:
            course_link = ''
        else:
            course_link = '&course_id=%s' % course_id
        data['course_link'] = course_link
        return data

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

    def get_context_data(self, **kwargs):
        data = super(StudentDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Student info suppression'
        return data

    def delete(self, request, *args, **kwargs):
        ret_msg = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (self.object.name, self.object.surname))
        return ret_msg

