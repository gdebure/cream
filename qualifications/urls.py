from django.conf.urls import patterns,url
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import permission_required, login_required

from qualifications.models import Skill, SkillCategory, Job, EmployeeSkill, JobProfileSkill, Profile, JobEmployee
from qualifications.forms import SkillForm

urlpatterns = patterns('',
    ##################################
    # Skills 
    (r'^skills/$', login_required()(ListView.as_view( model=Skill, context_object_name='skills_list', template_name='skill_list.html')), ),
    (r'^skills/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Skill, )), ),
    (r'^skills/create/$', permission_required('qualifications.add_skill')(CreateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s', template_name='skill_form.html' )), ),
    (r'^skills/(?P<pk>\d+)/update/$', permission_required('qualifications.change_skill')(UpdateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s' )), ),
    (r'^skills/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_skill')(DeleteView.as_view( model=Skill, success_url='/qualifications/skills/' )), ),
    ##################################
    
    ##################################
    # Skill Categories 
    (r'^skill_categories/$', login_required()(ListView.as_view( model=SkillCategory, context_object_name='skill_categories_list', template_name='skillcategory_list.html')), ),
    (r'^skill_categories/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=SkillCategory, template_name='skillcategory_detail.html' )), ),
    (r'^skill_categories/create/$', permission_required('qualifications.add_skillcategory')(CreateView.as_view( model=SkillCategory, success_url='/qualifications/skill_categories/%(id)s', template_name='skillcategory_form.html' )), ),
    (r'^skill_categories/(?P<pk>\d+)/update/$', permission_required('qualifications.change_skillcategory')(UpdateView.as_view( model=SkillCategory, success_url='/qualifications/skill_categories/%(id)s', template_name='skillcategory_form.html' )), ),
    (r'^skill_categories/(?P<pk>\d+)/delete/$', permission_required('qualifications.add_skillcategory')(DeleteView.as_view( model=SkillCategory, success_url='/qualifications/skill_categories/' )), ),
    ##################################
    
    ##################################
    # Jobs
    (r'^jobs/$', login_required()(ListView.as_view( model=Job, context_object_name='jobs_list', )), ),
    (r'^jobs/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Job, )), ),
    (r'^jobs/create/$', permission_required('qualifications.add_job')(CreateView.as_view( model=Job, success_url='/qualifications/jobs/%(id)s' )), ),
    (r'^jobs/(?P<pk>\d+)/update/$', permission_required('qualifications.change_job')(UpdateView.as_view( model=Job, success_url='/qualifications/jobs/%(id)s' )), ),
    (r'^jobs/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_job')(DeleteView.as_view( model=Job, success_url='/qualifications/jobs/' )), ),
    ##################################
    
    ##################################
    # Employee Skills 
    (r'^employee_skills/$', login_required()(ListView.as_view( model=EmployeeSkill, context_object_name='employeeskills_list', )), ),
    (r'^employee_skills/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=EmployeeSkill, )), ),
    (r'^employee_skills/create/$', permission_required('qualifications.add_employeeskill')(CreateView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/%(id)s' )), ),
    (r'^employee_skills/(?P<pk>\d+)/update/$', permission_required('qualifications.change_employeeskill')(UpdateView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/%(id)s' )), ),
    (r'^employee_skills/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_employeeskill')(DeleteView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/' )), ),
    ##################################
    
    ##################################
    # profiles 
    (r'^profiles/$', login_required()(ListView.as_view( model=Profile, context_object_name='profiles_list', )), ),
    (r'^profiles/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=Profile, )), ),
    (r'^profiles/create/$', permission_required('qualifications.add_profile')(CreateView.as_view( model=Profile, success_url='/qualifications/profiles/%(id)s' )), ),
    (r'^profiles/(?P<pk>\d+)/update/$', permission_required('qualifications.change_profile')(UpdateView.as_view( model=Profile, success_url='/qualifications/profiles/%(id)s' )), ),
    (r'^profiles/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_profile')(DeleteView.as_view( model=Profile, success_url='/qualifications/profiles/' )), ),
    ##################################
    
    ##################################
    # job profile Skills 
    (r'^job_skills/$', login_required()(ListView.as_view( model=JobProfileSkill, context_object_name='jobprofileskills_list', )), ),
    (r'^job_skills/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=JobProfileSkill, )), ),
    (r'^job_skills/create/$', permission_required('qualifications.add_jobprofileskill')(CreateView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/%(id)s' )), ),
    (r'^job_skills/(?P<pk>\d+)/update/$', permission_required('qualifications.add_jobprofileskill')(UpdateView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/%(id)s' )), ),
    (r'^job_skills/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_jobprofileskill')(DeleteView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/' )), ),
    ##################################
    
    ##################################
    # job Employees 
    (r'^job_employees/$', login_required()(ListView.as_view( model=JobEmployee, context_object_name='jobemployees_list', )), ),
    (r'^job_employees/(?P<pk>\d+)/$', login_required()(DetailView.as_view( model=JobEmployee, )), ),
    (r'^job_employees/create/$', permission_required('qualifications.add_jobemployee')(CreateView.as_view( model=JobEmployee, success_url='/qualifications/job_employees/%(id)s' )), ),
    (r'^job_employees/(?P<pk>\d+)/update/$', permission_required('qualifications.add_jobemployee')(UpdateView.as_view( model=JobEmployee, success_url='/qualifications/job_employees/%(id)s' )), ),
    (r'^job_employees/(?P<pk>\d+)/delete/$', permission_required('qualifications.delete_jobemployee')(DeleteView.as_view( model=JobEmployee, success_url='/qualifications/job_employees/' )), ),
    ##################################
    
    
)