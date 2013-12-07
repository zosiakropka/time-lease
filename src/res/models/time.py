"""@package res.models.time
@author: Zosia Sobocinska
@date Dec 7, 2013
"""
from django.db import models
from django.core.validators import MaxValueValidator


class TimeUnit(models.Model):
    """
    """
    date = models.DateField()
    hour = models.IntegerField(validators=[MaxValueValidator(23)])
    quarter = models.IntegerField(validators=[MaxValueValidator(3)])


class TimePeriod(models.Model):
    start = TimeUnit()
    stop = TimeUnit()
    pass
