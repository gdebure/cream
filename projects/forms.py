from django import forms
from projects.models import Project, Deliverable, Task

class ProjectForm(forms.ModelForm):
    
    date_start = forms.DateField(help_text='YYYY-MM-DD')
    date_end = forms.DateField(help_text='YYYY-MM-DD')
    
    class Meta:
        model = Project



class DeliverableForm(forms.ModelForm):
    
    class Meta:
        model = Deliverable
        fields = ('project', 'name', 'service', 'code', 'description', 'acceptance_criteria', 'contractual_volume', 'unit_price')
        
    def save(self, commit=True):
        deliverable = super(forms.ModelForm, self).save(commit=commit)
        if deliverable.approved_by_service_owner == 'P':
            pass
            #send_mail('New deliverable added to service', 'Here is the message.', 'from@example.com',['to@example.com'], fail_silently=False)
        


class DeliverableValidateServiceForm(forms.ModelForm):
    
    class Meta:
        model = Deliverable
        fields = ('approved_by_service_owner',)
        
        
class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task