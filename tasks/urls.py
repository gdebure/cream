from django.conf.urls.defaults import *

urlpatterns = patterns('tasks.views',
    (r'^$', 'index'),
    (r'^(?P<task_id>\d+)/$', 'detail'),
)