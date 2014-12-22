from django.conf.urls import patterns, include, url
from courses.views import (courses_list, course_item, course_new, 
						  course_edit, course_delete)


urlpatterns = patterns('',

    url(r'^$', courses_list, name='courses_list'),
    url(r'^(?P<course_id>\d+)/$', course_item, name='course_item'),
    url(r'^new/$', course_new, name='course_new'),
    url(r'^edit/(?P<course_id>\d+)/$', course_edit, name='course_edit'),
    url(r'^delete/(?P<course_id>\d+)/$', course_delete, name='course_delete'),

)
