from django.views.generic import UpdateView, DetailView
from guardian.decorators import permission_required
from django.utils.decorators import method_decorator

from django.db.models import ProtectedError

from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.create_update import update_object, delete_object
from django.views.generic.simple import direct_to_template

from projects.models import Project, Authorization, Deliverable, Turnover, Task
from projects.forms import ProjectForm, DeliverableForm, DeliverableValidateServiceForm





def update_project(request, pk):
    '''Perform update on the project'''
    
    project = get_object_or_404(Project, id=pk)
    
    # Can only update if the current user has rights on the project
    if request.user.has_perm('projects.change_projectn',project):
        response = update_object(request, form_class=ProjectForm, object_id=pk)
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
    





class TurnoverUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_turnover',(Turnover, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(TurnoverUpdateView, self).dispatch(*args, **kwargs)



class TaskUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_turnover',(Task, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)
        