from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from core.views import LoginRequiredMixin,PermissionRequiredMixin
from qualifications.models import SkillCategory


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