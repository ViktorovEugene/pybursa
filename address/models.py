from django.db import models
# from courses.models import Course

class Address(models.Model):
    post_index = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s, %s, %s' % (self.country, self.region, self.street)



class Dossier(models.Model):
 	COLOR_CHOISES = (
 		('red', 'red'),
 		('orange', 'orange'),
 		('yellow', 'yellow'),
 		('green', 'green'),
 		('azure', 'azure'),
 		('blue', 'blue'),
 		('violet', 'violet'),
 	)
	address = models.ForeignKey(Address, related_name='dissier_address',
		blank=True)
	courses = models.ManyToManyField('courses.Course', blank=True, 
		related_name='dossier_courses')
	color = models.CharField(max_length=6, choices=COLOR_CHOISES, default='red')
    
	def __unicode__(self):
		return self.color