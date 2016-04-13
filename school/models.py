from django.db import models
from user.models import MyUser
from utils.choices import SCHOOL_CHOICES

# Create your models here.
class Team(models.Model):
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    #Relations
    my_user = models.ForeignKey(MyUser, related_name='teams', blank=False)

    #Attributes
    name = models.CharField(max_length=50, unique=True, blank=False)
    school = models.CharField(max_length=50, choices=SCHOOL_CHOICES, blank=False)

    def __str__(self):
        return self.name

class Leader(models.Model):
    class Meta:
        verbose_name = 'Leader'
        verbose_name_plural = 'Leaders'

    # Relations
    team = models.ForeignKey(Team, related_name='leaders', blank=False)

    # Attributes
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    school = models.CharField(max_length=50, choices=SCHOOL_CHOICES)

    def __str__(self):
        return self.first_name


class Kid(models.Model):
    class Meta:
        verbose_name = 'Kid'
        verbose_name_plural = 'Kids'

    #Relations
    team = models.ForeignKey(Team, related_name='kids', blank=False)

    #Attributes
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.first_name

class Bitacora(models.Model):
    class Meta:
        verbose_name = 'Bitacora'
        verbose_name_plural = 'Bitacoras'

    #Relations
    kid = models.ForeignKey(Kid)

    #Attributes
    date = models.DateField(auto_now=False)
    assistance = models.BooleanField(default=False, blank=True)
    week_talk = models.BooleanField(default=False, blank=True)
