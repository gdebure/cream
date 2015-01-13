from django.conf.urls import url, patterns
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from services.models import Domain, ServiceFamily, Service
from services.forms import DomainForm, ServiceFamilyForm, ServiceForm

from services.views import DomainListView, DomainDetailView, DomainCreateView, DomainUpdateView, DomainDeleteView
from services.views import ServiceFamilyListView, ServiceFamilyDetailView, ServiceFamilyCreateView, AddServiceFamilyView, ServiceFamilyUpdateView, ServiceFamilyDeleteView
from services.views import ServiceListView, ServiceDetailView, ServiceCreateView, AddServiceView, ServiceUpdateView, ServiceDeleteView

urlpatterns = patterns('',
    ##################################
    # Domains 
    url(r'^domains/$', DomainListView.as_view(), name='domains_list'),
    url(r'^domains/(?P<pk>\d+)/$', DomainDetailView.as_view(), name='domain' ),
    url(r'^domains/create/$', DomainCreateView.as_view(), name='create_domain'),
    url(r'^domains/(?P<pk>\d+)/update/$', DomainUpdateView.as_view(), name='update_domain'),
    url(r'^domains/(?P<pk>\d+)/delete/$', DomainDeleteView.as_view(), name='delete_domain'),
    url(r'^domains/(?P<pk>\d+)/add_servicefamily/$', AddServiceFamilyView.as_view(), name='add_servicefamily'),
    ##url(r'^domains/deleted',show_history),
    ##################################
    
    ##################################
    # Service Families 
    url(r'^service_families/$', ServiceFamilyListView.as_view(), name='servicefamilies_list'),
    url(r'^service_families/(?P<pk>\d+)/$', ServiceFamilyDetailView.as_view(), name='servicefamily' ),
    url(r'^service_families/create/$', ServiceFamilyCreateView.as_view(), name='create_servicefamily'),
    url(r'^service_families/(?P<pk>\d+)/update/$',ServiceFamilyUpdateView.as_view() , name='update_servicefamily' ),
    url(r'^service_families/(?P<pk>\d+)/delete/$', ServiceFamilyDeleteView.as_view(), name='delete_servicefamily' ),
    url(r'^service_families/(?P<pk>\d+)/add_service/$', AddServiceView.as_view(), name='add_service'),
    ##################################
    
    ##################################
    # Services
    url(r'^services/$', ServiceListView.as_view(), name='services_list'),
    url(r'^services/(?P<pk>\d+)/$', ServiceDetailView.as_view(), name='service' ),
    url(r'^services/create/$',ServiceCreateView.as_view() , name='create_service'),
    url(r'^services/(?P<pk>\d+)/update/$', ServiceUpdateView.as_view(), name='update_service'),
    url(r'^services/(?P<pk>\d+)/delete/$', ServiceDeleteView.as_view(), name='delete_service'),
    ##################################
    
)