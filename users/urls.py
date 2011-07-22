from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from users.models import Employee, EmployeeForm

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Employee.objects.order_by('-id'),
            context_object_name='employees_list',
            ),),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Employee,
            ),),
    (r'^(?P<pk>\d+)/update/$',
        UpdateView.as_view(
            model=EmployeeForm,
        ),
    ),
    (r'^create/$',
        CreateView.as_view(
            model=Employee,
        ),
    ),
)