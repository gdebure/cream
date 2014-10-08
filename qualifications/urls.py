from django.conf.urls import patterns,url
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from django.contrib.auth.decorators import permission_required, login_required

from qualifications.models import Skill, SkillCategory, Job, EmployeeSkill, JobProfileSkill, Profile, JobEmployee
from qualifications.forms import SkillForm

from qualifications.views import SkillCategoriesListView, SkillCategoryDetailView, SkillCategoryCreateView, SkillCategoryUpdateView, SkillCategoryDeleteView
from qualifications.views import SkillsListView, SkillDetailView, SkillCreateView, SkillUpdateView, SkillDeleteView, AddSkillView
from qualifications.views import JobsListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView

urlpatterns = patterns('',
    
    ##################################
    # Skill Categories 
    url(r'^skill_categories/$', SkillCategoriesListView.as_view(), name='skill_categories_list'),
    url(r'^skill_categories/(?P<pk>\d+)/$', SkillCategoryDetailView.as_view(), name='skill_category_detail'),
    url(r'^skill_categories/create/$', SkillCategoryCreateView.as_view(), name='create_skill_category' ),
    url(r'^skill_categories/(?P<pk>\d+)/update/$', SkillCategoryUpdateView.as_view(), name='update_skill_category' ),
    url(r'^skill_categories/(?P<pk>\d+)/delete/$', SkillCategoryDeleteView.as_view(), name='delete_skill_category' ),
    
    url(r'^skill_categories/(?P<pk>\d+)/add_skill/$', AddSkillView.as_view(), name='add_skill' ),
    ##################################
    
    ##################################
    # Skills 
    url(r'^skills/$', SkillsListView.as_view(), name='skills_list'),
    url(r'^skills/(?P<pk>\d+)/$', SkillDetailView.as_view(), name='skill_detail' ),
    url(r'^skills/create/$', SkillCreateView.as_view(), name='create_skill'),
    url(r'^skills/(?P<pk>\d+)/update/$', SkillUpdateView.as_view(), name='update_skill' ),
    url(r'^skills/(?P<pk>\d+)/delete/$', SkillDeleteView.as_view(), name='delete_skill' ),
    ##################################
        
    ##################################
    # Jobs
    url(r'^jobs/$', JobsListView.as_view(), name='jobs_list'),
    url(r'^jobs/(?P<pk>\d+)/$', JobDetailView.as_view(), name='job_detail' ),
    url(r'^jobs/create/$', JobCreateView.as_view(), name='create_job' ),
    url(r'^jobs/(?P<pk>\d+)/update/$', JobUpdateView.as_view(), name='update_job' ),
    url(r'^jobs/(?P<pk>\d+)/delete/$', JobDeleteView.as_view(), name='delete_job' ),
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