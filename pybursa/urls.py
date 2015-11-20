from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello')

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
)