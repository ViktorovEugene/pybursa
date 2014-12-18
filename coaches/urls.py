from django.conf.urls import patterns, include, url
from coaches.views import coaches_list, coaches_item


urlpatterns = patterns('',

    url(r'^$', coaches_list, name='coaches_list'),
    url(r'^(?P<coach_id>\d+)/$', coaches_item, name='coaches_item'),

)
