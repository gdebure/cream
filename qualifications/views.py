from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from qualifications.models import SkillCategory, Skill, Job, Position, EmployeeSkill, JobProfileSkill, EmployeePosition


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
    template_name='skillcategory_form.html'
    permission='qualifications.add_skillcategory'
    fields=['name','description']
    
    def get_success_url(self):
        return reverse_lazy('skillcategory_detail',args=[self.object.id])
    

class SkillCategoryUpdateView(UpdateView,PermissionRequiredMixin):
    model = SkillCategory
    template_name='skillcategory_form.html' 
    permission = 'qualifications.change_skillcategory'
    fields=['name','description']
    
    def get_success_url(self):
        return reverse_lazy('skillcategory_detail',args=[self.object.id])

class SkillCategoryDeleteView(DeleteView,PermissionRequiredMixin):
    model=SkillCategory
    permission='qualifications.add_skillcategory'
    
    def get_success_url(self):
        return reverse_lazy('skillcategories_list')
    
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
    template_name='skill_form.html'
    permission='qualifications.add_skill'
    fields=['category','name','enabled','description']
    
    def get_success_url(self):
        return reverse_lazy('skill_detail',args=[self.object.id])


class SkillUpdateView(UpdateView,PermissionRequiredMixin):
    model = Skill
    template_name='skill_form.html' 
    permission = 'qualifications.change_skill'
    fields=['category','name','enabled','description']
    
    def get_success_url(self):
        return reverse_lazy('skill_detail',args=[self.object.id])


class SkillDeleteView(DeleteView,PermissionRequiredMixin):
    model=Skill
    template_name='skill_confirm_delete.html'
    permission='qualifications.add_skill'

    def get_success_url(self):
        return reverse_lazy('skills_list')
    
    
class AddSkillView(CreateView,PermissionRequiredMixin):
    model=Skill
    success_url='/qualifications/skills/%(id)s'
    template_name='skill_form.html'
    permission='qualifications.add_skill'
    fields=['category','name','enabled','description']
    
    def get_context_data(self, **kwargs):
        context = super(AddSkillView,self).get_context_data(**kwargs)
        category = SkillCategory.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'category':category}
        return  context
    
    def get_success_url(self):
        return reverse_lazy('skill_detail',args=[self.object.id])
    
    
    
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
    template_name='job_form.html'
    permission='qualifications.add_job'
    fields=['name','description']
    
    def get_success_url(self):
        return reverse_lazy('job_detail',args=[self.object.id])

class JobUpdateView(UpdateView,PermissionRequiredMixin):
    model = Job
    template_name='job_form.html' 
    permission = 'qualifications.change_job'
    fields=['name','description']
    
    def get_success_url(self):
        return reverse_lazy('job_detail',args=[self.object.id])
    

class JobDeleteView(DeleteView,PermissionRequiredMixin):
    model=Job
    template_name='job_confirm_delete.html'
    permission='qualifications.add_job'

    def get_success_url(self):
        return reverse_lazy('skills_list')


class AddPositionView(CreateView,PermissionRequiredMixin):
    model=Position
    template_name='position_form.html'
    permission='qualifications.add_position'
    fields=['job','profile','project','status','location','start_date','publish_date','headcount','comment']
    
    def get_context_data(self, **kwargs):
        context = super(AddPositionView,self).get_context_data(**kwargs)
        job = Job.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'job':job}
        return  context

    def get_success_url(self):
        return reverse_lazy('position_detail',args=[self.object.id])


######################
### Position Views ###
######################

class PositionsListView(ListView,LoginRequiredMixin):
    model=Position
    context_object_name='positions_list'
    template_name='position_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListView,self).get_context_data(**kwargs)
        context['viewing'] = "all"
        return  context

class OpenPositionsListView(PositionsListView):
    
    def get_queryset(self):
        return self.model.objects.exclude(status='S').exclude(status='C')

    def get_context_data(self, **kwargs):
        context = super(ListView,self).get_context_data(**kwargs)
        context['viewing'] = "open"
        return  context
    
class PositionDetailView(DetailView,LoginRequiredMixin):
    model = Position
    template_name='position_detail.html'

    
class PositionCreateView(CreateView,PermissionRequiredMixin):
    model=Position
    template_name='position_form.html'
    permission='qualifications.add_position'
    fields=['job','profile','project','status','location','start_date','publish_date','headcount','comment']
    
    def get_success_url(self):
        return reverse_lazy('position_detail',args=[self.object.id])
    

