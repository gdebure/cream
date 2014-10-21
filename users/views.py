from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from core.views import LoginRequiredMixin, PermissionRequiredMixin

from users.models import Employee
from qualifications.models import EmployeePosition


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