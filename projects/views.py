from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
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
    success_url='/projects/projects/%(id)s'
    template_name='project_form.html'
    permission='projects.add_project'
    

class ProjectUpdateView(UpdateView,PermissionRequiredMixin):
    model = Project
    success_url='/projects/projects/%(id)s'
    template_name='project_form.html' 
    permission = 'projects.change_project'
    

class ProjectDeleteView(DeleteView,PermissionRequiredMixin):
    model=Project
    success_url='/projects/projects/'
    permission='projects.delete_project'
    
    
class AddDeliverableView(CreateView,PermissionRequiredMixin):
    model = Deliverable
    template_name='deliverable_form.html'
    permission='projects.add_deliverable'
    success_url='/projects/deliverable/%(id)s'
    permission='projects.add_deliverable'

    def get_context_data(self, **kwargs):
        context = super(AddDeliverableView,self).get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'project':project}
        return  context


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
    success_url='/projects/deliverable/%(id)s'
    template_name='deliverable_form.html'
    permission='projects.add_deliverable'
    

class DeliverableUpdateView(UpdateView,PermissionRequiredMixin):
    model = Deliverable
    success_url='/projects/deliverable/%(id)s'
    template_name='deliverable_form.html' 
    permission = 'projects.change_deliverable'
    

class DeliverableDeleteView(DeleteView,PermissionRequiredMixin):
    model=Deliverable
    success_url='/projects/deliverable/'
    template_name='deliverable_confirm_delete.html'
    permission='projects.delete_deliverable'
    
    
class AddDeliverableVolumeView(CreateView,PermissionRequiredMixin):
    model = DeliverableVolume
    template_name='deliverablevolume_form.html'
    permission='projects.add_deliverablevolume'
    success_url='/projects/deliverable_volume/%(id)s' 
    permission='projects.add_deliverablevolume'

    def get_context_data(self, **kwargs):
        context = super(AddDeliverableVolumeView,self).get_context_data(**kwargs)
        deliverable= Deliverable.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'deliverable':deliverable}
        return  context
    