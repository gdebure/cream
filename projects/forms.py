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
        
        
        return project




class DeliverableForm(forms.ModelForm):
    
    class Meta:
        model = Deliverable
        fields = ('name', 'code', 'project',  'service', 'description', 'acceptance_criteria')
        
   
        

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
    

class TaskFromProjectForm(TaskForm):
    
    predefined = 'project'
    project = forms.CharField()
    
    class Meta:
        model = Task
        fields = ('name', 'open_date', 'criticity', 'description', 'requestor', 'creator', 'project', 'deliverable', 'subject')
    
    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project')
        super(TaskFromProjectForm, self).__init__(*args, **kwargs)
        deliverable = forms.ChoiceField(choices=project.deliverable_set.all())

class TaskAnswerForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('status', 'answer', 'close_date', 'reject_reason', 'time_spent', 'owner', 'number_of_units')
        
    
    
