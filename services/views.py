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
        response += "Domain: " + str(domain) + "<br/>"
        families = domain.servicefamily_set.all()
        response += "Services Families: " + str(families.count())
        response += "<hr/>"
    
    return HttpResponse(response)
        
