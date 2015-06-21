from django.db import models
from venues.models import Venue
from sports.models import Sport

class Team(models.Model):
    name = models.CharField(max_length=200)
    manager = models.CharField(max_length=300)

    team_create_time = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Time Created')
    team_update_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Time Modified')

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
        
    def __str__(self):
        return '%s, %s' % (self.name, self.manager)

    def save(self, *args, **kwargs):
        super(Team, self).save(*args, **kwargs)

 
class League(models.Model):
    name = models.CharField(max_length=200)
    manager = models.CharField(max_length=300)
        
    league_create_time = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Time Created')
    league_update_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Time Modified')

    sports = models.ManyToManyField(Sport)
    teams = models.ManyToManyField(Team)

       
    def __str__(self):
        return '%s, %s' % (self.name, self.manager)

    def save(self, *args, **kwargs):
        super(League, self).save(*args, **kwargs)
     

class Event(models.Model):
    name = models.CharField(max_length=200)
    manager = models.CharField(max_length=300)
    
    event_create_time = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Time Created')
    event_update_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Time Modified')

    venue = models.ForeignKey(Venue)
    leagues = models.ForeignKey(League)
    teams = models.ManyToManyField(Team)
       
    def __str__(self):
        return '%s, %s' % (self.name, self.manager)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)


class MiniEvent(models.Model):
    name = models.CharField(max_length=200)
    manager = models.CharField(max_length=300)
    
    minievent_create_time = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Time Created')
    minievent_update_time = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Time Modified')

    event = models.ForeignKey(Event)
    venue = models.ForeignKey(Venue)
    leagues = models.ForeignKey(League)
    teams = models.ManyToManyField(Team)
       
    def __str__(self):
        return '%s, %s' % (self.name, self.manager)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)