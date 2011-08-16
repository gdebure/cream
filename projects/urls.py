from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from projects.models import Project, Authorization

from projects.views import ProjectUpdateView, AuthorizationUpdateView

urlpatterns = patterns('',
    ##################################
    # Projects 
    (r'^projects/$', login_required()(ListView.as_view( model=Project, context_object_name='projects_list', )), ),
    (r'^projects/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Project, )), ),
    (r'^projects/create/$', permission_required('projects.add_project')(CreateView.as_view( model=Project, success_url='/projects/projects/%(id)s' )), ),
    (r'^projects/(?P<pk>\d+)/update/$', ProjectUpdateView.as_view( model=Project, success_url='/projects/projects/%(id)s' ), ),
    (r'^projects/(?P<pk>\d+)/delete/$', permission_required('projects.delete_project')(DeleteView.as_view( model=Project, success_url='/projects/projects/' )), ),
    ##################################
    
    ##################################
    # Authorizations
    (r'^authorizations/$', login_required()(ListView.as_view( model=Authorization, context_object_name='authorizations_list', )), ),
    (r'^authorizations/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Authorization, )), ),
    (r'^authorizations/create/$', permission_required('authorizations.add_authorization')(CreateView.as_view( model=Authorization, success_url='/authorizations/authorizations/%(id)s' )), ),
    (r'^authorizations/(?P<pk>\d+)/update/$', AuthorizationUpdateView.as_view( model=Authorization, success_url='/authorizations/authorizations/%(id)s' ), ),
    (r'^authorizations/(?P<pk>\d+)/delete/$', permission_required('authorizations.delete_authorization')(DeleteView.as_view( model=Authorization, success_url='/authorizations/authorizations/' )), ),
    ##################################
    
)