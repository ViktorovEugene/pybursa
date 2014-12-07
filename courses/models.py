from django.db import models


class Course(models.Model):

    language = models.CharField(max_length=225)
    course_name = models.CharField(max_length=225)
    instructor = models.CharField(max_length=225)
    assistant = models.CharField(max_length=225)
    description= models.TextField()
    date_of_start = models.DateField()
    date_of_end = models.DateField()

    def __str__(self):
        return self.course_name
