from django.conf.urls import patterns, include, url
from django import template
from django.contrib import admin
from views import contact
from views import student_list
from views import student_detail
from views import index
from . import views
from django.conf.urls.static import static


urlpatterns = patterns('',
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^contact/', contact, name='contact'),
    url(r'^student_list/', student_list, name='student_list'),
    url(r'^student_detail/', student_detail, name='student_detail'),
    
)
