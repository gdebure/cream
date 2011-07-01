from django.db import models
from users.models import Employee
from projects.models import Deliverable

class RequestorType (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
        
        
class Task (models.Model):
    
    CRITICITY_CHOICES = (
        ('H','High'),
        ('L','Low'),
        ('M','Medium'),
    )
    
    STATUS_CHOICES = (
        ('O','Open'),
        ('C','Closed')
    )
    
    # Base information
    name = models.CharField(max_length=128)
    open_date = models.DateField()
    criticity = models.CharField(max_length=1,choices=CRITICITY_CHOICES)
    description = models.TextField()
    requestor = models.CharField(max_length=64)
    requestor_type = models.ForeignKey(RequestorType)
    creator = models.ForeignKey(Employee)
    deliverable = models.ForeignKey(Deliverable)
    
    # Answer information
    answer = models.TextField(null=True)
    close_date = models.DateField(null=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    reject_reason = models.CharField(max_length=64)
    time_spent = models.DecimalField(max_digits=5,decimal_places=2)
    
    
    def __unicode__(self):
        return str(self.id) + ":" + self.name
    