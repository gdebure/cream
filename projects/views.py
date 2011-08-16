from django.views.generic import UpdateView
from guardian.decorators import permission_required
from django.utils.decorators import method_decorator

from projects.models import Project

class ProjectUpdateView(UpdateView):

    @method_decorator(permission_required('projects.change_project',(Project, 'id', 'pk')))
    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)
