from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname+' '+self.name

    def _get_full_name(self):
        return self.name+' '+self.surname

    full_name = property(_get_full_name)
