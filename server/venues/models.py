from django.db import models
from sports.models import Sport

class Venue(models.Model):
    ''' Model features for an venue registration '''
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    timings = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)

    venue_create_time = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Time Created')
    venue_update_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Time Modified')

    sports = models.ManyToManyField(Sport)

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.name, self.location, self.sports, self.timings, self.contactno)

    def save(self, *args, **kwargs):
        super(Venue, self).save(*args, **kwargs)
