from django.conf.urls import patterns, include, url
from students.views import students_list, student_item


urlpatterns = patterns('',

    url(r'^$', students_list, name='students_list'),
    url(r'^(?P<student_id>\d+)/$', student_item, name='student_item'),

)
