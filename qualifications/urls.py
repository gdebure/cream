from django.conf.urls import patterns,url

from qualifications.views import SkillCategoriesListView, SkillCategoryDetailView, SkillCategoryCreateView, SkillCategoryUpdateView, SkillCategoryDeleteView
from qualifications.views import SkillsListView, SkillDetailView, SkillCreateView, SkillUpdateView, SkillDeleteView, AddSkillView
from qualifications.views import JobsListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView, AddPositionView
from qualifications.views import PositionsListView, OpenPositionsListView, PositionDetailView, PositionCreateView, PositionUpdateView, PositionDeleteView, AddEmployeePositionView
from qualifications.views import EmployeeSkillsListView, EmployeeSkillDetailView, EmployeeSkillCreateView, EmployeeSkillUpdateView, EmployeeSkillDeleteView
from qualifications.views import JobProfileSkillsListView, JobProfileSkillDetailView, JobProfileSkillCreateView, JobProfileSkillUpdateView, JobProfileSkillDeleteView
from qualifications.views import EmployeePositionsListView, EmployeePositionDetailView, EmployeePositionCreateView, EmployeePositionUpdateView, EmployeePositionDeleteView


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
    
    url(r'^jobs/(?P<pk>\d+)/add_position/$', AddPositionView.as_view(), name='add_position' ),
    ##################################
    
    ##################################
    # Positions
    url(r'^positions/$', PositionsListView.as_view(), name='positions_list'),
    url(r'^positions/open/$', OpenPositionsListView.as_view(), name='open_positions_list'),
    url(r'^positions/(?P<pk>\d+)/$', PositionDetailView.as_view(), name='position_detail' ),
    url(r'^positions/create/$', PositionCreateView.as_view(), name='create_position' ),
    url(r'^positions/(?P<pk>\d+)/update/$', PositionUpdateView.as_view(), name='update_position' ),
    url(r'^positions/(?P<pk>\d+)/delete/$', PositionDeleteView.as_view(), name='delete_position' ),
    
    url(r'^positions/(?P<pk>\d+)/add_employee/$', AddEmployeePositionView.as_view(), name='add_employeeposition' ),
    ##################################
        
    ##################################
    # Employee Skills 
    url(r'^employee_skills/$', EmployeeSkillsListView.as_view(), name='employee_skills_list'),
    url(r'^employee_skills/(?P<pk>\d+)/$', EmployeeSkillDetailView.as_view(), name='employee_skills_detail' ),
    url(r'^employee_skills/create/$', EmployeeSkillCreateView.as_view(), name='create_employee_skills' ),
    url(r'^employee_skills/(?P<pk>\d+)/update/$', EmployeeSkillUpdateView.as_view(), name='update_employee_skills' ),
    url(r'^employee_skills/(?P<pk>\d+)/delete/$', EmployeeSkillDeleteView.as_view(), name='delete_employee_skills' ),
    ##################################
    
    ##################################
    # job profile Skills 
    url(r'^job_profile_skills/$', JobProfileSkillsListView.as_view(), name='job_profile_skills_list'),
    url(r'^job_profile_skills/(?P<pk>\d+)/$', JobProfileSkillDetailView.as_view(), name='job_profile_skill_detail'),
    url(r'^job_profile_skills/create/$', JobProfileSkillCreateView.as_view(), name='create_job_profile_skill'),
    url(r'^job_profile_skills/(?P<pk>\d+)/update/$', JobProfileSkillUpdateView.as_view(), name='update_job_profile_skill'),
    url(r'^job_profile_skills/(?P<pk>\d+)/delete/$', JobProfileSkillDeleteView.as_view(), name='delete_job_profile_skill'),
    ##################################
    
    ##################################
    # Employee Positions 
    url(r'^employee_positions/$', EmployeePositionsListView.as_view(), name='employee_positions_list'),
    url(r'^employee_positions/(?P<pk>\d+)/$', EmployeePositionDetailView.as_view(), name='employee_position_detail' ),
    url(r'^employee_positions/create/$', EmployeePositionCreateView.as_view(), name='create_employee_position' ),
    url(r'^employee_positions/(?P<pk>\d+)/update/$', EmployeePositionUpdateView.as_view(), name='update_employee_position' ),
    url(r'^employee_positions/(?P<pk>\d+)/delete/$', EmployeePositionDeleteView.as_view(), name='delete_employee_position' ),
    ##################################
    
)