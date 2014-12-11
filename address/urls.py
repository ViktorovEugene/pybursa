from django.conf.urls import patterns, include, url
from address.views import course_addresses, course_address


urlpatterns = patterns('',

    url(r'^$', course_addresses),
    url(r'^(?P<address_id>\d+)/$', course_address),

)
