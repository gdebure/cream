from django.conf.urls import patterns,url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from projects.models import Project, Deliverable, DeliverableVolume

from projects.views import AddDeliverableView, DeleteDeliverableView, AddDeliverableVolumeView, DeleteDeliverableVolumeView

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
    ##################################
    
    
    ##################################
    # Deliverables
    url(r'^deliverables/$', login_required()(ListView.as_view( model=Deliverable, context_object_name='deliverables_list', template_name='deliverable_list.html' )), name='deliverables_list' ),
    url(r'^deliverables/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Deliverable, template_name='deliverable_detail.html' )), name='deliverable'),
    url(r'^deliverables/create/$', permission_required('projects.add_deliverable')(CreateView.as_view( model=Deliverable, template_name='deliverable_form.html' )), name='create_deliverable'),
    url(r'^deliverables/(?P<pk>\d+)/update/$', permission_required('projects.change_deliverable')(UpdateView.as_view( model=Deliverable, template_name='deliverable_form.html' )), name='update_deliverable'),
    url(r'^deliverables/(?P<pk>\d+)/delete/$', permission_required('projects.delete_deliverable')(DeleteDeliverableView.as_view()), name='delete_deliverable'),
    
    # Add volume to a deiverable
    url(r'^deliverables/(?P<pk>\d+)/add_volume/$', permission_required('projects.change_deliverable')(AddDeliverableVolumeView.as_view( model=DeliverableVolume, template_name='deliverablevolume_form.html' )), name='add_deliverablevolume'),
    ##################################
    
    
    ##################################
    # Deliverable Volumes
    url(r'^deliverablevolumes/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=DeliverableVolume, template_name='deliverablevolume_detail.html', )), name='deliverablevolume'),
    url(r'^deliverablevolumes/(?P<pk>\d+)/update/$', permission_required('projects.change_deliverablevolume')(UpdateView.as_view( model=DeliverableVolume, template_name='deliverablevolume_form.html' )), name='update_deliverablevolume'),
    url(r'^deliverablevolumes/(?P<pk>\d+)/delete/$', permission_required('projects.delete_deliverablevolume')(DeleteDeliverableVolumeView.as_view()), name='delete_deliverablevolume'),
    ##################################

)