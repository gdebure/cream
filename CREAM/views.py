from django.views.generic import TemplateView
from django.db.models import Count

from guardian.shortcuts import get_objects_for_user

from users.models import Employee, EmployeeStatus
from services.models import Domain, ServiceFamily, Service
from projects.models import Project, Deliverable

from qualifications.models import Position
from users.models import Employee

class HomeView(TemplateView):
    
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(HomeView,self).get_context_data(**kwargs)

        context['current_employee'] = Employee.objects.get(user=self.request.user.id)

        context['count_domains'] = Domain.objects.count()
        context['count_servicefamilies'] = ServiceFamily.objects.count()
        context['count_services'] = Service.objects.count()

        context['count_projects'] = Project.objects.count()
        context['count_deliverables'] = Deliverable.objects.count()

        context['user_services'] = Service.objects.filter(owner=context['current_employee'])
        
        context['user_projects'] = Project.objects.filter(project_leader=context['current_employee'])

        return context
    
    
class DashboardView(TemplateView):
    
    template_name = "dashboard.html"
    
    def get_context_data(self,**kwargs):
        
        context = super(DashboardView,self).get_context_data(**kwargs)
        
        context.update(self.get_positions())
        context.update(self.get_intercontracts())
        context.update(self.get_services())
        context.update(self.get_employeestatus_count())
        
        return context
        
    def get_services(self, **kwargs):
        
        context = dict()
        
        context['count_domains'] = Domain.objects.count()
        context['count_servicefamilies'] = ServiceFamily.objects.count()
        context['count_services'] = Service.objects.count()

        return context
        
    def get_positions(self):
        
        return {'positions_list':Position.objects.exclude(status='S').exclude(status='C')}
        
    def get_intercontracts(self):
        
        return {'employees_list':Employee.objects.filter(status='I')}
    
    def get_employeestatus_count(self):
        
        result = EmployeeStatus.objects.annotate(count=Count('employee'))
        print result
        return {'employee_status':result}
    