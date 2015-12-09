from django.db import models
from django.core.urlresolvers import reverse_lazy

from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def get_url(self):
        return reverse_lazy('courses:detail', None, [self.course.id])

    def __unicode__(self):
        return self.subject

