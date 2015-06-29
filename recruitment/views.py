from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from recruitment.models import Applicant, ApplicantPosition
from recruitment.models import Interview

from qualifications.models import Position

class ApplicantListView(ListView,LoginRequiredMixin):
    
    model = Applicant
    context_object_name='applicants_list'
    template_name='applicant_list.html'
    
class ApplicantDetailView(DetailView,LoginRequiredMixin):
    
    model = Applicant
    template_name='applicant_detail.html'
    
class ApplicantCreateView(CreateView,PermissionRequiredMixin):
    model = Applicant
    template_name='applicant_form.html'
    permission='recruitment.add_applicant'
    fields=['last_name','first_name','address','phone','email','first_contact','cv','comments']

    def get_success_url(self):
        return reverse_lazy('applicant_detail',args=[self.object.id])
    
class ApplicantUpdateView(UpdateView,PermissionRequiredMixin):
    model = Applicant
    template_name='applicant_form.html'
    permission='recruitment.add_applicant'
    fields=['last_name','first_name','address','phone','email','first_contact','cv','comments']

    def get_success_url(self):
        return reverse_lazy('applicant_detail',args=[self.object.id])
    
class ApplicantDeleteView(DeleteView):
    model = Applicant
    permission='recruitment.delete_applicant'
    template_name = 'applicant_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('applicants_list')




class ApplicantPositionListView(ListView,LoginRequiredMixin):
    
    model = ApplicantPosition
    context_object_name='applicantpositions_list'
    template_name='applicantposition_list.html'
    
class ApplicantPositionDetailView(DetailView,LoginRequiredMixin):
    
    model = ApplicantPosition
    template_name='applicantposition_detail.html'
    
class ApplicantPositionCreateView(CreateView,PermissionRequiredMixin):
    model = ApplicantPosition
    template_name='applicantposition_form.html'
    permission='recruitment.add_applicantposition'
    fields=['applicant','position','status','comments']

    def get_success_url(self):
        return reverse_lazy('applicantposition_detail',args=[self.object.id])
    
class ApplicantPositionUpdateView(UpdateView,PermissionRequiredMixin):
    model = ApplicantPosition
    template_name='applicantposition_form.html'
    permission='recruitment.add_applicantposition'
    fields=['applicant','position','status','comments']

    def get_success_url(self):
        return reverse_lazy('applicant_detail',args=[self.object.id])
    
class ApplicantPositionDeleteView(DeleteView):
    model = ApplicantPosition
    permission='recruitment.delete_applicantposition'
    template_name = 'applicantposition_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('applicantpositions_list')
    
class AddPositionFromApplicantView(ApplicantPositionCreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddPositionFromApplicantView,self).get_context_data(**kwargs)
        applicant = Applicant.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'applicant':applicant}
        return  context
    

class AddApplicantFromPositionView(ApplicantPositionCreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddApplicantFromPositionView,self).get_context_data(**kwargs)
        position = Position.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'position':position}
        return  context
    
    
    
class InterviewListView(ListView, PermissionRequiredMixin):
    model = Interview
    context_object_name='interviews_list'
    template_name='interview_list.html'
    permission='recruitment.add_interview'


class InterviewDetailView(DetailView,PermissionRequiredMixin):
    model = Interview
    template_name='interview_detail.html'
    permission='recruitment.add_interview'
    
    
class InterviewCreateView(CreateView, PermissionRequiredMixin):
    model = Interview
    template_name='interview_form.html'
    permission='recruitment.add_interview'
    fields=['applicant','type','date','interviewer','status','notes']
    
    def get_success_url(self):
        return reverse_lazy('interview_detail',args=[self.object.id])
    
class InterviewUpdateView(UpdateView, PermissionRequiredMixin):
    model = Interview
    template_name='interview_form.html'
    permission='recruitment.add_interview'
    fields=['applicant','type','date','interviewer','status','notes']
    
    def get_success_url(self):
        return reverse_lazy('interview_detail',args=[self.object.id])
    
class InterviewDeleteView(DeleteView):
    model = Interview
    permission='recruitment.delete_interview'
    template_name = 'interview_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('interviews_list')
    
    
class AddInterviewFromApplicantView(InterviewCreateView):
    
    def get_context_data(self, **kwargs):
        context = super(AddInterviewFromApplicantView,self).get_context_data(**kwargs)
        applicant = Applicant.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'applicant':applicant}
        return  context