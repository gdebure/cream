from django.db.models import ProtectedError

from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.create_update import create_object, update_object, delete_object
from django.views.generic.simple import direct_to_template

from services.models import Domain, ServiceFamily, Service
from services.forms import DomainForm, ServiceFamilyForm, ServiceFamilyFromDomainForm, ServiceForm, ServiceFromServiceFamilyForm



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


        
def domains_report(request):
    
    domains = Domain.objects.all()
    response = "<h1>Domain Reporting</h1><hr/>"
    
    for domain in domains:
        domain_turnover = 0
        response += "Domain: " + str(domain) + "<br/>"
        families = domain.servicefamily_set.all()
    
        for family in families:
            family_turnover = 0
            response += "Service Family: " + str(family) + "<br/>"
            services = family.service_set.all()
            
            for service in services:
                service_turnover = 0
                response += "Service: " + str(service) + "<br/>"
                deliverables = service.deliverable_set.all()
                
                for deliverable in deliverables:
                    deliverable_turnover = 0
                    if deliverable.contractual_volume != None and deliverable.unit_price != None:
                        deliverable_turnover = deliverable.contractual_volume * deliverable.unit_price
                        response += "Deliverable: " + str(deliverable) + " = " + str(deliverable_turnover) + "<br/>"
                    service_turnover += deliverable_turnover
                
                response += "Service Total = " + str(service_turnover) + "</br>"
                family_turnover += service_turnover
            
            response += "Family Total = " + str(family_turnover) + "</br>"
            domain_turnover += family_turnover
        
        response += "Domain Total = " + str(domain_turnover) + "</br>"
                
    
    return HttpResponse(response)
        

