from django.conf.urls import patterns, include, url
from coaches.views import (coaches_list, coach_item, coach_edit, 
						  coach_delete, coach_new)


urlpatterns = patterns('',

    url(r'^$', coaches_list, name='coaches_list'),
    url(r'^new/$', coach_new, name='coach_new'),
    url(r'^(?P<coach_id>\d+)/$', coach_item, name='coach_item'),
    url(r'^edit/(?P<coach_id>\d+)/$', coach_edit, name='coach_edit'),
    url(r'^delete/(?P<coach_id>\d+)/$', coach_delete, name='coach_delete'),


)
