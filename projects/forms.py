from django import forms
from django.core.mail import send_mail

from projects.models import Project, Deliverable, DeliverableVolume, Task

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('name','number','project_leader','date_start','date_end','department','natco','customer_name', 'customer_siglum','description','wiki_link')




class DeliverableForm(forms.ModelForm):
    
    class Meta:
        model = Deliverable
        fields = ('name', 'code', 'project',  'service', 'description', 'acceptance_criteria')
        
    def save(self, commit=True):
        '''On save, send a mail to the service owner'''
        deliverable = super(forms.ModelForm, self).save(commit=commit)
        
        if deliverable.approved_by_service_owner == 'P':
            mail_title = 'New deliverable added to service'
            mail_body = 'Please check whether the deliverable "' + str(deliverable)+ '" should be linked to the service "' + str(deliverable.service) + "\n"
            mail_body += 'Please Approve or Reject at this address : ' + deliverable.get_absolute_url()
            #send_mail(mail_title,mail_body,'creamrobot@cimpa.com',[deliverable.service.owner.user.email],fail_silently=False)
            
        return deliverable
        
        

class DeliverableFromProjectForm(DeliverableForm):
    
    predefined = 'project'
    
    class Meta:
        model = Deliverable
        fields = ('name', 'code', 'project',  'service', 'description', 'acceptance_criteria')
        
    

    
    
class DeliverableValidateServiceForm(forms.ModelForm):
    
    class Meta:
        model = Deliverable
        fields = ('approved_by_service_owner',)
        


        
class DeliverableVolumeForm(forms.ModelForm):
    
    class Meta:
        model = DeliverableVolume


        
class DeliverableVolumeFromDeliverableForm(DeliverableVolumeForm):
    
    predefined = 'deliverable'
        

        

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('name', 'open_date', 'criticity', 'description', 'requestor', 'creator', 'deliverable', 'subject')



class TaskFromDeliverableForm(TaskForm):
    
    predefined = 'deliverable'



class TaskAnswerForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('answer', 'close_date', 'status', 'reject_reason', 'time_spent', 'owner', 'number_of_units')
        
    
    
