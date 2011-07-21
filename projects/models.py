# -*- coding: utf-8 -*-
from django.db import models

from services.models import Service
from users.models import Employee, Profile

class Project (models.Model):
    '''A class to handle projects'''
    
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    customer_name = models.CharField(max_length=128, null=True)
    customer_siglum = models.CharField(max_length=16, null=True)
    wiki_link = models.CharField(max_length=255, null=True)
    
    def __unicode__(self):
        return self.number + ": " + self.name
        

class Authorization (models.Model):
    employee = models.ForeignKey(Employee)
    project = models.ForeignKey(Project)
    profile = models.ForeignKey(Profile)
    
    class Meta:
        unique_together = ("employee","project")
        
    def __unicode__(self):
        return str(self.id)


class Turnover (models.Model):
    
    year = models.IntegerField()
    project = models.ForeignKey(Project)
    amount = models.IntegerField()
    
    def __unicode__(self):
        return self.project.name + ", " + str(self.year) + ", " + str(self.amount)
        
        
class Deliverable (models.Model):
    
    project = models.ForeignKey(Project)
    service = models.ForeignKey(Service)
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    description = models.TextField()
    estimated_volume = models.IntegerField()
    acceptance_criteria = models.TextField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    unit_time = models.IntegerField()
    turnover = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __unicode__(self):
        return self.name