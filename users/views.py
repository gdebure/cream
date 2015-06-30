from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from users.models import Employee
from qualifications.models import EmployeePosition


class EmployeeListView(ListView,LoginRequiredMixin):
    model=Employee
    context_object_name='employees_list'
    template_name='employee_list.html'


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
