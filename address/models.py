from django.db import models

class Address(models.Model):
    post_index = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s, %s, %s' % (self.country, self.region, self.street)
