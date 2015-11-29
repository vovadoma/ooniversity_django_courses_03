from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username

    def _get_first_name(self):
        return self.user.first_name

    def _get_last_name(self):
        return self.user.last_name

    first_name = property(_get_first_name)
    last_name = property(_get_last_name)


