from django.conf.urls import patterns, url
from students.views import (StudentListView, StudentDetailView, StudentUpdateView, 
						  StudentDeleteView, StudentCreateView)

urlpatterns = patterns('',

    url(r'^$', StudentListView.as_view(), name='students_list'),
    url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='student_item'),
    url(r'^new/$', StudentCreateView.as_view(), name='student_new'),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='student_edit'),
    url(r'^delete/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name='student_delete'),
)
