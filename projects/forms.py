from django import forms
from projects.models import Deliverable

# Rework order of fields for deliverables
class DeliverableForm(forms.ModelForm):
    
    class Meta:
        model = Deliverable
        fields = ('project', 'name', 'code', 'description', 'acceptance_criteria', 'contractual_volume', 'unit_price')
        
class DeliverableValidateServiceForm(forms.ModelForm):
    
    class Meta:
        model = Deliverable
        fields = ('service','approved_by_service_owner')