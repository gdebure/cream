from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from projects.models import Project, Deliverable, DeliverableVolume


#####################
### Projects View ###
#####################

class ProjectListView(ListView, LoginRequiredMixin):
    model = Project
    context_object_name='projects_list'
    template_name='project_list.html'


class ProjectDetailView(DetailView,LoginRequiredMixin):
    model = Project()
    template_name='project_detail.html'
    
    
class ProjectCreateView(CreateView,PermissionRequiredMixin):
    model=Project
    template_name='project_form.html'
    permission='projects.add_project'
    
    def get_success_url(self):
        return reverse_lazy('project_detail',args=[self.object.id])
    

class ProjectUpdateView(UpdateView,PermissionRequiredMixin):
    model = Project
    template_name='project_form.html' 
    permission = 'projects.change_project'
    
    def get_success_url(self):
        return reverse_lazy('project_detail',args=[self.object.id])
    

class ProjectDeleteView(DeleteView,PermissionRequiredMixin):
    model=Project
    permission='projects.delete_project'
    
    def get_success_url(self):
        return reverse_lazy('projects_list',args=[self.object.id])
    
    
class AddDeliverableView(CreateView,PermissionRequiredMixin):
    model = Deliverable
    template_name='deliverable_form.html'
    permission='projects.add_deliverable'
    permission='projects.add_deliverable'

    def get_context_data(self, **kwargs):
        context = super(AddDeliverableView,self).get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'project':project}
        return  context
    
    def get_success_url(self):
        return reverse_lazy('deliverable_detail',args=[self.object.id])


#####################
### Deliverables View ###
#####################

class DeliverableListView(ListView, LoginRequiredMixin):
    model = Deliverable
    context_object_name='deliverables_list'
    template_name='deliverable_list.html'


class DeliverableDetailView(DetailView,LoginRequiredMixin):
    model = Deliverable()
    template_name='deliverable_detail.html'
    
    
class DeliverableCreateView(CreateView,PermissionRequiredMixin):
    model=Deliverable
    template_name='deliverable_form.html'
    permission='projects.add_deliverable'
    
    def get_success_url(self):
        return reverse_lazy('deliverable_detail',args=[self.object.id])
    

class DeliverableUpdateView(UpdateView,PermissionRequiredMixin):
    model = Deliverable
    template_name='deliverable_form.html' 
    permission = 'projects.change_deliverable'
    
    def get_success_url(self):
        return reverse_lazy('deliverable_detail',args=[self.object.id])
    

class DeliverableDeleteView(DeleteView,PermissionRequiredMixin):
    model=Deliverable
    template_name='deliverable_confirm_delete.html'
    permission='projects.delete_deliverable'
    
    def get_success_url(self):
        return reverse_lazy('deliverables_list')
    
    
class AddDeliverableVolumeView(CreateView,PermissionRequiredMixin):
    model = DeliverableVolume
    template_name='deliverablevolume_form.html'
    permission='projects.add_deliverablevolume'
    permission='projects.add_deliverablevolume'

    def get_context_data(self, **kwargs):
        context = super(AddDeliverableVolumeView,self).get_context_data(**kwargs)
        deliverable= Deliverable.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'deliverable':deliverable}
        return  context
    
    def get_success_url(self):
        return reverse_lazy('deliverablevolume_detail',args=[self.object.id])
    
class DeliverableVolumeUpdateView(UpdateView,PermissionRequiredMixin):
    model = DeliverableVolume
    template_name='deliverablevolume_form.html' 
    permission = 'projects.change_deliverablevolume'
    
    def get_success_url(self):
        return reverse_lazy('deliverablevolume_detail',args=[self.object.id])
    