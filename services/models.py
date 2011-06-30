from django.db import models
from users.models import User


class Domain (models.Model):
    
    name = models.CharField(max_length=64)
    is_active = models.BooleanField()
    owner = models.ForeignKey(User)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name
        

        
class ServiceFamily (models.Model):
    
    SERVICE_POSITION_CHOICES = (
        ('L','Leader'),
        ('C','Challenger'),
        ('F','Follower'),
        ('N','Nicher'),
    )
    
    SERVICE_LIFECYCLE_CHOICES = (
        ('I','Introduction'),
        ('G','Growth'),
        ('M','Maturity'),
        ('D','Decrease'),
    )
    
    name = models.CharField(max_length=128)
    domain = models.ForeignKey(Domain)
    description = models.TextField(null=True)
    focal_user = models.ForeignKey(User)
    growth_potential = models.DecimalField(max_digits=2,decimal_places=0)
    is_active = models.BooleanField()
    service_position = models.CharField(max_length=1,choices=SERVICE_POSITION_CHOICES)
    trend = models.IntegerField()
    service_lifecycle = models.CharField(max_length=1, choices=SERVICE_LIFECYCLE_CHOICES)