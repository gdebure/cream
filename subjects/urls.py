from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from subjects.models import Subject

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Subject.objects.order_by('subject_family','name'),
            context_object_name='subjects_list',
        ),
    ),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Subject,
        ),
    ),
    (r'^(?P<pk>\d+)/update/$',
        UpdateView.as_view(
            model=Subject,
            success_url='/subjects/%(id)s'
        ),
    ),
    (r'^create/$',
        CreateView.as_view(
            model=Subject,
            success_url='/subjects/%(id)s'
        ),
    ),
)