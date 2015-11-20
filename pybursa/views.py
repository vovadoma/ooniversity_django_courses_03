from django.shortcuts import render
from django.conf.urls.static import static


def index(request):
    return render(request, "{% url 'pybursa:index' %}")
    #return render(request, "index.html")
    
    
def contact(request):
    return render(request, "{% url 'contact' %}")
    
def student_list(request):
    return render(request, "{% url 'student_list' %}")
    
def student_detail(request):
    return render(request, "{% url 'student_detail' %}")

