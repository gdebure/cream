from django.views.generic import UpdateView
from guardian.decorators import permission_required
from django.utils.decorators import method_decorator

from projects.models import Project, Authorization, Deliverable, Turnover

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
        


class TurnoverUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_turnover',(Turnover, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(TurnoverUpdateView, self).dispatch(*args, **kwargs)