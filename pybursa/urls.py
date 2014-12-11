from django.views.generic import TemplateView

from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='pybursa/index.html'), name='home'),
    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^address/', include('address.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
