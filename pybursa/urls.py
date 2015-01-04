from django.views.generic import TemplateView

from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa.views import DelationView


urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='pybursa/base.html'), name='home'),
    url(r'^students/', include('students.urls'), name='students'),
    url(r'^courses/', include('courses.urls'), name='courses'),
    url(r'^coaches/', include('coaches.urls'), name='coaches'),
    url(r'^address/', include('address.urls'), name='addresses'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', DelationView.as_view(), name='delation' ),
)
