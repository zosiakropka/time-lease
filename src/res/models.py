"""@package res.models
@author: Zosia Sobocinska
@date Dec 7, 2013
"""

from django.db import models
from recurrence.fields import RecurrenceField
from django.core.validators import MaxValueValidator
from django.db.models.fields import IntegerField, CharField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class Resource(models.Model):
    """
    Resource whose time should be shared between Users.
    """
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=200)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name


class Occupation(models.Model):
    """
    """
    QUARTERS = 4
    HOURS = 24
    
    BOOK = 'b'
    LIKE = 'l'
    LEVELS = (
        (LIKE, "Like"),
        (BOOK, "Book")
    )
    user = models.ForeignKey(User, related_name="occupations")
    hour = models.IntegerField(validators=[MaxValueValidator(23)])
    quarter = models.IntegerField(validators=[MaxValueValidator(3)])
    resource = ForeignKey(Resource, related_name="occupations")
    quarters = IntegerField()
    recurrences = RecurrenceField()
    level = CharField(max_length=1, choices=LEVELS)

    @property
    def abs_quarter_start(self):
        return 4 * self.hour + self.quarter

    @property
    def abs_quarter_stop(self):
        return self.abs_quarter_start + self.quarters

    @staticmethod
    def abs_quarter(hour, quarter):
        return 4 * hour + quarter

    def __unicode__(self):
        return self.user.username

    def date_overlaps(self, date):
        return date in self.recurrences.rdates

    def quarter_overlaps(self, hour, quarter):
        abs_quarter = self.abs_quarter(hour, quarter)
        return self.abs_quarter_start < abs_quarter and self.abs_quarter_stop > abs_quarter
