from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

from pybursa import views
from quadratic import views as views_q

def index(request):
    return HttpResponse('hello')

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^quadratic/results/', views_q.quadratic_results, name='equation'),

    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
)
