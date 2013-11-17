from django.conf.urls import patterns,url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from projects.models import Project, Deliverable, DeliverableVolume, Task

from projects.views import AddDeliverableView, AddDeliverableVolumeView

urlpatterns = patterns('',
    ##################################
    # Projects 
    url(r'^projects/$', login_required()(ListView.as_view( model=Project, context_object_name='projects_list', template_name='project_list.html' )), name='projects_list'),
    url(r'^projects/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Project, template_name='project_detail.html' )), name='project'),
    url(r'^projects/create/$', permission_required('projects.add_project')(CreateView.as_view( model=Project, template_name='project_form.html' )), name='create_project'),
    url(r'^projects/(?P<pk>\d+)/update/$', permission_required('projects.change_project')(UpdateView.as_view( model=Project, template_name='project_form.html' )), name='update_project'),
    url(r'^projects/(?P<pk>\d+)/delete/$', permission_required('projects.delete_project')(DeleteView.as_view( model=Project, template_name='project_confirm_delete.html', success_url=reverse_lazy('projects_list' ))), name='delete_project'),
    # Add deliverable to a project
    url(r'^projects/(?P<pk>\d+)/add_deliverable/$', permission_required('projects.change_project')(AddDeliverableView.as_view( model=Deliverable, template_name='deliverable_form.html' )), name='add_deliverable'),
    # Add task to a project
    #url(r'^projects/(?P<pk>\d+)/add_task/$',create_task_from_project),
    ##################################
    
    ##################################
    # Deliverables
    url(r'^deliverables/$', login_required()(ListView.as_view( model=Deliverable, context_object_name='deliverables_list', template_name='deliverable_list.html' )), name='deliverables_list' ),
    url(r'^deliverables/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Deliverable, template_name='deliverable_detail.html' )), name='deliverable'),
    url(r'^deliverables/create/$', permission_required('projects.add_deliverable')(CreateView.as_view( model=Deliverable, template_name='deliverable_form.html' )), name='create_deliverable'),
    url(r'^deliverables/(?P<pk>\d+)/update/$', permission_required('projects.change_deliverable')(UpdateView.as_view( model=Deliverable, template_name='deliverable_form.html' )), name='update_deliverable'),
    url(r'^deliverables/(?P<pk>\d+)/delete/$', permission_required('projects.delete_deliverable')(DeleteView.as_view( model=Deliverable, template_name='deliverable_confirm_delete.html', success_url=reverse_lazy('deliverables_list') )), name='delete_deliverable'),
    ## Service validation stuff
    #url(r'^deliverables/(?P<pk>\d+)/validate_service/$', validate_deliverable_service),
    url(r'^deliverables/(?P<pk>\d+)/add_volume/$', permission_required('projects.change_deliverable')(AddDeliverableVolumeView.as_view( model=DeliverableVolume, template_name='deliverablevolume_form.html' )), name='add_deliverablevolume'),
    #url(r'^deliverables/(?P<pk>\d+)/add_task/$', create_task),
    ##################################
    
    
    ##################################
    # Deliverable Volumes
    url(r'^deliverablevolumes/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=DeliverableVolume, template_name='deliverablevolume_detail.html', )), name='deliverablevolume'),
    url(r'^deliverablevolumes/(?P<pk>\d+)/update/$', permission_required('projects.change_deliverablevolume')(UpdateView.as_view( model=DeliverableVolume, template_name='deliverablevolume_form.html' )), name='update_deliverablevolume'),
    url(r'^deliverablevolumes/(?P<pk>\d+)/delete/$', permission_required('projects.delete_deliverablevolume')(DeleteView.as_view( model=DeliverableVolume, template_name='deliverablevolume_confirm_delete.html' )), name='delete_deliverablevolume'),
    ##################################
    
    
    ##################################
    # Tasks
    #url(r'^tasks/$', login_required()(ListView.as_view( model=Task, context_object_name='tasks_list', )), ),
    #url(r'^tasks/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Task, )), ),
    #url(r'^tasks/create/$', permission_required('projects.add_task')(CreateView.as_view( model=Task, success_url='/projects/tasks/%(id)s' )), ),
    #url(r'^tasks/(?P<pk>\d+)/update/$', update_task),
    #url(r'^tasks/(?P<pk>\d+)/update_answer/$', update_task_answer),
    #url(r'^tasks/(?P<pk>\d+)/delete/$', delete_task),
    ##################################
)