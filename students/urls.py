from django.conf.urls import patterns, include, url
from students.views import (students_list, student_item, student_new,
							student_edit, student_delete)

urlpatterns = patterns('',

    url(r'^$', students_list, name='students_list'),
    url(r'^(?P<student_id>\d+)/$', student_item, name='student_item'),
    url(r'^new/$', student_new, name='student_new'),
    url(r'^edit/(?P<student_id>\d+)/$', student_edit, name='student_edit'),
    url(r'^delete/(?P<student_id>\d+)/$', student_delete, name='student_delete'),
)
