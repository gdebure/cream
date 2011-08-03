from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from services.models import Domain, ServiceFamily, Service

urlpatterns = patterns('',
    ##################################
    # Domains 
    (r'^domains/$', ListView.as_view( queryset=Domain.objects.order_by('name'), context_object_name='domains_list', ), ),
    (r'^domains/(?P<pk>\d+)/$', DetailView.as_view( model=Domain, ), ),
    (r'^domains/create/$', CreateView.as_view( model=Domain, success_url='/services/domains/%(id)s' ), ),
    (r'^domains/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Domain, success_url='/services/domains/%(id)s' ), ),
    (r'^domains/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=Domain, success_url='/services/domains/' ), ),
    ##################################
    
    ##################################
    # Service Families 
    (r'^service_families/$', ListView.as_view( queryset=ServiceFamily.objects.order_by('name'), context_object_name='servicefamilies_list', ), ),
    (r'^service_families/(?P<pk>\d+)/$', DetailView.as_view( model=ServiceFamily, ), ),
    (r'^service_families/create/$', CreateView.as_view( model=ServiceFamily, success_url='/services/service_families/%(id)s' ), ),
    (r'^service_families/(?P<pk>\d+)/update/$', UpdateView.as_view( model=ServiceFamily, success_url='/services/service_families/%(id)s' ), ),
    (r'^service_families/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=ServiceFamily, success_url='/services/service_families/' ), ),
    ##################################
    
    ##################################
    # Services
    (r'^services/$', ListView.as_view( queryset=Service.objects.order_by('name'), context_object_name='services_list', ), ),
    (r'^services/(?P<pk>\d+)/$', DetailView.as_view( model=Service, ), ),
    (r'^services/create/$', CreateView.as_view( model=Service, success_url='/services/services/%(id)s' ), ),
    (r'^services/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Service, success_url='/services/services/%(id)s' ), ),
    (r'^services/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=Service, success_url='/services/services/' ), ),
    ##################################
    
)