class PositionUpdateView(UpdateView,PermissionRequiredMixin):
    model = Position
    template_name='position_form.html' 
    permission = 'qualifications.change_position'
    fields=['job','profile','project','status','location','start_date','publish_date','headcount','comment']
    
    def get_success_url(self):
        return reverse_lazy('position_detail',args=[self.object.id])
    

class PositionDeleteView(DeleteView,PermissionRequiredMixin):
    model=Position
    template_name='position_confirm_delete.html'
    permission='qualifications.add_position'
    
    def get_success_url(self):
        return reverse_lazy('positions_list')



class AddEmployeePositionView(CreateView,PermissionRequiredMixin):
    model=EmployeePosition
    template_name='employeeposition_form.html'
    permission='qualifications.add_employeeposition'
    fields=['employee','position','status','start_date','end_date','comments']
    
    def get_context_data(self, **kwargs):
        context = super(AddEmployeePositionView,self).get_context_data(**kwargs)
        position = Position.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'position':position}
        return context
    
    def get_success_url(self):
        return reverse_lazy('employeeposition_detail',args=[self.object.id])

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
    template_name='employeeskill_form.html'
    permission='qualifications.add_employeeskill'
    fields=['employee','skill','level']
    
    def get_success_url(self):
        return reverse_lazy('employeeskill_detail',args=[self.object.id])
    
    
    
class EmployeeSkillUpdateView(UpdateView,PermissionRequiredMixin):
    model = EmployeeSkill
    template_name='employeeskill_form.html' 
    permission = 'qualifications.change_employeeskill'
    fields=['employee','skill','level']
    
    def get_success_url(self):
        return reverse_lazy('employeeskill_detail',args=[self.object.id])
    

class EmployeeSkillDeleteView(DeleteView,PermissionRequiredMixin):
    model=EmployeeSkill
    template_name='employeeskill_confirm_delete.html'
    permission='qualifications.add_employeeskill'
    
    def get_success_url(self):
        return reverse_lazy('employeeskills_list')


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
    template_name='jobprofileskill_form.html'
    permission='qualifications.add_jobprofileskill'
    fields=['job','profile','skill','level']
    
    def get_success_url(self):
        return reverse_lazy('jobprofileskill_detail',args=[self.object.id])
    

class JobProfileSkillUpdateView(UpdateView,PermissionRequiredMixin):
    model = JobProfileSkill
    template_name='jobprofileskill_form.html' 
    permission = 'qualifications.change_jobprofileskill'
    fields=['job','profile','skill','level']
    
    def get_success_url(self):
        return reverse_lazy('jobprofileskill_detail',args=[self.object.id])
    

class JobProfileSkillDeleteView(DeleteView,PermissionRequiredMixin):
    model=JobProfileSkill
    template_name='jobprofileskill_confirm_delete.html'
    permission='qualifications.add_jobprofileskill'

    def get_success_url(self):
        return reverse_lazy('jobprofileskills_list')

################################
### Employee Positions Views ###
################################

class EmployeePositionsListView(ListView,LoginRequiredMixin):
    model=EmployeePosition
    context_object_name='employeepositions_list'
    template_name='employeeposition_list.html'

    
class EmployeePositionDetailView(DetailView,LoginRequiredMixin):
    model = EmployeePosition
    template_name='employeeposition_detail.html'

    
class EmployeePositionCreateView(CreateView,PermissionRequiredMixin):
    model=EmployeePosition
    template_name='employeeposition_form.html'
    permission='qualifications.add_employeeposition'
    fields=['employee','position','status','start_date','end_date','comments']
    
    def get_success_url(self):
        return reverse_lazy('employeeposition_detail',args=[self.object.id])
    

class EmployeePositionUpdateView(UpdateView,PermissionRequiredMixin):
    model = EmployeePosition
    template_name='employeeposition_form.html' 
    permission = 'qualifications.change_employeeposition'
    fields=['employee','position','status','start_date','end_date','comments']
    
    def get_success_url(self):
        return reverse_lazy('employeeposition_detail',args=[self.object.id])
    

class EmployeePositionDeleteView(DeleteView,PermissionRequiredMixin):
    model=EmployeePosition
    template_name='employeeposition_confirm_delete.html'
    permission='qualifications.add_employeeposition'
    
    def get_success_url(self):
        return reverse_lazy('employeepositions_list')
    
