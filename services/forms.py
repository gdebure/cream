from django import forms

from services.models import Domain

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        
class ServiceFamilyForm(forms.ModelForm):
    class Meta:
        model = ServiceFamily
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service