# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Runner(models.Model):
    """
    Represents an individual runner.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        """Return a string representation of the runner."""
        return self.first_name + " " + self.last_name

class Meet(models.Model):
    """
    Represents a meet, marathon, etc.
    """
    meet_name = models.CharField(max_length=255)
    meet_date = models.DateField()

    def __unicode__(self):
        """Return a string representation of the meet."""
        return self.meet_name + ", " + str(self.meet_date)

class Performance(models.Model):
    """
    Table relating runners to their performance in a meet.
    """
    runner = models.ForeignKey(Runner)
    meet = models.ForeignKey(Meet)
    number_distance = models.DecimalField(max_digits=8, decimal_places=1, validators=[MinValueValidator(0)])
    UNIT_CHOICES = (
        ('m', 'm'),
        ('km', 'km'),
        ('mi', 'mi')
    )
    units = models.CharField(choices=UNIT_CHOICES, default='km', max_length=255)
    hours = models.IntegerField(null=True, blank=True,
                                validators=[MinValueValidator(0)])
    minutes = models.IntegerField(validators=[MaxValueValidator(60), MinValueValidator(0)])
    seconds = models.DecimalField(decimal_places=2, max_digits=4,
                                  validators=[MaxValueValidator(60.0), MinValueValidator(00)])

    def __unicode__(self):
        """Return a string representation of the performance."""
        if self.hours:
            hour = str(self.hours)
            minute = ""
            second = ""
            if len(str(self.minutes)) < 2:
                minute = str(self.minutes)
                while len(minute) < 2:
                    minute = "0" + minute
            else:
                minute = str(self.minutes)
            
            secs = str(self.seconds).split('.')
            if len(secs[0]) < 2:
                second = secs[0]
                while len(second) < 2:
                    second = "0" + second
            else:
                second = secs[0]
            
            if len(secs) != 1 and len(secs[1]) != 0 and secs[1] != "00":
                second += "." + secs[1]
    
            #return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
            return hour + ":" + minute + ":" + second
        else:
            minute = ""
            second = ""
            minute = str(self.minutes)
            
            secs = str(self.seconds).split('.')
            if len(secs[0]) < 2:
                second = secs[0]
                while len(second) < 2:
                    second = "0" + second
            else:
                second = secs[0]
            
            if secs[1] != "" and secs[1] != "00":
                second += "." + secs[1]
        
            #return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
            return minute + ":" + second
