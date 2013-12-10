"""@package res.urls
@author: Zosia Sobocinska
@date Dec 8, 2013
"""

from django.conf.urls import patterns, url

from django.utils import timezone

urlpatterns = patterns('')
urlpatterns += patterns('res.views',
    url(r'^$', 'resource_list'),

    url(r'^(?P<resource_slug>[a-zA-Z0-9_.-]+)?/$',
        'resource_calendar',
        {"year": timezone.now().year, "month": timezone.now().month},
        name="resource_calendar"),

    url(r'^(?P<resource_slug>[a-zA-Z0-9_.-]+)/(?P<year>\d{4})-(?P<month>\d{1,2})?/$',
        'resource_calendar',
        name="resource_calendar"),

    url(r'^(?P<resource_slug>[a-zA-Z0-9_.-]+)/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})?/(?P<hour>\d{1,2})/(?P<minute>\d{1,2})?/$',
        'resource_book',
        name="resource_book"),
)
