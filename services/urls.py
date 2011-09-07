from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, CreateView, DeleteView
from services.models import Domain, ServiceFamily, Service
from services.forms import DomainForm, ServiceFamilyForm, ServiceForm

from services.views import update_domain, delete_domain
from services.views import create_servicefamily,update_servicefamily, delete_servicefamily
from services.views import create_service, update_service, delete_service
from services.views import domains_report

urlpatterns = patterns('',
    ##################################
    # Domains 
    (r'^domains/$', login_required()(ListView.as_view( model=Domain, context_object_name='domains_list', )), ),
    (r'^domains/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Domain, )), ),
    (r'^domains/create/$', permission_required('services.add_domain')(CreateView.as_view( model=Domain, form_class=DomainForm, success_url='/services/domains/%(id)s' )), ),
    (r'^domains/(?P<pk>\d+)/update/$', update_domain ),
    (r'^domains/(?P<pk>\d+)/delete/$', delete_domain ),
    (r'^domains/(?P<pk>\d+)/add_servicefamily/$', create_servicefamily),
    ##################################
    
    ##################################
    # Service Families 
    (r'^service_families/$', login_required()(ListView.as_view( model=ServiceFamily, context_object_name='servicefamilies_list', )), ),
    (r'^service_families/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=ServiceFamily, )), ),
    (r'^service_families/create/$', permission_required('services.add_servicefamily')(CreateView.as_view( model=ServiceFamily, form_class=ServiceFamilyForm, success_url='/services/service_families/%(id)s' )), ),
    (r'^service_families/(?P<pk>\d+)/update/$', update_servicefamily ),
    (r'^service_families/(?P<pk>\d+)/delete/$', delete_servicefamily ),
    (r'^service_families/(?P<pk>\d+)/add_service/$', create_service),
    ##################################
    
    ##################################
    # Services
    (r'^services/$', login_required()(ListView.as_view( model=Service, context_object_name='services_list', )), ),
    (r'^services/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Service, )), ),
    (r'^services/create/$', permission_required('services.add_service')(CreateView.as_view( model=Service, form_class=ServiceForm, success_url='/services/services/%(id)s' )), ),
    (r'^services/(?P<pk>\d+)/update/$', update_service),
    (r'^services/(?P<pk>\d+)/delete/$', delete_service),
    
    ##################################
    
    (r'^report$',domains_report),
    
)