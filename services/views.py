from django.db.models import ProtectedError
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.create_update import create_object, update_object, delete_object
from django.views.generic.simple import direct_to_template

from services.models import Domain, ServiceFamily, Service
from services.forms import DomainForm, ServiceFamilyForm, ServiceFamilyFromDomainForm, ServiceForm, ServiceFromServiceFamilyForm

import reversion


def update_domain(request, pk):
    '''Perform update on the domain'''
    
    domain = get_object_or_404(Domain, id=pk)
    
    # Can only update if the current user has rights on the project
    if request.user.has_perm('services.change_domain',domain):
        response = update_object(request, form_class=DomainForm, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response
    
    


def delete_domain(request, pk):
    '''Perform the domain delete'''
    
    domain = get_object_or_404(Domain, id=pk)
     
    # It is only possible if the user has rights on the project
    if request.user.has_perm('services.delete_domain',domain):
        try:
            response = delete_object(request, Domain, '/services/domains', object_id=pk, template_object_name="domain")
        except ProtectedError:
            message = 'You can not delete domain <a href="' + domain.get_absolute_url() +'">' + str(domain) + '</a> because there are Service Families attached to it'
            response = direct_to_template(request, template="common/error.html", extra_context={'message':message})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response


    
def create_servicefamily(request, pk):
    '''Create a deliverable from a project page'''
    
    domain = get_object_or_404(Domain, id=pk)
     
    # It is only possible if the user has rights on the project
    if request.user.has_perm('services.change_domain',domain):
        response = create_object(request, form_class=ServiceFamilyFromDomainForm, extra_context={'predefined_value':domain})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response


def update_servicefamily(request, pk):
    '''Perform update on the servicefamily'''
    
    servicefamily = get_object_or_404(ServiceFamily, id=pk)
    
    # Can only update if the current user has rights on the servicefamily or on the domain
    if request.user.has_perm('services.change_servicefamily',servicefamily) or request.user.has_perm('services.change_domain', servicefamily.domain):
        response = update_object(request, form_class=ServiceFamilyForm, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response
    
    


def delete_servicefamily(request, pk):
    '''Perform the domain delete'''
    
    servicefamily = get_object_or_404(ServiceFamily, id=pk)
     
    # It is only possible if the user has rights on the servicefamily or on the domain
    if request.user.has_perm('services.delete_servicefamily',servicefamily) or request.user.has_perm('services.change_domain',servicefamily.domain):
        try:
            response = delete_object(request, ServiceFamily, '/services/service_families', object_id=pk, template_object_name="servicefamily")
        except ProtectedError:
            message = 'You can not delete Service Family <a href="' + servicefamily.get_absolute_url() +'">' + str(servicefamily) + '</a> because there are Services attached to it'
            response = direct_to_template(request, template="common/error.html", extra_context={'message':message})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response


def create_service(request, pk):
    '''Create a deliverable from a project page'''
    
    servicefamily = get_object_or_404(ServiceFamily, id=pk)
     
    # It is only possible if the user has rights on the project
    if request.user.has_perm('services.change_servicefamily',servicefamily):
        response = create_object(request, form_class=ServiceFromServiceFamilyForm, extra_context={'predefined_value':servicefamily})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response

    
    

def update_service(request, pk):
    '''Perform update on the service'''
    
    service = get_object_or_404(Service, id=pk)
    
    # Can only update if the current user has rights on the service or on the servicefamily
    if request.user.has_perm('services.change_service',service) or request.user.has_perm('services.change_servicefamily', service.service_family):
        response = update_object(request, form_class=ServiceForm, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response
    
    


def delete_service(request, pk):
    '''Perform the domain delete'''
    
    service = get_object_or_404(Service, id=pk)
     
    # It is only possible if the user has rights on the service or on the domain
    if request.user.has_perm('services.delete_service',service) or request.user.has_perm('services.change_servicefamily', service.service_family):
        try:
            response = delete_object(request, Service, '/services/services', object_id=pk, template_object_name="service")
        except ProtectedError:
            message = 'You can not delete Service <a href="' + service.get_absolute_url() +'">' + str(service) + '</a> because there are Deliverables attached to it'
            response = direct_to_template(request, template="common/error.html", extra_context={'message':message})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response



def show_history(request):
    
    # Build list of deleted items
    deleted_domains = reversion.get_deleted(Domain)
    
    response = direct_to_template(request, template="services/deleted_domains.html")
    return response
    

        
def domains_report(request):
    
    domain_list = Domain.objects.all()
    total_turnover = 0
    for domain in domain_list:
        total_turnover += domain.get_turnover()
    response = direct_to_template(request, template="services/domains_report.html", extra_context={'domain_list':domain_list,'total_turnover':total_turnover})
    return response


def domain_report(request,pk):
    
    domain = get_object_or_404(Domain, id=pk)
    total_turnover = 0
    for service_family in domain.get_service_families():
        total_turnover += service_family.get_turnover()
    response = direct_to_template(request, template="services/domain_report.html", extra_context={'domain':domain,'total_turnover':total_turnover})
    return response    


def servicefamilies_report(request):
    
    servicefamilies_list = ServiceFamily.objects.all()
    total_turnover = 0
    for service_family in servicefamilies_list:
        total_turnover += service_family.get_turnover()
    response = direct_to_template(request, template="services/servicefamilies_report.html", extra_context={'servicefamilies_list':servicefamilies_list,'total_turnover':total_turnover})
    return response 

    
def servicefamily_report(request,pk):
    
    service_family = get_object_or_404(ServiceFamily, id=pk)
    total_turnover = 0
    for service in service_family.get_services():
        total_turnover += service.get_turnover()
    response = direct_to_template(request, template="services/servicefamily_report.html", extra_context={'service_family':service_family,'total_turnover':total_turnover})
    return response 
    

def services_report(request):
    
    services_list = Service.objects.all()
    total_turnover = 0
    for service in services_list:
        total_turnover += service.get_turnover()
    response = direct_to_template(request, template="services/services_report.html", extra_context={'services_list':services_list,'total_turnover':total_turnover})
    return response
    
    
def service_report(request,pk):
    
    service = get_object_or_404(Service, id=pk)
    total_turnover = 0
    for deliverable in service.get_deliverables():
        total_turnover += deliverable.get_turnover()
    response = direct_to_template(request, template="services/service_report.html", extra_context={'service':service,'total_turnover':total_turnover})
    return response