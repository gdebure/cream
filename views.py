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
    
    user_services = get_objects_for_user(request.user,'services.change_service')
    #deliverables_pending = Deliverable.objects.filter(approved_by_service_owner='p')
    #user_pending_deliverables = deliverables_pending.filter(service in user_services)
    
    
    return direct_to_template(request, template="home.html", extra_context={
        'count_domains':count_domains,
        'count_servicefamilies':count_servicefamilies,
        'count_services':count_services,
        'count_projects':count_projects,
        'count_deliverables':count_deliverables,
        #'user_pending_deliverables':user_pending_deliverables,
        })