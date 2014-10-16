# Create your views here.
from django.views.generic import ListView, DetailView

from services.models import Domain, ServiceFamily, Service

class DomainsReportView(ListView):
    
    template_name="domains_report.html"
    model = Domain    
    
    
class DomainReportView(DetailView):
    
    template_name="domain_report.html"
    model = Domain

    
class ServiceFamilyReportView(DetailView):
    
    template_name="servicefamily_report.html"
    model = ServiceFamily
    

class ServiceReportView(DetailView):
    
    template_name="service_report.html"
    model = Service
    

class ServicesReportView(ListView):
    
    template_name="service_report.html"
    model = Service