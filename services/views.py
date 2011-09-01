from django.views.generic import UpdateView
from guardian.decorators import permission_required
from django.utils.decorators import method_decorator

from services.models import Domain, ServiceFamily, Service

from django.http import HttpResponse

class DomainUpdateView(UpdateView):

    @method_decorator(permission_required('services.change_domain',(Domain, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(DomainUpdateView, self).dispatch(*args, **kwargs)

class ServiceFamilyUpdateView(UpdateView):

    @method_decorator(permission_required('services.change_servicefamily',(ServiceFamily, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(ServiceFamilyUpdateView, self).dispatch(*args, **kwargs)

class ServiceUpdateView(UpdateView):

    @method_decorator(permission_required('services.change_service',(Service, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(ServiceUpdateView, self).dispatch(*args, **kwargs)

#class AddServiceFamilyView(UpdateView):

    #@method_decorator(permission_required('services.create_domain',(Domain, 'id', 'pk')))
    #def dispatch(self, *args, **kwargs):
        #return super(ServiceFamilyUpdateView, self).dispatch(*args, **kwargs)
        
        
        
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
        

