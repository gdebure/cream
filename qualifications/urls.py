from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from qualifications.models import Skill, SkillCategory, Job, EmployeeSkill, JobProfileSkill, Profile
from qualifications.forms import SkillForm

urlpatterns = patterns('',
    ##################################
    # Skills 
    (r'^skills/$', ListView.as_view( queryset=Skill.objects.order_by('category','name'), context_object_name='skills_list', ), ),
    (r'^skills/(?P<pk>\d+)/$', DetailView.as_view( model=Skill, ), ),
    (r'^skills/create/$', CreateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s' ), ),
    (r'^skills/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s' ), ),
    (r'^skills/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=Skill, success_url='/qualifications/skills/' ), ),
    ##################################
    
    ##################################
    # Skill Categories 
    (r'^skill_categories/$', ListView.as_view( queryset=SkillCategory.objects.order_by('name'), context_object_name='skill_categories_list', ), ),
    (r'^skill_categories/(?P<pk>\d+)/$', DetailView.as_view( model=SkillCategory, ), ),
    (r'^skill_categories/create/$', CreateView.as_view( model=SkillCategory, success_url='/qualifications/skill_categories/%(id)s' ), ),
    (r'^skill_categories/(?P<pk>\d+)/update/$', UpdateView.as_view( model=SkillCategory, success_url='/qualifications/skill_categories/%(id)s' ), ),
    (r'^skill_categories/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=SkillCategory, success_url='/qualifications/skill_categories/' ), ),
    ##################################
    
    ##################################
    # Jobs
    (r'^jobs/$', ListView.as_view( queryset=Job.objects.order_by('name'), context_object_name='jobs_list', ), ),
    (r'^jobs/(?P<pk>\d+)/$', DetailView.as_view( model=Job, ), ),
    (r'^jobs/create/$', CreateView.as_view( model=Job, success_url='/qualifications/jobs/%(id)s' ), ),
    (r'^jobs/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Job, success_url='/qualifications/jobs/%(id)s' ), ),
    (r'^jobs/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=Job, success_url='/qualifications/jobs/' ), ),
    ##################################
    
    ##################################
    # Employee Skills 
    (r'^employee_skills/$', ListView.as_view( queryset=EmployeeSkill.objects.order_by('employee','skill'), context_object_name='employeeskills_list', ), ),
    (r'^employee_skills/(?P<pk>\d+)/$', DetailView.as_view( model=EmployeeSkill, ), ),
    (r'^employee_skills/create/$', CreateView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/%(id)s' ), ),
    (r'^employee_skills/(?P<pk>\d+)/update/$', UpdateView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/%(id)s' ), ),
    (r'^employee_skills/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=EmployeeSkill, success_url='/qualifications/employee_skills/' ), ),
    ##################################
    
    ##################################
    # profiles 
    (r'^profiles/$', ListView.as_view( queryset=Profile.objects.order_by('category','name'), context_object_name='profiles_list', ), ),
    (r'^profiles/(?P<pk>\d+)/$', DetailView.as_view( model=Profile, ), ),
    (r'^profiles/create/$', CreateView.as_view( model=Profile, success_url='/qualifications/profiles/%(id)s' ), ),
    (r'^profiles/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Profile, success_url='/qualifications/profiles/%(id)s' ), ),
    (r'^profiles/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=Profile, success_url='/qualifications/profiles/' ), ),
    ##################################
    
    ##################################
    # job profile Skills 
    (r'^job_skills/$', ListView.as_view( queryset=JobProfileSkill.objects.order_by('job','skill'), context_object_name='jobprofileskills_list', ), ),
    (r'^job_skills/(?P<pk>\d+)/$', DetailView.as_view( model=JobProfileSkill, ), ),
    (r'^job_skills/create/$', CreateView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/%(id)s' ), ),
    (r'^job_skills/(?P<pk>\d+)/update/$', UpdateView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/%(id)s' ), ),
    (r'^job_skills/(?P<pk>\d+)/delete/$', DeleteView.as_view( model=JobProfileSkill, success_url='/qualifications/job_skills/' ), ),
    ##################################
    
)