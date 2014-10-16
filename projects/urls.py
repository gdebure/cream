from django.conf.urls import patterns,url
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from projects.models import Project, Deliverable, DeliverableVolume

from projects.views import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectCreateView, ProjectDeleteView, AddDeliverableView
from projects.views import DeliverableListView, DeliverableDetailView, DeliverableUpdateView, DeliverableCreateView, DeliverableDeleteView, AddDeliverableVolumeView

urlpatterns = patterns('',
    ##################################
    # Projects 
    url(r'^projects/$', ProjectListView.as_view(), name='projects_list'),
    url(r'^projects/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='project_detail'),
    url(r'^projects/create/$', ProjectCreateView.as_view(), name='create_project'),
    url(r'^projects/(?P<pk>\d+)/update/$', ProjectUpdateView.as_view(), name='update_project'),
    url(r'^projects/(?P<pk>\d+)/delete/$', ProjectDeleteView.as_view(), name='delete_project'),
    
    # Add deliverable to a project
    url(r'^projects/(?P<pk>\d+)/add_deliverable/$', AddDeliverableView.as_view(), name='add_deliverable'),
    ##################################
    
    
    ##################################
    # Deliverables
    url(r'^deliverables/$', DeliverableListView.as_view(), name='deliverables_list' ),
    url(r'^deliverables/(?P<pk>\d+)/$', DeliverableDetailView.as_view(), name='deliverable_detail'),
    url(r'^deliverables/create/$', DeliverableCreateView.as_view(), name='create_deliverable'),
    url(r'^deliverables/(?P<pk>\d+)/update/$', DeliverableUpdateView.as_view(), name='update_deliverable'),
    url(r'^deliverables/(?P<pk>\d+)/delete/$', DeliverableDeleteView.as_view(), name='delete_deliverable'),
    
    # Add volume to a deiverable
    url(r'^deliverables/(?P<pk>\d+)/add_volume/$', AddDeliverableVolumeView.as_view(), name='add_deliverablevolume'),
    ##################################
    
    
    ##################################
    # Deliverable Volumes
    url(r'^deliverablevolumes/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=DeliverableVolume, template_name='deliverablevolume_detail.html', )), name='deliverablevolume'),
    url(r'^deliverablevolumes/(?P<pk>\d+)/update/$', permission_required('projects.change_deliverablevolume')(UpdateView.as_view( model=DeliverableVolume, template_name='deliverablevolume_form.html' )), name='update_deliverablevolume'),
    #url(r'^deliverablevolumes/(?P<pk>\d+)/delete/$', permission_required('projects.delete_deliverablevolume')(DeleteDeliverableVolumeView.as_view()), name='delete_deliverablevolume'),
    ##################################

)