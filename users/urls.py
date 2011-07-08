from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from users.models import Employee

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
)