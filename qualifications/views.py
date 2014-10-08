from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from core.views import LoginRequiredMixin,PermissionRequiredMixin
from qualifications.models import SkillCategory, Skill, Job


##############################
### Skill Categories Views ###
##############################

class SkillCategoriesListView(ListView,LoginRequiredMixin):
    model=SkillCategory
    context_object_name='skill_categories_list'
    template_name='skillcategory_list.html'

    
class SkillCategoryDetailView(DetailView,LoginRequiredMixin):
    model = SkillCategory
    template_name='skillcategory_detail.html'

    
class SkillCategoryCreateView(CreateView,PermissionRequiredMixin):
    model=SkillCategory
    success_url='/qualifications/skill_categories/%(id)s'
    template_name='skillcategory_form.html'
    permission='qualifications.add_skillcategory'
    

class SkillCategoryUpdateView(UpdateView,PermissionRequiredMixin):
    model = SkillCategory
    success_url='/qualifications/skill_categories/%(id)s'
    template_name='skillcategory_form.html' 
    permission = 'qualifications.change_skillcategory'
    

class SkillCategoryDeleteView(DeleteView,PermissionRequiredMixin):
    model=SkillCategory
    success_url='/qualifications/skill_categories/'
    permission='qualifications.add_skillcategory'
    
    
###################
### Skill Views ###
###################

class SkillsListView(ListView,LoginRequiredMixin):
    model=Skill
    context_object_name='skills_list'
    template_name='skill_list.html'

    
class SkillDetailView(DetailView,LoginRequiredMixin):
    model = Skill
    template_name='skill_detail.html'

    
class SkillCreateView(CreateView,PermissionRequiredMixin):
    model=Skill
    success_url='/qualifications/skills/%(id)s'
    template_name='skill_form.html'
    permission='qualifications.add_skill'
    

class SkillUpdateView(UpdateView,PermissionRequiredMixin):
    model = Skill
    success_url='/qualifications/skills/%(id)s'
    template_name='skill_form.html' 
    permission = 'qualifications.change_skill'
    

class SkillDeleteView(DeleteView,PermissionRequiredMixin):
    model=Skill
    success_url='/qualifications/skills/'
    template_name='skill_confirm_delete.html'
    permission='qualifications.add_skill'

    
class AddSkillView(CreateView,PermissionRequiredMixin):
    model=Skill
    success_url='/qualifications/skills/%(id)s'
    template_name='skill_form.html'
    permission='qualifications.add_skill'
    
    def get_context_data(self, **kwargs):
        context = super(AddSkillView,self).get_context_data(**kwargs)
        category = SkillCategory.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'category':category}
        return  context
    
    
    
#################
### Job Views ###
#################

class JobsListView(ListView,LoginRequiredMixin):
    model=Job
    context_object_name='jobs_list'
    template_name='job_list.html'

    
class JobDetailView(DetailView,LoginRequiredMixin):
    model = Job
    template_name='job_detail.html'

    
class JobCreateView(CreateView,PermissionRequiredMixin):
    model=Job
    success_url='/qualifications/jobs/%(id)s'
    template_name='job_form.html'
    permission='qualifications.add_job'
    

class JobUpdateView(UpdateView,PermissionRequiredMixin):
    model = Job
    success_url='/qualifications/jobs/%(id)s'
    template_name='job_form.html' 
    permission = 'qualifications.change_job'
    

class JobDeleteView(DeleteView,PermissionRequiredMixin):
    model=Job
    success_url='/qualifications/jobs/'
    template_name='job_confirm_delete.html'
    permission='qualifications.add_job'
