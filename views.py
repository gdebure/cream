from django.views.generic.simple import direct_to_template
from guardian.shortcuts import get_objects_for_user

from services.models import Domain, ServiceFamily, Service
from projects.models import Project, Deliverable

def home_view(request):
    
    count_domains = Domain.objects.count()
    count_servicefamilies = ServiceFamily.objects.count()
    count_services = Service.objects.count()
    
    count_projects = Project.objects.count()
    count_deliverables = Deliverable.objects.count()
    
    user_services = Service.objects.filter(owner=request.user)
    deliverables_pending = Deliverable.objects.filter(approved_by_service_owner='p')
    user_pending_deliverables = deliverables_pending.filter(service__in=user_services)
    
    user_projects = Project.objects.filter(project_leader=request.user)
    
    deliverables_rejected = Deliverable.objects.filter(approved_by_service_owner='r')
    user_rejected_deliverables = deliverables_rejected.filter(project__in=user_projects)
    
    return direct_to_template(request, template="home.html", extra_context={
        'count_domains':count_domains,
        'count_servicefamilies':count_servicefamilies,
        'count_services':count_services,
        'count_projects':count_projects,
        'count_deliverables':count_deliverables,
        'user_services':user_services,
        'user_pending_deliverables':user_pending_deliverables,
        'user_rejected_deliverables':user_rejected_deliverables,
        'user_projects':user_projects,
        })