from django.views.generic import TemplateView
from guardian.shortcuts import get_objects_for_user

from users.models import Employee
from services.models import Domain, ServiceFamily, Service
from projects.models import Project, Deliverable

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
    
    