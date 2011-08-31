from django.views.generic import UpdateView, DetailView
from guardian.decorators import permission_required
from django.utils.decorators import method_decorator

from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.create_update import update_object
from django.views.generic.simple import direct_to_template

from projects.models import Project, Authorization, Deliverable, Turnover, Task
from projects.forms import DeliverableForm, DeliverableValidateServiceForm





class ProjectUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_project',(Project, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)



class AuthorizationUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_authorization',(Authorization, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(AuthorizationUpdateView, self).dispatch(*args, **kwargs)



class DeliverableUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_deliverable',(Deliverable, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(DeliverableUpdateView, self).dispatch(*args, **kwargs)
        
        



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
    
    domain = get_object_or_404(Deliverable, id=pk)
    
    # It is only possible if the user has rights on the service
    if request.user.has_perm('services.change_service',domain.service):
        response = update_object(request,form_class=DeliverableValidateServiceForm, object_id=pk)
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