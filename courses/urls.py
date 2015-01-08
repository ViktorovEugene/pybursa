from django.conf.urls import patterns, include, url
# from courses.views import (courses_list, course_item, course_new, 
# 						  course_edit, course_delete)
from courses.views import (CourseListView, CourseDetailView, CourseUpdateView, 
						  CourseDeleteView, CourseCreateView)


urlpatterns = patterns('',

    url(r'^$', CourseListView.as_view(), name='courses_list'),
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='course_item'),
    url(r'^new/$', CourseCreateView.as_view(), name='course_new'),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='course_edit'),
    url(r'^delete/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='course_delete'),

)
