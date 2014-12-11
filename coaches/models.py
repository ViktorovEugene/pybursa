from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    COACH_TYPES = (
        ('C', 'Coach'),
        ('A', 'Assistant'),
    )
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    email = models.EmailField(default='example@gmail.com')
    status = models.CharField(choices=COACH_TYPES, max_length=1,)
    phone_number = models.CharField(max_length=15, default='+38000000000')
    user = models.ForeignKey(User, blank=True, default='')

    def __unicode__(self):
        return "%s %s (%s)" % (self.surname, self.name, self.status)
