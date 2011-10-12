from django import forms
from django.core.mail import send_mail

from projects.models import Project, Deliverable, DeliverableVolume, Task

from guardian.shortcuts import assign, remove_perm, get_users_with_perms


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('name','number','project_leader','date_start','date_end','department','natco','customer_name', 'customer_siglum','description','wiki_link')
        
    def save(self, commit=True):
        project = super(forms.ModelForm, self).save(commit=commit)
        
        
        # Remove existing rights on this project
        users_with_perms = get_users_with_perms(project)
        for user in users_with_perms:
            if user.has_perm('change_project',project):
                remove_perm('change_project',user,project)
            if user.has_perm('delete_project',project):
                remove_perm('delete_project',user,project)
        
        # Assign the right to update this project to the project owner
        if project.project_leader != None:
            assign('projects.change_project', project.project_leader.user, project)
            assign('projects.delete_project', project.project_leader.user, project)
        
        
        mail_title = 'Project Updated: ' + str(project)
        mail_body = 'This project has been updated "' + str(project)+ ' by XXXXX \n'
        mail_body += project.get_absolute_url()
            
        # FIXME: Use the catalog admin group to get email adresses
        send_mail(mail_title,mail_body,'creamrobot@cimpa.com',['christian.scholz@airbus.com'],fail_silently=False)
        
        return project




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
            send_mail(mail_title,mail_body,'creamrobot@cimpa.com',[deliverable.service.owner.user.email,'christian.scholz@airbus.com'],fail_silently=False)
            
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
        
        
    def save(self, commit=True):
        deliverable = super(forms.ModelForm, self).save(commit=commit)
        
        mail_title = 'Deliverable ' + str(deliverable) + ' linked to service ' + str(deliverable.service)
        mail_body = 'The deliverable ' + str(deliverable)+ ' link to the service ' + str(deliverable.service) + ' has been approved by XXXX \n'
        mail_body += deliverable.get_absolute_url()
            
        # FIXME: Use the catalog admin group to get email adresses
        send_mail(mail_title,mail_body,'creamrobot@cimpa.com',['christian.scholz@airbus.com'],fail_silently=False)
        
        return deliverable


        
class DeliverableVolumeForm(forms.ModelForm):
    
    class Meta:
        model = DeliverableVolume
        
    def save(self, commit=True):
        volume = super(forms.ModelForm, self).save(commit=commit)
        
        mail_title = 'Deliverable Volume updated ' + str(volume.deliverable)
        mail_body = 'The Deliverable Volume for deliverable ' + str(volume.deliverable)+ ' has been updated by XXXX \n'
        mail_body += volume.get_absolute_url()
            
        # FIXME: Use the catalog admin group to get email adresses
        send_mail(mail_title,mail_body,'creamrobot@cimpa.com',['christian.scholz@airbus.com'],fail_silently=False)
        
        return volume


        
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
        
    
    
