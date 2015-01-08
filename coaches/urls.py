from django.conf.urls import patterns, include, url
from coaches.views import (CoachListView, CoachDetailView, CoachUpdateView, 
						  CoachDeleteView, CoachCreateView)


urlpatterns = patterns('',

    url(r'^$', CoachListView.as_view(), name='coaches_list'),
    url(r'^new/$', CoachCreateView.as_view(), name='coach_new'),
    url(r'^(?P<pk>\d+)/$', CoachDetailView.as_view(), name='coach_item'),
    url(r'^edit/(?P<pk>\d+)/$', CoachUpdateView.as_view(), name='coach_edit'),
    url(r'^delete/(?P<pk>\d+)/$', CoachDeleteView.as_view(), name='coach_delete'),


)
