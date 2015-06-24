from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from recruitment.models import Applicant, ApplicantPosition

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
        return reverse_lazy('applicants_list',args=[self.object.id])


