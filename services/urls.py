from django.conf.urls import url, patterns
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from services.models import Domain, ServiceFamily, Service
from services.forms import DomainForm, ServiceFamilyForm, ServiceForm

from services.views import ServiceView, AddServiceFamilyView, AddServiceView

urlpatterns = patterns('',
    ##################################
    # Domains 
    url(r'^domains/$', login_required()(ListView.as_view( model=Domain, context_object_name='domains_list',template_name='domain_list.html')), name='domains_list' ),
    url(r'^domains/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Domain, template_name='domain_detail.html')), name='domain' ),
    url(r'^domains/create/$', permission_required('services.add_domain')(CreateView.as_view( model = Domain, template_name='domain_form.html')), name='create_domain'),
    url(r'^domains/(?P<pk>\d+)/update/$', permission_required('services.change_domain')(UpdateView.as_view( model = Domain, template_name='domain_form.html')), name='update_domain'),
    url(r'^domains/(?P<pk>\d+)/delete/$', permission_required('services.delete_domain')(DeleteView.as_view( model = Domain, template_name='domain_confirm_delete.html', success_url=reverse_lazy('domains_list') )), name='delete_domain'),
    url(r'^domains/(?P<pk>\d+)/add_servicefamily/$', permission_required('services.change_domain')(AddServiceFamilyView.as_view( model=ServiceFamily, template_name='servicefamily_form.html' )), name='add_servicefamily'),
    ##url(r'^domains/deleted',show_history),
    ##################################
    
    ##################################
    # Service Families 
    url(r'^service_families/$', login_required()(ListView.as_view( model=ServiceFamily, context_object_name='servicefamilies_list', template_name='servicefamily_list.html' )), name='servicefamilies_list'),
    url(r'^service_families/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=ServiceFamily, template_name='servicefamily_detail.html' )), name='servicefamily' ),
    url(r'^service_families/create/$', permission_required('services.add_servicefamily')(CreateView.as_view( model=ServiceFamily, template_name='servicefamily_form.html' )), name='create_servicefamily'),
    url(r'^service_families/(?P<pk>\d+)/update/$', permission_required('services.change_servicefamily')(UpdateView.as_view( model = ServiceFamily, template_name='servicefamily_form.html' )), name='update_servicefamily' ),
    url(r'^service_families/(?P<pk>\d+)/delete/$', permission_required('services.delete_servicefamily')(DeleteView.as_view( model = ServiceFamily, template_name='servicefamily_confirm_delete.html', success_url=reverse_lazy('servicefamilies_list') )), name='delete_servicefamily' ),
    url(r'^service_families/(?P<pk>\d+)/add_service/$', permission_required('services.change_servicefamily')(AddServiceView.as_view( model = Service, template_name='service_form.html' )), name='add_service'),
    ##################################
    
    ##################################
    # Services
    url(r'^services/$', login_required()(ListView.as_view( model=Service, context_object_name='services_list', template_name='service_list.html')), name='services_list'),
    url(r'^services/(?P<pk>\d+)/$', login_required()(ServiceView.as_view()), name='service' ),
    url(r'^services/create/$', permission_required('services.add_service')(CreateView.as_view( model=Service, template_name='service_form.html' )), name='create_service'),
    url(r'^services/(?P<pk>\d+)/update/$', permission_required('services.change_service')(UpdateView.as_view( model=Service, template_name='service_form.html' )), name='update_service'),
    url(r'^services/(?P<pk>\d+)/delete/$', permission_required('services.delete_service')(DeleteView.as_view( model=Service, template_name='service_confirm_delete.html' )), name='delete_service'),
    ##################################
    # Reports
    #url(r'^reports/$',domains_report),
    #url(r'^reports/domains/$',domains_report),
    #url(r'^reports/domains/(?P<pk>\d+)/$',domain_report),
    #url(r'^reports/service_families/$',servicefamilies_report),
    #url(r'^reports/service_families/(?P<pk>\d+)/$',servicefamily_report),
    #url(r'^reports/services/$',services_report),
    #url(r'^reports/services/(?P<pk>\d+)/$',service_report),
    ##################################
)