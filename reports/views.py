# Create your views here.
from django.views.generic import ListView, DetailView

from services.models import Domain, ServiceFamily, Service

class DomainsReportView(ListView):
    
    template_name="domains_report.html"
    model = Domain
    
class DomainsChartView(ListView):
    
    template_name = "domain_piechart.html"
    model = Domain
    
    def get_context_data(self, **kwargs):
        
        context = super(DomainsChartView,self).get_context_data(**kwargs)
        
        x_data = []
        y_data = []
        
        for domain in context['domain_list']:
            x_data.append(str(domain))
            y_data.append(domain.get_turnover())
            
        chartdata = {'x': x_data, 'y': y_data}
        charttype = "pieChart"
        chartcontainer = 'piechart_container'
        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': False,
            }
        }
        context.update(data)
        return context
    
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