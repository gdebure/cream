from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from core.views import LoginRequiredMixin, PermissionRequiredMixin
from qualifications.models import SkillCategory, Skill, Job, Position, EmployeeSkill, JobProfileSkill


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


#############################
### Employee Skills Views ###
#############################

class EmployeeSkillsListView(ListView,LoginRequiredMixin):
    model=EmployeeSkill
    context_object_name='employeeskills_list'
    template_name='employeeskill_list.html'

    
class EmployeeSkillDetailView(DetailView,LoginRequiredMixin):
    model = EmployeeSkill
    template_name='employeeskill_detail.html'

    
class EmployeeSkillCreateView(CreateView,PermissionRequiredMixin):
    model=EmployeeSkill
    success_url='/qualifications/employees_kills/%(id)s'
    template_name='employeeskill_form.html'
    permission='qualifications.add_employeeskill'
    

class EmployeeSkillUpdateView(UpdateView,PermissionRequiredMixin):
    model = EmployeeSkill
    success_url='/qualifications/employee_skills/%(id)s'
    template_name='employeeskill_form.html' 
    permission = 'qualifications.change_employeeskill'
    

class EmployeeSkillDeleteView(DeleteView,PermissionRequiredMixin):
    model=EmployeeSkill
    success_url='/qualifications/employeeskills/'
    template_name='employeeskill_confirm_delete.html'
    permission='qualifications.add_employeeskill'


#################################
### Job Profiles Skills Views ###
#################################

class JobProfileSkillsListView(ListView,LoginRequiredMixin):
    model=JobProfileSkill
    context_object_name='jobprofileskills_list'
    template_name='jobprofileskill_list.html'

    
class JobProfileSkillDetailView(DetailView,LoginRequiredMixin):
    model = JobProfileSkill
    template_name='jobprofileskill_detail.html'

    
class JobProfileSkillCreateView(CreateView,PermissionRequiredMixin):
    model=JobProfileSkill
    success_url='/qualifications/employees_kills/%(id)s'
    template_name='jobprofileskill_form.html'
    permission='qualifications.add_jobprofileskill'
    

class JobProfileSkillUpdateView(UpdateView,PermissionRequiredMixin):
    model = JobProfileSkill
    success_url='/qualifications/employee_skills/%(id)s'
    template_name='jobprofileskill_form.html' 
    permission = 'qualifications.change_jobprofileskill'
    

class JobProfileSkillDeleteView(DeleteView,PermissionRequiredMixin):
    model=JobProfileSkill
    success_url='/qualifications/jobprofileskills/'
    template_name='jobprofileskill_confirm_delete.html'
    permission='qualifications.add_jobprofileskill'
