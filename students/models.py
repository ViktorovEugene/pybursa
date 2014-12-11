from django.db import models

from courses.models import Course


class Student(models.Model):
    PACKAGE_CHOISES = (
        ('s', 'Standart'),
        ('g', 'Glod'),
        ('p', 'Platinum'),
    )
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    courses = models.ManyToManyField(Course, blank=True)
    package = models.CharField(max_length=1, choices=PACKAGE_CHOISES,
                               default='s')

    def __unicode__(self):
        return u"%s %s" % (self.surname, self.name)
