"""@package res.templatetags.res_extras
@author Zosia Sobocinska
@date Dec 10, 2013
"""
from django import template

register = template.Library()


@register.filter
def urly_hour(value):
    return value.replace(':', '/')
