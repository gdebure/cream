from django.db import models
from users.models import Employee



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
        
    def get_service_families(self):
        return self.servicefamily_set.all()
        

        
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
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT, verbose_name="service family domain")
    description = models.TextField(null=True)
    focal_point = models.ForeignKey(Employee, null=True, blank=True)
    growth_potential = models.DecimalField(max_digits=2,decimal_places=0, verbose_name='Growth Potential in %',null=True, blank=True)
    is_active = models.BooleanField()
    service_position = models.CharField(max_length=1,choices=SERVICE_POSITION_CHOICES,null=True, blank=True)
    trend = models.CharField(max_length=1, choices=TREND_CHOICES,null=True, blank=True)
    service_lifecycle = models.CharField(max_length=1, choices=SERVICE_LIFECYCLE_CHOICES,null=True, blank=True)
    
    class Meta:
        ordering = ['domain','name']
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return '/services/service_families/' + str(self.id)
        
    def get_services(self):
        return self.service_set.all()
        
        

class Service (models.Model):
    
    name = models.CharField(max_length=128, unique=True, verbose_name="service name")
    service_family = models.ForeignKey(ServiceFamily,on_delete=models.PROTECT)
    is_active = models.BooleanField()
    owner = models.ForeignKey(Employee, null=True, blank=True)
    description = models.TextField(null=True)
    
    class Meta:
        ordering = ['service_family__name','name']
    
    def __unicode__(self):
        return self.service_family.name + " : " + self.name
        
    def get_absolute_url(self):
        return '/services/services/' + str(self.id)
        
    def get_deliverables(self):
        return self.deliverable_set.all()