from django.views.generic import UpdateView
from guardian.decorators import permission_required
from django.utils.decorators import method_decorator

from services.models import Domain, ServiceFamily, Service

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
        
        
