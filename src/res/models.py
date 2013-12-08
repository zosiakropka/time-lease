"""@package res.models
@author: Zosia Sobocinska
@date Dec 7, 2013
"""

from django.db import models
from recurrence.fields import RecurrenceField
from django.core.validators import MaxValueValidator
from django.db.models.fields import IntegerField


class Resource(models.Model):
    """
    Resource whose time should be shared between Users.
    """
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=200)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name


class DayPoint(models.Model):
    """
    """
    hour = models.IntegerField(validators=[MaxValueValidator(23)])
    quarter = models.IntegerField(validators=[MaxValueValidator(3)])


class Occupation(models.Model):
    """
    """
    daypoint = DayPoint()
    quarters = IntegerField()


class SingleOccupation(Occupation):
    """
    """
    date = models.TimeField()


class MultiOccupation(Occupation):
    """
    """
    start = models.TimeField()
    end = models.TimeField()
    recurrences = RecurrenceField()
