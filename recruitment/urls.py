from django.conf.urls import patterns,url

from recruitment.views import ApplicantListView, ApplicantDetailView, ApplicantCreateView, ApplicantUpdateView, ApplicantDeleteView, AddPositionFromApplicantView
from recruitment.views import ApplicantPositionListView, ApplicantPositionDetailView, ApplicantPositionCreateView, ApplicantPositionUpdateView, ApplicantPositionDeleteView
from recruitment.views import RecruitmentMeetingListView, RecruitmentMeetingDetailView, RecruitmentMeetingCreateView,RecruitmentMeetingUpdateView, RecruitmentMeetingDeleteView, AddRecruitmentMeetingFromApplicantView

urlpatterns = patterns('',
    
    url(r'^applicants/$', ApplicantListView.as_view(), name='applicants_list'),
    url(r'^applicants/(?P<pk>\d+)/$', ApplicantDetailView.as_view(), name='applicant_detail'),
    url(r'^applicants/create/$',ApplicantCreateView.as_view(),name='create_applicant'),
    url(r'^applicants/(?P<pk>\d+)/update/$',ApplicantUpdateView.as_view(),name='update_applicant'),
    url(r'^applicants/(?P<pk>\d+)/delete/$',ApplicantDeleteView.as_view(),name='delete_applicant'),
    url(r'^applicants/(?P<pk>\d+)/add_position/$', AddPositionFromApplicantView.as_view(), name='add_positionfromapplicant' ),
    url(r'^applicants/(?P<pk>\d+)/add_recruitmentmeeting/$', AddRecruitmentMeetingFromApplicantView.as_view(), name='add_recruitmentmeetingfromapplicant' ),
    
    url(r'^applicantpositions/$', ApplicantPositionListView.as_view(), name='applicantpositions_list'),
    url(r'^applicantpositions/(?P<pk>\d+)/$', ApplicantPositionDetailView.as_view(), name='applicantposition_detail'),
    url(r'^applicantpositions/create/$',ApplicantPositionCreateView.as_view(),name='create_applicantposition'),
    url(r'^applicantpositions/(?P<pk>\d+)/update/$',ApplicantPositionUpdateView.as_view(),name='update_applicantposition'),
    url(r'^applicantpositions/(?P<pk>\d+)/delete/$',ApplicantPositionDeleteView.as_view(),name='delete_applicantposition'),
    
    url(r'^recruitmentmeetings/$', RecruitmentMeetingListView.as_view(), name='recruitmentmeetings_list'),
    url(r'^recruitmentmeetings/(?P<pk>\d+)/$', RecruitmentMeetingDetailView.as_view(), name='recruitmentmeeting_detail'),
    url(r'^recruitmentmeetings/create/$', RecruitmentMeetingCreateView.as_view(), name='create_recruitmentmeeting'),
    url(r'^recruitmentmeetings/(?P<pk>\d+)/update/$', RecruitmentMeetingUpdateView.as_view(), name='update_recruitmentmeeting'),
    url(r'^recruitmentmeetings/(?P<pk>\d+)/delete/$', RecruitmentMeetingDeleteView.as_view(), name='delete_recruitmentmeeting'),
    )