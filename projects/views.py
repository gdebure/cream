from django.views.generic import CreateView, DeleteView
from django.core.urlresolvers import reverse

from projects.models import Project, Deliverable, DeliverableVolume

class AddDeliverableView(CreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddDeliverableView,self).get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'project':project}
        return  context
    
    
    
class DeleteDeliverableView(DeleteView):
    
    project = None
    model = Deliverable
    template_name='deliverable_confirm_delete.html'
    
    def get_success_url(self):
        project = self.object.project
        url_params = dict()
        url_params['pk'] = project.id
        return reverse('project',kwargs=url_params)
    
    
class AddDeliverableVolumeView(CreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddDeliverableVolumeView,self).get_context_data(**kwargs)
        deliverable= Deliverable.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'deliverable':deliverable}
        return  context
    
class DeleteDeliverableVolumeView(DeleteView):
    
    deliverable = None
    model = DeliverableVolume
    template_name='deliverablevolume_confirm_delete.html'
    
    def get_success_url(self):
        deliverable = self.object.deliverable
        url_params = dict()
        url_params['pk'] = deliverable.id
        return reverse('deliverable',kwargs=url_params)
        