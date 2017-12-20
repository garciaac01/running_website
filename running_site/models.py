# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    number_distance = models.IntegerField()
    UNIT_CHOICES = (
        ('m', 'm'),
        ('km', 'km'),
        ('mi', 'mi')
    )
    units = models.CharField(choices=UNIT_CHOICES, default='km', max_length=255)
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.DecimalField(decimal_places=2, max_digits=2)

    def __unicode__(self):
        """Return a string representation of the performance."""
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
