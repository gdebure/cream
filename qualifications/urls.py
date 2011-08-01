from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from qualifications.models import Skill
from qualifications.forms import SkillForm

urlpatterns = patterns('',
    ##################################
    # Skills 
    (r'^skills/$', ListView.as_view( queryset=Skill.objects.order_by('name'), context_object_name='skills_list', ), ),
    (r'^skills/(?P<pk>\d+)/$', DetailView.as_view( model=Skill, ), ),
    (r'^skills/(?P<pk>\d+)/update/$', UpdateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s' ), ),
    (r'^skills/create/$', CreateView.as_view( model=Skill, success_url='/qualifications/skills/%(id)s' ), ),
    ##################################
    
    
)