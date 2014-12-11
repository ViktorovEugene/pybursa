from django.db import models
from address.models import Address

from coaches.models import Coach


class Course(models.Model):
    TECNOLOGY_CHOISE = (
        ('p', 'Python'),
        ('r', 'Ruby'),
        ('j', 'JavaScript'),
    )
    name = models.CharField(max_length=225)
    description= models.TextField()
    coach = models.ForeignKey(Coach)
    assistant = models.ForeignKey(Coach, blank=True, null=True,
                                  related_name='course_assistant')
    start_date = models.DateField()
    end_date = models.DateField()
    tecnology = models.CharField(max_length=225, choices=TECNOLOGY_CHOISE)
    venue = models.ForeignKey(Address, related_name='course_venue')

    def __unicode__(self):
        return '%s (%s) - %s' % (self.name, self.coach, self.tecnology)
