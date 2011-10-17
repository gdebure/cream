from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group

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
        
    def get_service_families(self):
        return self.servicefamily_set.all()
        
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
        
    def get_services(self):
        return self.service_set.all()
        
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
        
    def get_deliverables(self):
        return self.deliverable_set.all()
        
# Register this object in reversion, so that we can track its history
reversion.register(Service)



@receiver(post_save,sender=Domain)
@receiver(post_save,sender=Service)
@receiver(post_save,sender=ServiceFamily)
def send_mail_on_save(sender, **kwargs):
    
    # This is the list of users that will receive the email
    recipients = User.objects.filter(groups__name='Service Catalog Admins').values_list('email',flat=True)
    # Get the object instance
    instance = kwargs['instance']
    
    # Get the latest two version for comparison:
    instance_versions = reversion.get_for_object(instance)
    old_version = instance_versions[0]
    new_version = instance
    
    mail_body = "\n"
    for field in old_version.field_dict:
        old_object_value = old_version.field_dict[field]
        new_object_value = instance.__getattribute__(field)
        if old_object_value != new_object_value:
            mail_body += "\n" + field + ":\n"
            mail_body += "----------------\n"
            mail_body += "* old: " + str(old_object_value) + "\n"
            mail_body += "* new: " + str(new_object_value) + "\n"
    
    mail_body += "\n\nThis is an automatically generated email, please do not reply"
    
    mail_title = str(sender._meta.verbose_name)+ " " + str(instance) + " updated"
    send_mail(mail_title, mail_body, 'creamrobot@cimpa.com', recipients, fail_silently=False)