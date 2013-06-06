from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required, login_required

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from services.models import Domain, ServiceFamily, Service
from services.forms import DomainForm, ServiceFamilyForm, ServiceForm

from services.views import AddServiceFamilyView, AddServiceView

urlpatterns = patterns('',
    ##################################
    # Domains 
    (r'^domains/$', login_required()(ListView.as_view( model=Domain, context_object_name='domains_list', )), ),
    (r'^domains/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Domain, )), ),
    (r'^domains/create/$', permission_required('services.add_domain')(CreateView.as_view( model = Domain))),
    (r'^domains/(?P<pk>\d+)/update/$', permission_required('services.change_domain')(UpdateView.as_view( model = Domain))),
    (r'^domains/(?P<pk>\d+)/delete/$', permission_required('services.delete_domain')(DeleteView.as_view( model = Domain ))),
    (r'^domains/(?P<pk>\d+)/add_servicefamily/$', permission_required('services.change_domain')(AddServiceFamilyView.as_view( model=ServiceFamily ))),
    ##(r'^domains/deleted',show_history),
    ##################################
    
    ##################################
    # Service Families 
    (r'^service_families/$', login_required()(ListView.as_view( model=ServiceFamily, context_object_name='servicefamilies_list', )), ),
    (r'^service_families/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=ServiceFamily, )), ),
    (r'^service_families/create/$', permission_required('services.add_servicefamily')(CreateView.as_view( model=ServiceFamily )), ),
    (r'^service_families/(?P<pk>\d+)/update/$', permission_required('services.change_servicefamily')(UpdateView.as_view( model = ServiceFamily )) ),
    (r'^service_families/(?P<pk>\d+)/delete/$', permission_required('services.delete_servicefamily')(DeleteView.as_view( model = ServiceFamily )) ),
    (r'^service_families/(?P<pk>\d+)/add_service/$', permission_required('services.change_servicefamily')(AddServiceView.as_view( model = Service ))),
    ##################################
    
    ##################################
    # Services
    (r'^services/$', login_required()(ListView.as_view( model=Service, context_object_name='services_list', )), ),
    (r'^services/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Service, )), ),
    (r'^services/create/$', permission_required('services.add_service')(CreateView.as_view( model=Service )), ),
    (r'^services/(?P<pk>\d+)/update/$', permission_required('services.change_service')(UpdateView.as_view( model=Service ))),
    (r'^services/(?P<pk>\d+)/delete/$', permission_required('services.delete_service')(DeleteView.as_view( model=Service ))),
    ##################################
    # Reports
    #(r'^reports/$',domains_report),
    #(r'^reports/domains/$',domains_report),
    #(r'^reports/domains/(?P<pk>\d+)/$',domain_report),
    #(r'^reports/service_families/$',servicefamilies_report),
    #(r'^reports/service_families/(?P<pk>\d+)/$',servicefamily_report),
    #(r'^reports/services/$',services_report),
    #(r'^reports/services/(?P<pk>\d+)/$',service_report),
    ##################################
)