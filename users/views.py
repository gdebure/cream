from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from users.models import Employee, EmployeeStatus
from qualifications.models import EmployeePosition


class EmployeeListView(ListView,LoginRequiredMixin):
    model=Employee
    context_object_name='employees_list'
    template_name='employee_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(EmployeeListView,self).get_context_data(**kwargs)
        context['viewing'] = "all"
        context['employeestatus_list'] = EmployeeStatus.objects.all()
        return  context

class FilteredEmployeeListView(EmployeeListView):
    
    def get_queryset(self):
        employee_status = self.kwargs['filter']
        return self.model.objects.filter(status__name=employee_status)

    def get_context_data(self, **kwargs):
        context = super(FilteredEmployeeListView,self).get_context_data(**kwargs)
        context['viewing'] = self.kwargs['filter']
        context['employeestatus_list'] = EmployeeStatus.objects.all()
        return  context
    

class EmployeeDetailView(DetailView,LoginRequiredMixin):
    model = Employee
    template_name='employee_detail.html'


class EmployeeCreateView(CreateView,PermissionRequiredMixin):
    model=Employee
    template_name='employee_form.html'
    permission='users.add_employee'
    fields=['user','siglum','location','status','category']

    def get_success_url(self):
        return reverse_lazy('employee',args=[self.object.id])


class EmployeeUpdateView(UpdateView,PermissionRequiredMixin):
    model = Employee
    template_name='employee_form.html'
    permission = 'users.change_employee'
    fields=['user','siglum','location','status','category']

    def get_success_url(self):
        return reverse_lazy('employee',args=[self.object.id])


class EmployeeDeleteView(DeleteView,PermissionRequiredMixin):
    model=Employee
    template_name='employee_confirm_delete.html'
    permission='users.add_employee'

    def get_success_url(self):
        return reverse_lazy('employees_list')
