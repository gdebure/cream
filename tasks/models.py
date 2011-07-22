from django.db import models
from django import forms

from users.models import Employee
from projects.models import Deliverable
from subjects.models import Subject

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
    creator = models.ForeignKey(Employee, related_name='creator')
    deliverable = models.ForeignKey(Deliverable)
    subject = models.ManyToManyField(Subject)
    
    
    # Answer information
    answer = models.TextField(null=True)
    close_date = models.DateField(null=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    reject_reason = models.CharField(max_length=64)
    time_spent = models.DecimalField(max_digits=5,decimal_places=2)
    owner = models.ManyToManyField(Employee, related_name='owner')
    
    def __unicode__(self):
        return str(self.id) + ":" + self.name
        
        
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        
        
class Comment (models.Model):
    
    task = models.ForeignKey(Task)
    date = models.DateField()
    user = models.ForeignKey(Employee, related_name='comment_user')
    description = models.TextField()
    file = models.FileField(upload_to='comments')
    
    def __unicode__(self):
        return str(self.id)
    