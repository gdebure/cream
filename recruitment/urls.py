from django.conf.urls import url

from recruitment.views import ApplicantListView, ApplicantDetailView, ApplicantCreateView, ApplicantUpdateView, ApplicantDeleteView, AddPositionFromApplicantView
from recruitment.views import ApplicantPositionListView, ApplicantPositionDetailView, ApplicantPositionCreateView, ApplicantPositionUpdateView, ApplicantPositionDeleteView
from recruitment.views import InterviewListView, InterviewDetailView, InterviewCreateView,InterviewUpdateView, InterviewDeleteView, AddInterviewFromApplicantView

urlpatterns = [
    
    url(r'^applicants/$', ApplicantListView.as_view(), name='applicants_list'),
    url(r'^applicants/(?P<pk>\d+)/$', ApplicantDetailView.as_view(), name='applicant_detail'),
    url(r'^applicants/create/$',ApplicantCreateView.as_view(),name='create_applicant'),
    url(r'^applicants/(?P<pk>\d+)/update/$',ApplicantUpdateView.as_view(),name='update_applicant'),
    url(r'^applicants/(?P<pk>\d+)/delete/$',ApplicantDeleteView.as_view(),name='delete_applicant'),
    url(r'^applicants/(?P<pk>\d+)/add_position/$', AddPositionFromApplicantView.as_view(), name='add_positionfromapplicant' ),
    url(r'^applicants/(?P<pk>\d+)/add_interview/$', AddInterviewFromApplicantView.as_view(), name='add_interviewfromapplicant' ),
    
    url(r'^applicantpositions/$', ApplicantPositionListView.as_view(), name='applicantpositions_list'),
    url(r'^applicantpositions/(?P<pk>\d+)/$', ApplicantPositionDetailView.as_view(), name='applicantposition_detail'),
    url(r'^applicantpositions/create/$',ApplicantPositionCreateView.as_view(),name='create_applicantposition'),
    url(r'^applicantpositions/(?P<pk>\d+)/update/$',ApplicantPositionUpdateView.as_view(),name='update_applicantposition'),
    url(r'^applicantpositions/(?P<pk>\d+)/delete/$',ApplicantPositionDeleteView.as_view(),name='delete_applicantposition'),
    
    url(r'^interviews/$', InterviewListView.as_view(), name='interviews_list'),
    url(r'^interviews/(?P<pk>\d+)/$', InterviewDetailView.as_view(), name='interview_detail'),
    url(r'^interviews/create/$', InterviewCreateView.as_view(), name='create_interview'),
    url(r'^interviews/(?P<pk>\d+)/update/$', InterviewUpdateView.as_view(), name='update_interview'),
    url(r'^interviews/(?P<pk>\d+)/delete/$', InterviewDeleteView.as_view(), name='delete_interview'),
    ]