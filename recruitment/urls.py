from django.conf.urls import patterns,url

from recruitment.views import ApplicantListView, ApplicantDetailView, ApplicantCreateView

urlpatterns = patterns('',
    
    url(r'^applicants/$', ApplicantListView.as_view(), name='applicants_list'),
    url(r'^applicant/(?P<pk>\d+)/', ApplicantDetailView.as_view(), name='applicant_detail'),
    url(r'^applicant/create/$',ApplicantCreateView.as_view(),name='create_applicant'),
    )