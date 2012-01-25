from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from projects.models import Project, Deliverable, DeliverableVolume, Task
from projects.forms import DeliverableForm, DeliverableValidateServiceForm

from projects.views import update_project, delete_project
from projects.views import create_deliverable, update_deliverable, delete_deliverable, validate_deliverable_service
from projects.views import create_deliverablevolume, update_deliverablevolume, delete_deliverablevolume
from projects.views import create_task, create_task_from_project, update_task, update_task_answer, delete_task

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
    # Add task to a project
    (r'^projects/(?P<pk>\d+)/add_task/$',create_task_from_project),
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
    (r'^deliverables/(?P<pk>\d+)/add_volume/$', create_deliverablevolume),
    (r'^deliverables/(?P<pk>\d+)/add_task/$', create_task),
    ##################################
    
    
    ##################################
    # Deliverable Volumes
    (r'^deliverablevolumes/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=DeliverableVolume, )), ),
    (r'^deliverablevolumes/(?P<pk>\d+)/update/$', update_deliverablevolume),
    (r'^deliverablevolumes/(?P<pk>\d+)/delete/$', delete_deliverablevolume),
    ##################################
    
    
    ##################################
    # Tasks
    (r'^tasks/$', login_required()(ListView.as_view( model=Task, context_object_name='tasks_list', )), ),
    (r'^tasks/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Task, )), ),
    (r'^tasks/create/$', permission_required('projects.add_task')(CreateView.as_view( model=Task, success_url='/projects/tasks/%(id)s' )), ),
    (r'^tasks/(?P<pk>\d+)/update/$', update_task),
    (r'^tasks/(?P<pk>\d+)/update_answer/$', update_task_answer),
    (r'^tasks/(?P<pk>\d+)/delete/$', delete_task),
    ##################################
)