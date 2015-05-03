from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from services.models import Domain, ServiceFamily, Service



class DomainListView(ListView,LoginRequiredMixin):
    
    model = Domain
    context_object_name = 'domains_list'
    template_name = 'domain_list.html'


class DomainDetailView(DetailView,LoginRequiredMixin):
    
    model = Domain
    template_name = 'domain_detail.html'
    
    
class DomainCreateView(CreateView,PermissionRequiredMixin):
    
    model = Domain
    template_name = 'domain_form.html'
    permission = 'services.add_domain'
    fields=['name','is_active','owner','description']
    
    def get_success_url(self):
        return reverse_lazy('domain',args=[self.object.id])

    
class DomainUpdateView(UpdateView,PermissionRequiredMixin):
    
    model = Domain
    template_name = 'domain_form.html'
    permission = 'services.change_domain'
    fields=['name','is_active','owner','description']
    
    def get_success_url(self):
        return reverse_lazy('domain',args=[self.object.id])


class DomainDeleteView(DeleteView,PermissionRequiredMixin):
    
    model = Domain
    success_url = reverse_lazy('domains_list')
    template_name = 'domain_confirm_delete.html'
    permission = 'services.delete_domain'




    

class ServiceFamilyListView(ListView,LoginRequiredMixin):
    
    model = ServiceFamily
    context_object_name = 'servicefamilies_list'
    template_name = 'servicefamily_list.html'


class ServiceFamilyDetailView(DetailView,LoginRequiredMixin):
    
    model = ServiceFamily
    template_name = 'servicefamily_detail.html'

    
class ServiceFamilyCreateView(CreateView,PermissionRequiredMixin):
    
    model = ServiceFamily
    template_name = 'servicefamily_form.html'
    permission = 'services.add_servicefamily'
    fields=['name','domain','is_active','owner','description']
    
    def get_success_url(self):
        return reverse_lazy('servicefamily',args=[self.object.id])


class AddServiceFamilyView(ServiceFamilyCreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddServiceFamilyView,self).get_context_data(**kwargs)
        domain = Domain.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'domain':domain}
        return  context


class ServiceFamilyUpdateView(UpdateView,PermissionRequiredMixin):
    
    model = ServiceFamily
    template_name = 'servicefamily_form.html'
    permission = 'services.change_servicefamily'
    fields=['name','domain','is_active','owner','description']
    
    def get_success_url(self):
        return reverse_lazy('servicefamily',args=[self.object.id])
    
    
class ServiceFamilyDeleteView(DeleteView,PermissionRequiredMixin):
    
    model = ServiceFamily
    template_name = 'servicefamily_confirm_delete.html'
    success_url = reverse_lazy('servicefamilies_list')
    permission = 'services.delete_servicefamily'
    



class ServiceListView(ListView, LoginRequiredMixin):
    
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services_list'


class ServiceDetailView(DetailView, LoginRequiredMixin):
    
    model = Service
    template_name = 'service_detail.html'


class ServiceCreateView(CreateView, PermissionRequiredMixin):
    
    model = Service
    template_name = 'service_form.html'
    permission = 'services.add_service'
    fields=['name','service_family','is_active','owner','description']
    
    def get_success_url(self):
        return reverse_lazy('service',args=[self.object.id])
    
    
class AddServiceView(ServiceCreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddServiceView,self).get_context_data(**kwargs)
        service_family = ServiceFamily.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'service_family':service_family}
        return  context
    
class ServiceUpdateView(UpdateView,PermissionRequiredMixin):
    
    model = Service
    template_name = 'service_form.html'
    permission = 'services.change_service'
    fields=['name','service_family','is_active','owner','description']
    
    def get_success_url(self):
        return reverse_lazy('service',args=[self.object.id])
    

class ServiceDeleteView(DeleteView,PermissionRequiredMixin):
    
    model = Service
    template_name = 'service_confirm_delete.html'
    permission = 'services.delete_service'
    success_url = reverse_lazy('services_list')
    