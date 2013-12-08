"""@package res.urls
@author: Zosia Sobocinska
@date Dec 8, 2013
"""

from django.conf.urls import patterns, url

from django.contrib import admin
from django.utils import timezone
admin.autodiscover()

urlpatterns = patterns('')
urlpatterns += patterns('res.views',
    url(r'^$', 'resource_list'),
    url(r'^(?P<resource_slug>[a-zA-Z0-9_.-]+)?/$',
        'resource_detail',
        {"year": timezone.now().year, "month": timezone.now().month}),
    url(r'^(?P<resource_slug>[a-zA-Z0-9_.-]+)/(?P<year>\d{4})-(?P<month>\d{2})?/$',
        'resource_detail'),
    url(r'^(?P<resource_slug>[a-zA-Z0-9_.-]+)/(?P<year>\d{4})-(?P<month>\d{2})?/(prev|next)?/$',
        'resource_detail', {}),
    url(r'^(?P<resource_slug>[a-zA-Z0-9_.-]+)/(prv|nxt)?/$',
        'resource_detail', {}),
)
