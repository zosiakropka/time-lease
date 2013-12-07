"""@package account.urls
@author: Zosia Sobocinska
@date Dec 7, 2013
"""

from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('')
urlpatterns += patterns('account.views',
    url(r'^signin/$', 'signin'),
    url(r'^signup/$', 'signup'),
)
