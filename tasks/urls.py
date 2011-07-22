from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from tasks.models import Task, TaskForm

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Task.objects.order_by('-id'),
            context_object_name='tasks_list',
        ),
    ),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Task,
        ),
    ),
    (r'^(?P<pk>\d+)/update/$',
        UpdateView.as_view(
            model=Task,
        ),
    ),
    (r'^create/$',
        CreateView.as_view(
            model=Task,
        ),
    ),
)