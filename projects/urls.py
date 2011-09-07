from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from projects.models import Project, Authorization, Deliverable, DeliverableVolume, Turnover, Task
from projects.forms import DeliverableForm, DeliverableValidateServiceForm

from projects.views import update_project, delete_project
from projects.views import update_authorization, delete_authorization
from projects.views import create_deliverable, update_deliverable, delete_deliverable, validate_deliverable_service
from projects.views import update_deliverablevolume
from projects.views import update_turnover, delete_turnover
from projects.views import update_task, delete_task

urlpatterns = patterns('',
    ##################################
    # Projects 
    (r'^projects/$', login_required()(ListView.as_view( model=Project, context_object_name='projects_list', )), ),
    (r'^projects/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Project, )), ),
    (r'^projects/create/$', permission_required('projects.add_project')(CreateView.as_view( model=Project, success_url='/projects/projects/%(id)s' )), ),
    (r'^projects/(?P<pk>\d+)/update/$', update_project),
    (r'^projects/(?P<pk>\d+)/delete/$', delete_project),
    # Add deliverable to a project
    (r'^projects/(?P<pk>\d+)/add_deliverable/$', create_deliverable),
    ##################################
    
    ##################################
    # Authorizations
    (r'^authorizations/$', login_required()(ListView.as_view( model=Authorization, context_object_name='authorizations_list', )), ),
    (r'^authorizations/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Authorization, )), ),
    (r'^authorizations/create/$', permission_required('projects.add_authorization')(CreateView.as_view( model=Authorization, success_url='/authorizations/authorizations/%(id)s' )), ),
    (r'^authorizations/(?P<pk>\d+)/update/$', update_authorization ),
    (r'^authorizations/(?P<pk>\d+)/delete/$', delete_authorization ),
    ##################################
    
    ##################################
    # Deliverables
    (r'^deliverables/$', login_required()(ListView.as_view( model=Deliverable, context_object_name='deliverables_list', )), ),
    (r'^deliverables/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Deliverable, )), ),
    (r'^deliverables/create/$', permission_required('projects.add_deliverable')(CreateView.as_view( model=Deliverable, form_class=DeliverableForm, success_url='/projects/deliverables/%(id)s' )), ),
    (r'^deliverables/(?P<pk>\d+)/update/$', update_deliverable),
    (r'^deliverables/(?P<pk>\d+)/delete/$', delete_deliverable),
    # Service validation stuff
    (r'^deliverables/(?P<pk>\d+)/validate_service/$', validate_deliverable_service),
    ##################################
    
    ##################################
    # Deliverables Volumes
    (r'^deliverablevolumes/$', login_required()(ListView.as_view( model=DeliverableVolume, context_object_name='deliverablevolumes_list', )), ),
    (r'^deliverablevolumes/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=DeliverableVolume, )), ),
    (r'^deliverablevolumes/create/$', permission_required('projects.add_deliverablevolume')(CreateView.as_view( model=DeliverableVolume, success_url='/projects/deliverablevolumes/%(id)s' )), ),
    (r'^deliverablevolumes/(?P<pk>\d+)/update/$', update_deliverablevolume),
    #(r'^deliverablevolumes/(?P<pk>\d+)/delete/$', delete_deliverablevolume),
    ##################################
    
    
    ##################################
    # Task values
    (r'^tasks/$', login_required()(ListView.as_view( model=Task, context_object_name='tasks_list', )), ),
    (r'^tasks/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Task, )), ),
    (r'^tasks/create/$', permission_required('projects.add_task')(CreateView.as_view( model=Task, success_url='/projects/tasks/%(id)s' )), ),
    (r'^tasks/(?P<pk>\d+)/update/$', update_task),
    (r'^tasks/(?P<pk>\d+)/delete/$', delete_task),
    ##################################
)