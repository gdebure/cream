from django.db import models
from django import forms

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

EMPLOYEE_STATUS_CHOICE=(
    ('I','Intercontract'),
    ('S','Structure'),
    ('P','On Project'),
    )    

class EmployeeStatus(models.Model):
    '''Indicates the status of an Employee'''
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    css_class = models.CharField(max_length=64)
    
    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name

    
class Employee (models.Model):
    '''A class to handle employees'''
    
    user = models.OneToOneField(User)
    siglum = models.CharField(max_length=16)
    status = models.CharField(max_length=1,choices=EMPLOYEE_STATUS_CHOICE)
    category = models.CharField(max_length=1, null=True, blank=True)
    
    class Meta:
        ordering = ['user__last_name']
    
    def __unicode__(self):
        return self.user.last_name + " " + self.user.first_name
    
    def get_picture(self):
        return ''

