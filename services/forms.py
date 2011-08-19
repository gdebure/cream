from services.models import Domain, ServiceFamily, Service
from django import forms

from guardian.shortcuts import assign, remove_perm, get_users_with_perms

class DomainForm(forms.ModelForm):
    
    class Meta:
        model = Domain
        
    def save(self, commit=True):
        domain = super(forms.ModelForm, self).save(commit=commit)
        
        # Remove existing rights on this domain
        users_with_perms = get_users_with_perms(domain)
        for user in users_with_perms:
            remove_perms('update_domain',user,domain)
        
        # Assign the right to update this domain to the domain owner
        assign('domains.update_domain', domain.owner.user, domain)
        
        return domain
        
        
        
       

class ServiceFamilyForm(forms.ModelForm):
    
    class Meta:
        model = ServiceFamily
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service