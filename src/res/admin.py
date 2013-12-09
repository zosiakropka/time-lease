"""@package res.admin
@author: Zosia Sobocinska
@date Dec 8, 2013
"""

from django.contrib import admin
from res.models import Resource, Occupation


admin.site.register(Resource)
admin.site.register(Occupation)
