from django.conf.urls import patterns,url
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from django.contrib.auth.decorators import permission_required, login_required

from qualifications.models import Skill, SkillCategory, Job, EmployeeSkill, JobProfileSkill, Profile, JobEmployee
from qualifications.forms import SkillForm

from qualifications.views import SkillCategoriesListView, SkillCategoryDetailView, SkillCategoryCreateView, SkillCategoryUpdateView, SkillCategoryDeleteView
from qualifications.views import SkillsListView, SkillDetailView, SkillCreateView, SkillUpdateView, SkillDeleteView


urlpatterns = patterns('',
    
    ##################################
    # Skill Categories 
    url(r'^skill_categories/$', SkillCategoriesListView.as_view(), name='skill_categories_list'),
    url(r'^skill_categories/(?P<pk>\d+)/$', SkillCategoryDetailView.as_view(), name='skill_category_detail'),
    url(r'^skill_categories/create/$', SkillCategoryCreateView.as_view(), name='create_skill_category' ),
    url(r'^skill_categories/(?P<pk>\d+)/update/$', SkillCategoryUpdateView.as_view(), name='update_skill_category' ),
    url(r'^skill_categories/(?P<pk>\d+)/delete/$', SkillCategoryDeleteView.as_view(), ),
    ##################################
    
    ##################################
    # Skills 
    url(r'^skills/$', SkillsListView.as_view(), name='skills_list'),
    url(r'^skills/(?P<pk>\d+)/$', SkillDetailView.as_view(), name='skill_detail' ),
    url(r'^skills/create/$', permission_required('qualifications.add_skill')(CreateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s', template_name='skill_form.html' )), ),
    url(r'^skills/(?P<pk>\d+)/update/$', permission_required('qualifications.change_skill')(UpdateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s' )), ),
    url(r'^skills/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_skill')(DeleteView.as_view( model=Skill, success_url='/qualifications/skills/' )), ),
    ##################################
        
    ##################################
    # Jobs
    url(r'^jobs/$', login_required()(ListView.as_view( model=Job, context_object_name='jobs_list', )), ),
    url(r'^jobs/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Job, )), ),
    url(r'^jobs/create/$', permission_required('qualifications.add_job')(CreateView.as_view( model=Job, success_url='/qualifications/jobs/%(id)s' )), ),
    url(r'^jobs/(?P<pk>\d+)/update/$', permission_required('qualifications.change_job')(UpdateView.as_view( model=Job, success_url='/qualifications/jobs/%(id)s' )), ),
    url(r'^jobs/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_job')(DeleteView.as_view( model=Job, success_url='/qualifications/jobs/' )), ),
    ##################################
    
    ##################################
    # Employee Skills 
    url(r'^employee_skills/$', login_required()(ListView.as_view( model=EmployeeSkill, context_object_name='employeeskills_list', )), ),
    url(r'^employee_skills/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=EmployeeSkill, )), ),
    url(r'^employee_skills/create/$', permission_required('qualifications.add_employeeskill')(CreateView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/%(id)s' )), ),
    url(r'^employee_skills/(?P<pk>\d+)/update/$', permission_required('qualifications.change_employeeskill')(UpdateView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/%(id)s' )), ),
    url(r'^employee_skills/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_employeeskill')(DeleteView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/' )), ),
    ##################################
    
    ##################################
    # profiles 
    url(r'^profiles/$', login_required()(ListView.as_view( model=Profile, context_object_name='profiles_list', )), ),
    url(r'^profiles/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Profile, )), ),
    url(r'^profiles/create/$', permission_required('qualifications.add_profile')(CreateView.as_view( model=Profile, success_url='/qualifications/profiles/%(id)s' )), ),
    url(r'^profiles/(?P<pk>\d+)/update/$', permission_required('qualifications.change_profile')(UpdateView.as_view( model=Profile, success_url='/qualifications/profiles/%(id)s' )), ),
    url(r'^profiles/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_profile')(DeleteView.as_view( model=Profile, success_url='/qualifications/profiles/' )), ),
    ##################################
    
    ##################################
    # job profile Skills 
    url(r'^job_skills/$', login_required()(ListView.as_view( model=JobProfileSkill, context_object_name='jobprofileskills_list', )), ),
    url(r'^job_skills/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=JobProfileSkill, )), ),
    url(r'^job_skills/create/$', permission_required('qualifications.add_jobprofileskill')(CreateView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/%(id)s' )), ),
    url(r'^job_skills/(?P<pk>\d+)/update/$', permission_required('qualifications.add_jobprofileskill')(UpdateView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/%(id)s' )), ),
    url(r'^job_skills/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_jobprofileskill')(DeleteView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/' )), ),
    ##################################
    
    ##################################
    # job Employees 
    url(r'^job_employees/$', login_required()(ListView.as_view( model=JobEmployee, context_object_name='jobemployees_list', )), ),
    url(r'^job_employees/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=JobEmployee, )), ),
    url(r'^job_employees/create/$', permission_required('qualifications.add_jobemployee')(CreateView.as_view( model=JobEmployee, success_url='/qualifications/job_employees/%(id)s' )), ),
    url(r'^job_employees/(?P<pk>\d+)/update/$', permission_required('qualifications.add_jobemployee')(UpdateView.as_view( model=JobEmployee, success_url='/qualifications/job_employees/%(id)s' )), ),
    url(r'^job_employees/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_jobemployee')(DeleteView.as_view( model=JobEmployee, success_url='/qualifications/job_employees/' )), ),
    ##################################
    
    
)