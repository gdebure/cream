from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from projects.models import Project, Authorization, Deliverable, Turnover, Task
from projects.forms import DeliverableForm, DeliverableValidateServiceForm

from projects.views import ProjectUpdateView, AuthorizationUpdateView, DeliverableUpdateView, TurnoverUpdateView, TaskUpdateView, validate_deliverable_service

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
    (r'^authorizations/create/$', permission_required('projects.add_authorization')(CreateView.as_view( model=Authorization, success_url='/authorizations/authorizations/%(id)s' )), ),
    (r'^authorizations/(?P<pk>\d+)/update/$', AuthorizationUpdateView.as_view( model=Authorization, success_url='/projects/authorizations/%(id)s' ), ),
    (r'^authorizations/(?P<pk>\d+)/delete/$', permission_required('projects.delete_authorization')(DeleteView.as_view( model=Authorization, success_url='/authorizations/authorizations/' )), ),
    ##################################
    
    ##################################
    # Deliverables
    (r'^deliverables/$', login_required()(ListView.as_view( model=Deliverable, context_object_name='deliverables_list', )), ),
    (r'^deliverables/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Deliverable, )), ),
    (r'^deliverables/create/$', permission_required('projects.add_deliverable')(CreateView.as_view( model=Deliverable, form_class=DeliverableForm, success_url='/projects/deliverables/%(id)s' )), ),
    (r'^deliverables/(?P<pk>\d+)/update/$', permission_required('projects.change_deliverable')(UpdateView.as_view( model=Deliverable, form_class=DeliverableForm, success_url='/projects/deliverables/%(id)s' ), )),
    (r'^deliverables/(?P<pk>\d+)/delete/$', permission_required('projects.delete_deliverable')(DeleteView.as_view( model=Deliverable, success_url='/projects/deliverables/' )), ),
    # Service validation stuff
    (r'^deliverables/(?P<pk>\d+)/validate_service/$', validate_deliverable_service),
    ##################################
    
    ##################################
    # Turnover values
    (r'^turnover_values/$', login_required()(ListView.as_view( model=Turnover, context_object_name='turnover_values_list', )), ),
    (r'^turnover_values/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Turnover, )), ),
    (r'^turnover_values/create/$', permission_required('projects.add_turnover')(CreateView.as_view( model=Turnover, success_url='/projects/turnover_values/%(id)s' )), ),
    (r'^turnover_values/(?P<pk>\d+)/update/$', TurnoverUpdateView.as_view( model=Turnover, success_url='/projects/turnover_values/%(id)s' ), ),
    (r'^turnover_values/(?P<pk>\d+)/delete/$', permission_required('projects.delete_turnover')(DeleteView.as_view( model=Turnover, success_url='/projects/turnover_values/' )), ),
    ##################################
    
    ##################################
    # Task values
    (r'^tasks/$', login_required()(ListView.as_view( model=Task, context_object_name='tasks_list', )), ),
    (r'^tasks/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Task, )), ),
    (r'^tasks/create/$', permission_required('projects.add_task')(CreateView.as_view( model=Task, success_url='/projects/tasks/%(id)s' )), ),
    (r'^tasks/(?P<pk>\d+)/update/$', TaskUpdateView.as_view( model=Task, success_url='/projects/tasks/%(id)s' ), ),
    (r'^tasks/(?P<pk>\d+)/delete/$', permission_required('projects.delete_task')(DeleteView.as_view( model=Task, success_url='/projects/tasks/' )), ),
    ##################################
)