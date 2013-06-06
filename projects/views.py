from django.views.generic import CreateView

from projects.models import Project, Deliverable

class AddDeliverableView(CreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddDeliverableView,self).get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'project':project}
        return  context
    
class AddDeliverableVolumeView(CreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddDeliverableVolumeView,self).get_context_data(**kwargs)
        deliverable= Deliverable.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'deliverable':deliverable}
        return  context