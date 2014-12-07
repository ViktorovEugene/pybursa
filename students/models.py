from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=15)

    def __str__(self):
        return u"%s %s" % (self.surname, self.name)
