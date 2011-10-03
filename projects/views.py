from django.db.models import ProtectedError

from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.create_update import create_object, update_object, delete_object
from django.views.generic.simple import direct_to_template

from projects.models import Project, Authorization, Deliverable, DeliverableVolume, Task

from projects.forms import ProjectForm
from projects.forms import DeliverableForm, DeliverableFromProjectForm, DeliverableValidateServiceForm
from projects.forms import DeliverableVolumeFromDeliverableForm
from projects.forms import TaskForm



def update_project(request, pk):
    '''Perform update on the project'''
    
    project = get_object_or_404(Project, id=pk)
    
    # Can only update if the current user has rights on the project
    if request.user.has_perm('projects.change_project',project):
        response = update_object(request, form_class=ProjectForm, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response
    
    


def delete_project(request, pk):
    '''Perform the project delete'''
    
    project = get_object_or_404(Project, id=pk)
     
    # It is only possible if the user has rights on the project
    if request.user.has_perm('projects.delete_project',project):
        try:
            response = delete_object(request, Project, '/projects/projects', object_id=pk, template_object_name="project")
        except ProtectedError:
            message = 'You can not delete project <a href="' + project.get_absolute_url() +'">' + str(project) + '</a> because there are Deliverable or Tasks attached to it'
            response = direct_to_template(request, template="common/error.html", extra_context={'message':message})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response





def update_authorization(request, pk):
    '''Perform update on the authorization'''
    
    authorization = get_object_or_404(Deliverable, id=pk)
    
    # Can only update if the current user has enough rights:
    # - has specifically the permission change_authorization
    # - or has the right to change the project this authorization belongs to
    if request.user.has_perm('projects.change_authorization',authorization) or request.user.has_perm('projects.change_project',authorization.project):
        response = update_object(request, model=Authorization, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response





def delete_authorization(request, pk):
    '''Perform the project authorization'''
    
    authorization = get_object_or_404(Authorization, id=pk)
     
    # It is only possible if the user has rights on the project
    if request.user.has_perm('projects.change_authorization',authorization) or request.user.has_perm('projects.change_project',authorization.project):
        response = delete_object(request, Authorization, authorization.project.get_absolute_url(), object_id=pk, template_object_name="authorization")
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response




def create_deliverable(request, pk):
    '''Create a deliverable from a project page'''
    
    project = get_object_or_404(Project, id=pk)
     
    # It is only possible if the user has rights on the project
    if request.user.has_perm('projects.change_project',project):
        response = create_object(request, form_class=DeliverableFromProjectForm, extra_context={'predefined_value':project})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response




def update_deliverable(request, pk):
    '''Perform update on the deliverable'''
    
    deliverable = get_object_or_404(Deliverable, id=pk)
    
    # Can only update if the current user has enough rights:
    # - has specifically the permission change_deliverable
    # - or has the right to change the project this deliverable belongs to
    if request.user.has_perm('projects.change_deliverable',deliverable) or request.user.has_perm('projects.change_project',deliverable.project):
        response = update_object(request,form_class=DeliverableForm, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response

    



def validate_deliverable_service(request, pk):
    '''Perform the validation of the link to the service'''
    
    deliverable = get_object_or_404(Deliverable, id=pk)
    
    # It is only possible if the user has rights on the service
    if request.user.has_perm('services.change_service',deliverable.service):
        response = update_object(request,form_class=DeliverableValidateServiceForm, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response





def delete_deliverable(request, pk):
    '''Perform the deliverable delete'''
    
    deliverable = get_object_or_404(Deliverable, id=pk)
    project = deliverable.project
    
    # It is only possible if the user has rights on the deliverable
    if request.user.has_perm('projects.delete_deliverable',deliverable):
        try:
            response = delete_object(request, Deliverable, project.get_absolute_url(), object_id=pk, template_object_name="deliverable")
        except ProtectedError:
            message = 'You can not delete deliverable <a href="' + deliverable.get_absolute_url() +'">' + str(deliverable) + '</a> because there are Tasks attached to it'
            response = direct_to_template(request, template="common/error.html", extra_context={'message':message})
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response
    



def create_deliverablevolume(request, pk):
    
    deliverable = get_object_or_404(Deliverable, id=pk)
    project = deliverable.project
    
    if request.user.has_perm('projects.add_deliverablevolume') or request.user.has_perm('projects.change_project',project):
        response = create_object(request, form_class=DeliverableVolumeFromDeliverableForm, extra_context={'predefined_value':deliverable})
    else:
        response = direct_to_template(request, template="forbidden.html")
    
    return response
    

def update_deliverablevolume(request, pk):
    '''Perform update on the deliverable'''
    
    deliverablevolume = get_object_or_404(DeliverableVolume, id=pk)
    project = deliverablevolume.deliverable.project
    
    # Can only update if the current user has enough rights:
    # - has specifically the permission change_deliverable
    # - or has the right to change the project this deliverable belongs to
    if request.user.has_perm('projects.change_deliverablevolume',deliverablevolume) or request.user.has_perm('projects.change_project',project):
        response = update_object(request,model=DeliverableVolume, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response


def delete_deliverablevolume(request, pk):
    '''Perform the deliverable delete'''
    
    deliverablevolume = get_object_or_404(DeliverableVolume, id=pk)
    deliverable = deliverablevolume.deliverable
    
    # It is only possible if the user has rights on the project
    if request.user.has_perm('projects.change_project',deliverable.project):
        response = delete_object(request, DeliverableVolume, deliverable.get_absolute_url(), object_id=pk, template_object_name="deliverablevolume")
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response



def update_task(request, pk):
    '''Perform update on the turnover'''
    
    task = get_object_or_404(Task, id=pk)
    
    # Can only update if the current user has enough rights:
    # - has specifically the permission change_turnover
    # - or has the right to change the project this deliverable belongs to
    if request.user.has_perm('projects.change_task',task) or request.user.has_perm('projects.change_project',turnover.project):
        response = update_object(request,form_class=TaskForm, object_id=pk)
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response
    



def delete_task(request, pk):
    '''Perform the task delete'''
    
    task = get_object_or_404(Task, id=pk)
    deliverable = task.deliverable
    
    # It is only possible if the user has rights on the deliverable
    if request.user.has_perm('projects.delete_task',task):
        response = delete_object(request, Task, deliverable.project.get_absolute_url(), object_id=pk, template_object_name="task")
    else:
        # if not allowed, return the page forbidden.html
        response = direct_to_template(request,template="forbidden.html")
    
    return response
