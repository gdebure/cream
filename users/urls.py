from django.conf.urls import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done
from users.models import Employee

from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = patterns('',
    ###################################
    # Authentication stuff
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login' ),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^change_password/$', password_change, {'template_name': 'password_change_form.html','post_change_redirect' : 'change_password/done/'}, name='change_password' ),
    url(r'^change_password/done/$', password_change_done, {'template_name': 'password_change_done.html'}, name='password_changed' ),
    ###################################
    
    url(r'^employees/$', login_required()(ListView.as_view( queryset=Employee.objects.order_by('id'), context_object_name='employees_list', template_name='employee_list.html' )), name='employees_list'),
    url(r'^employees/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Employee, template_name='employee_detail.html')),name='employee'),
    url(r'^employees/create/$', permission_required('users.add_employee')(CreateView.as_view( model=Employee, )), name='create_employee'),
)