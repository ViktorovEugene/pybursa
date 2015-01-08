from django.conf.urls import patterns, include, url
from address.views import AddressListView, AddressDetailView


urlpatterns = patterns('',

	url(r'^$', AddressListView.as_view(), name='course_addresses'),
    # url(r'^$', course_addresses, name='course_addresses'),
    url(r'^(?P<pk>\d+)/$', AddressDetailView.as_view(),
    								name='course_address',),

)
