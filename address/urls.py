from django.conf.urls import patterns, include, url
from address.views import (course_addresses, course_address,
						   AddressListView)


urlpatterns = patterns('',

	url(r'^$', AddressListView.as_view(), name='course_addresses'),
    # url(r'^$', course_addresses, name='course_addresses'),
    url(r'^(?P<address_id>\d+)/$', course_address,
    								name='course_address',),

)
