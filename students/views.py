from django.conf.urls import patterns
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


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Student info suppression'
        return data

    def get_object(self, queryset=None):
        object = super(StudentDeleteView, self).get_object()
        if object:
            messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (object.name, object.surname))
        return object



# def create(request):
#     if request.method == "POST":
#         form = StudentModelForm(request.POST)
#         if form.is_valid():
#             student = form.save()
#             messages.success(request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
#             return redirect('students:list_view')
#     else:
#         form = StudentModelForm()
#     data = {'form': form}
#     return render(request, 'students/add.html', data)

# def edit(request, student_id):
#     student = Student.objects.get(id=student_id)
#     if request.method == "POST":
#         form = StudentModelForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Info on the student has been sucessfully changed.')
#     else:
#         form = StudentModelForm(instance=student)
#     data = {'form': form}
#     return render(request, 'students/edit.html', data)
#
# def remove(request, student_id):
#     student = Student.objects.get(id=student_id)
#     if request.method == "POST":
#         student.delete()
#         messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
#         return redirect('students:list_view')
#     data = {'student': student}
#     return render(request, 'students/remove.html', data)
