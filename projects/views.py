from django.views.generic import UpdateView
from guardian.decorators import permission_required
from django.utils.decorators import method_decorator

from projects.models import Project, Authorization, Deliverable, Turnover, Task
from services.models import Service

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
        

class ValidateServiceView(UpdateView):
    
    def dispatch(self, *args, **kwargs):
        deliverable = self.get_object()
        if self.request.user.has_perm('services.change_service',deliverable.service):
            return super(ValidateServiceView, self).dispatch(*args, **kwargs)
        else:
            return HttpResponse("Not allowed")


class TurnoverUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_turnover',(Turnover, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(TurnoverUpdateView, self).dispatch(*args, **kwargs)



class TaskUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_turnover',(Task, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)