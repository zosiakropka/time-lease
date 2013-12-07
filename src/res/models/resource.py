"""@package res.models.resource
@author: Zosia Sobocinska
@date Dec 7, 2013
"""
from django.db import models
from res.models.time import TimePeriod


class Resource(models.Model):
    """
    Resource whose time should be shared between Users.
    """
    availability = TimePeriod()
    pass
