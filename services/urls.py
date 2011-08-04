from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from services.models import Domain, ServiceFamily, Service

urlpatterns = patterns('',
    ##################################
    # Domains 
    (r'^domains/$', login_required()(ListView.as_view( queryset=Domain.objects.order_by('name'), context_object_name='domains_list', )), ),
    (r'^domains/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Domain, )), ),
    (r'^domains/create/$', permission_required('services.add_domain')(CreateView.as_view( model=Domain, success_url='/services/domains/%(id)s' )), ),
    (r'^domains/(?P<pk>\d+)/update/$', permission_required('services.change_domain')(UpdateView.as_view( model=Domain, success_url='/services/domains/%(id)s' )), ),
    (r'^domains/(?P<pk>\d+)/delete/$', permission_required('services.delete_domain')(DeleteView.as_view( model=Domain, success_url='/services/domains/' )), ),
    ##################################
    
    ##################################
    # Service Families 
    (r'^service_families/$', login_required()(ListView.as_view( queryset=ServiceFamily.objects.order_by('name'), context_object_name='servicefamilies_list', )), ),
    (r'^service_families/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=ServiceFamily, )), ),
    (r'^service_families/create/$', permission_required('services.add_servicefamily')(CreateView.as_view( model=ServiceFamily, success_url='/services/service_families/%(id)s' )), ),
    (r'^service_families/(?P<pk>\d+)/update/$', permission_required('services.change_servicefamily')(UpdateView.as_view( model=ServiceFamily, success_url='/services/service_families/%(id)s' )), ),
    (r'^service_families/(?P<pk>\d+)/delete/$', permission_required('services.delete_servicefamily')(DeleteView.as_view( model=ServiceFamily, success_url='/services/service_families/' )), ),
    ##################################
    
    ##################################
    # Services
    (r'^services/$', login_required()(ListView.as_view( queryset=Service.objects.order_by('name'), context_object_name='services_list', )), ),
    (r'^services/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Service, )), ),
    (r'^services/create/$', permission_required('services.add_service')(CreateView.as_view( model=Service, success_url='/services/services/%(id)s' )), ),
    (r'^services/(?P<pk>\d+)/update/$', permission_required('services.change_service')(UpdateView.as_view( model=Service, success_url='/services/services/%(id)s' )), ),
    (r'^services/(?P<pk>\d+)/delete/$', permission_required('services.delete_service')(DeleteView.as_view( model=Service, success_url='/services/services/' )), ),
    ##################################
    
)