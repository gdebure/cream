from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

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
    success_url='/users/employees/%(id)s'
    template_name='employee_form.html'
    permission='users.add_employee'
    

class EmployeeUpdateView(UpdateView,PermissionRequiredMixin):
    model = Employee
    success_url='/users/employees/%(id)s'
    template_name='employee_form.html' 
    permission = 'users.change_employee'
    

class EmployeeDeleteView(DeleteView,PermissionRequiredMixin):
    model=Employee
    success_url='/users/employees/'
    template_name='employee_confirm_delete.html' 
    permission='users.add_employee'


class AddPositionToEmployeeView(CreateView,PermissionRequiredMixin):
    model=EmployeePosition
    success_url='/users/employees/%(id)s'
    template_name='employeeposition_form.html'
    permission='qualifications.add_employeeposition'
    
    def get_context_data(self, **kwargs):
        context = super(AddPositionToEmployeeView,self).get_context_data(**kwargs)
        employee = Employee.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'employee':employee}
        return context