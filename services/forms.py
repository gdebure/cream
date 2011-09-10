from services.models import Domain, ServiceFamily, Service
from django import forms

from guardian.shortcuts import assign, remove_perm, get_users_with_perms

class DomainForm(forms.ModelForm):
    
    class Meta:
        model = Domain
        fields = ['name','is_active','owner','description']
        
    def save(self, commit=True):
        domain = super(forms.ModelForm, self).save(commit=commit)
        
        # Remove existing rights on this domain
        users_with_perms = get_users_with_perms(domain)
        for user in users_with_perms:
            if user.has_perm('change_domain',domain):
                remove_perm('change_domain',user,domain)
            if user.has_perm('delete_domain',domain):
                remove_perm('delete_domain',user,domain)
        
        # Assign the right to update this domain to the domain owner
        if domain.owner != None:
            assign('domains.change_domain', domain.owner.user, domain)
            assign('domains.delete_domain', domain.owner.user, domain)
        
        return domain
        
        
      

class ServiceFamilyForm(forms.ModelForm):
    
    class Meta:
        model = ServiceFamily
        fields = ['name','is_active','owner','domain','description','growth_potential','service_position','trend','service_lifecycle']

    def save(self, commit=True):
        servicefamily = super(forms.ModelForm, self).save(commit=commit)
        
        # Remove existing rights on this servicefamily
        users_with_perms = get_users_with_perms(servicefamily)
        for user in users_with_perms:
            if user.has_perm('change_servicefamily',servicefamily):
                remove_perm('change_servicefamily',user,servicefamily)
            if user.has_perm('delete_servicefamily',servicefamily):
                remove_perm('delete_servicefamily',user,servicefamily)
        
        # Assign the right to update this servicefamily to the servicefamily focal point
        if servicefamily.owner != None:
            assign('servicefamily.change_servicefamily', servicefamily.owner.user, servicefamily)
            assign('servicefamily.delete_servicefamily', servicefamily.owner.user, servicefamily)
        
        return servicefamily


class ServiceFamilyFromDomainForm(ServiceFamilyForm):

    predefined = 'domain'
        
   
        


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name','is_active','owner','service_family','description']
        
    def save(self, commit=True):
        service = super(forms.ModelForm, self).save(commit=commit)
        
        # Remove existing rights on this service
        users_with_perms = get_users_with_perms(service)
        for user in users_with_perms:
            if user.has_perm('change_service',service):
                remove_perm('change_service',user,service)
            if user.has_perm('delete_service',service):
                remove_perm('delete_service',user,service)
        
        # Assign the right to update this service to the service focal point
        if service.owner != None:
            assign('service.change_service', service.owner.user, service)
            assign('service.delete_service', service.owner.user, service)
        
        return service
        
class ServiceFromServiceFamilyForm(ServiceForm):

    predefined = 'service_family'