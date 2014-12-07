from django.db import models


class Coach(models.Model):

    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    topic = models.CharField(max_length=225)

    def __str__(self):
        #return u"%s %s" % (self.surname, self.name)
        return self.topic
