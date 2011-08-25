from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done
from users.models import Employee

from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    ###################################
    # Authentication stuff
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'} ),
    (r'^logout/$', logout_then_login, ),
    (r'^change_password/$', password_change, {'template_name': 'users/password_change_form.html','post_change_redirect' : '/users/change_password/done/'} ),
    (r'^change_password/done/$', password_change_done, {'template_name': 'users/password_change_done.html'} ),
    ###################################
    
    (r'^employees/$', login_required()(ListView.as_view( queryset=Employee.objects.order_by('id'), context_object_name='employees_list', )),),
    (r'^employees/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Employee, )),),
    
)