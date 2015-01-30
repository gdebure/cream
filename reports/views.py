from django.views.generic import ListView, DetailView

from services.models import Domain, ServiceFamily, Service

class DonutChart(object):
    
    def set_chart(self,x_data,y_data):
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
                'donut': True,
                'donutRatio': 0.55,
            }
        }
        return data
    

class DomainsReportView(ListView):
    
    template_name="domains_report.html"
    model = Domain
    
class DomainsChartView(ListView,DonutChart):
    
    template_name = "domains_report.html"
    model = Domain
    
    def get_context_data(self, **kwargs):
        
        context = super(DomainsChartView,self).get_context_data(**kwargs)
        
        x_data = []
        y_data = []
        total_turnover = 0
        
        for domain in context['domain_list']:
            x_data.append(str(domain))
            y_data.append(float(domain.get_turnover()))
            total_turnover += domain.get_turnover()
            
        data = self.set_chart(x_data,y_data)
        
        context.update(data)
        context['total_turnover'] = total_turnover
        return context
    
class DomainReportView(DetailView, DonutChart):
    
    template_name="domain_report.html"
    model = Domain
    
    def get_context_data(self, **kwargs):
        
        context = super(DomainReportView,self).get_context_data(**kwargs)
        
        x_data = []
        y_data = []
        total_turnover = 0
        
        domain = self.object
        
        for service_family in domain.get_service_families():
            x_data.append(str(service_family))
            y_data.append(float(service_family.get_turnover()))
            total_turnover += service_family.get_turnover()
            
        data = self.set_chart(x_data,y_data)
        
        context.update(data)
        context['total_turnover'] = total_turnover
        return context

    
class ServiceFamilyReportView(DetailView,DonutChart):
    
    template_name="servicefamily_report.html"
    model = ServiceFamily
    
    def get_context_data(self, **kwargs):
        
        context = super(ServiceFamilyReportView,self).get_context_data(**kwargs)
        
        x_data = []
        y_data = []
        total_turnover = 0
        
        servicefamily = self.object
        
        for service in servicefamily.get_services():
            x_data.append(str(service))
            y_data.append(float(service.get_turnover()))
            total_turnover += service.get_turnover()
            
        data = self.set_chart(x_data,y_data)
        
        context.update(data)
        context['total_turnover'] = total_turnover
        return context
    

class ServiceReportView(DetailView,DonutChart):
    
    template_name="service_report.html"
    model = Service
    
    def get_context_data(self, **kwargs):
        
        context = super(ServiceReportView,self).get_context_data(**kwargs)
        
        x_data = []
        y_data = []
        total_turnover = 0
        
        service = self.object
        
        for deliverable in service.get_deliverables():
            x_data.append(str(deliverable))
            y_data.append(float(deliverable.get_turnover()))
            total_turnover += deliverable.get_turnover()
            
        data = self.set_chart(x_data,y_data)
        
        context.update(data)
        context['total_turnover'] = total_turnover
        return context

    

class ServicesReportView(ListView):
    
    template_name="service_report.html"
    model = Service