from django.db import models
from users.models import Employee
import reversion


class Domain (models.Model):
    '''A class to handle the domain for services'''
    name = models.CharField(max_length=64, verbose_name="domain name")
    is_active = models.BooleanField(verbose_name="domaine is active")
    owner = models.ForeignKey(Employee, verbose_name="domain owner")
    description = models.TextField(null=True)
    
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return '/services/domains/' + str(self.id)
    
    def get_report_url(self):
        return '/services/reports/domains/' + str(self.id)
        
    def get_service_families(self):
        return self.servicefamily_set.all()
        
    def get_turnover(self):
        service_families = self.get_service_families()
        turnover = 0
        for service_family in service_families:
            turnover += service_family.get_turnover()
        return turnover
        
    def get_turnover_year(self,year):
        service_families = self.get_service_families()
        turnover = 0
        for service_family in service_families:
            turnover += service_family.get_turnover_year(year)
        return turnover
        
# Register this object in reversion, so that we can track its history
reversion.register(Domain)

        
class ServiceFamily (models.Model):
    
    # Possible choices for Service Position
    SERVICE_POSITION_CHOICES = (
        ('L','Leader'),
        ('C','Challenger'),
        ('F','Follower'),
        ('N','Nicher'),
    )
    
    # Possible choices for Service Lifecycle
    SERVICE_LIFECYCLE_CHOICES = (
        ('I','Introduction'),
        ('G','Growth'),
        ('M','Maturity'),
        ('S','Saturation'),
        ('D','Decline'),
    )
    
    TREND_CHOICES = (
        ('I', 'Increasing'),
        ('S', 'Stable'),
        ('D', 'Decreasing'),
    )
    
    name = models.CharField(max_length=128, verbose_name="service family name")
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT, verbose_name="domain")
    description = models.TextField(null=True)
    owner = models.ForeignKey(Employee, null=True, blank=True, verbose_name="service family owner")
    growth_potential = models.DecimalField(max_digits=2,decimal_places=0, verbose_name='growth potential in %',null=True, blank=True)
    is_active = models.BooleanField()
    service_position = models.CharField(max_length=1,choices=SERVICE_POSITION_CHOICES,null=True, blank=True, verbose_name='service family market position')
    trend = models.CharField(max_length=1, choices=TREND_CHOICES,null=True, blank=True, verbose_name='service family market trend')
    service_lifecycle = models.CharField(max_length=1, choices=SERVICE_LIFECYCLE_CHOICES,null=True, blank=True, verbose_name='service family lifecycle')
    
    class Meta:
        ordering = ['domain','name']
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return '/services/service_families/' + str(self.id)
        
    def get_report_url(self):
        return '/services/reports/service_families/' + str(self.id)
        
    def get_services(self):
        return self.service_set.all()
        
    def get_turnover(self):
        services = self.get_services()
        turnover = 0
        for service in services:
            turnover += service.get_turnover()
        return turnover
        
    def get_turnover_year(self,year):
        services = self.get_services()
        turnover = 0
        for service in services:
            turnover += service.get_turnover_year(year)
        return turnover
        
# Register this object in reversion, so that we can track its history
reversion.register(ServiceFamily)
        

class Service (models.Model):
    
    name = models.CharField(max_length=128, unique=True, verbose_name="service name")
    service_family = models.ForeignKey(ServiceFamily,on_delete=models.PROTECT)
    is_active = models.BooleanField()
    owner = models.ForeignKey(Employee, null=True, blank=True, verbose_name='service owner')
    description = models.TextField(null=True)
    
    class Meta:
        ordering = ['service_family__name','name']
    
    def __unicode__(self):
        return self.service_family.name + " : " + self.name
        
    def get_absolute_url(self):
        return '/services/services/' + str(self.id)
        
    def get_report_url(self):
        return '/services/reports/services/' + str(self.id)
        
    def get_deliverables(self):
        return self.deliverable_set.all()
        
    def get_turnover(self):
        deliverables = self.get_deliverables()
        turnover = 0
        for deliverable in deliverables:
            turnover += deliverable.get_turnover()
        return turnover
        
    def get_turnover_year(self,year):
        deliverables = self.get_deliverables()
        turnover = 0
        for deliverable in deliverables:
            turnover += deliverable.get_turnover_year(year)
        return turnover
        
# Register this object in reversion, so that we can track its history
reversion.register(Service)