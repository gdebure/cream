from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from users.models import Employee

from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', ),
    (r'^employees/$', login_required()(ListView.as_view( queryset=Employee.objects.order_by('id'), context_object_name='employees_list', )),),
    (r'^employees/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Employee, )),),
    
)