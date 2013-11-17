from django.views.generic import DetailView, CreateView

from services.models import Domain, ServiceFamily, Service

class AddServiceFamilyView(CreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddServiceFamilyView,self).get_context_data(**kwargs)
        domain = Domain.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'domain':domain}
        return  context
    
class ServiceView(DetailView):
    
    model = Service
    template_name='service_detail.html'
    
    
class AddServiceView(CreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddServiceView,self).get_context_data(**kwargs)
        service_family = ServiceFamily.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'service_family':service_family}
        return  context