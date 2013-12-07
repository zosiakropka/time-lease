"""@package res.models.occupation
@author: Zosia Sobocinska
@date Dec 7, 2013
"""
from django.db import models
from res.models.time import TimePeriod


class BaseOccupation(models.Model):
    """
    """
    period = TimePeriod()


class SingleOccupation(BaseOccupation):
    """
    """
    period = TimePeriod()


class RecurrentOccupation(BaseOccupation):
    begin = models.DateField(null=False)
    end = models.DateField(null=False)
    period = TimePeriod()
    DAILY = 1
    WEEKLY = 7
    WEEKLY2 = 14
    SCHEDULING_CHOICES = (
        (DAILY, 'daily'),
        (WEEKLY, 'weekly'),
        (WEEKLY2, 'each 2 weeks'),
    )
    scheduling = models.IntegerField(choices=SCHEDULING_CHOICES)

    def units(self):
        
        pass
