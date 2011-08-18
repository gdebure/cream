# -*- coding: utf-8 -*-
from django.db import models

from services.models import Service
from users.models import Employee 


class Project (models.Model):
    '''A class to handle projects'''
    
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    customer_name = models.CharField(max_length=128, null=True)
    customer_siglum = models.CharField(max_length=16, null=True)
    wiki_link = models.URLField(null=True)
    
    def __unicode__(self):
        return self.number + ": " + self.name
        
    def get_absolute_url(self):
        return "/projects/projects/" + str(self.id)
        
    def get_authorizations(self):
        return self.authorization_set.all()
        
    def get_deliverables(self):
        return self.deliverable_set.all()
        
    def get_turnover_values(self):
        return self.turnover_set.all()
        
    def get_tasks(self):
        tasks = list()
        for deliverable in self.get_deliverables():
            tasks += deliverable.task_set.all()
            
        return tasks

class Profile (models.Model):
    '''A Class to handle user profiles on a project'''
    
    id = models.CharField(max_length=1,primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
        
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/projects/profiles/" + str(self.id)
    

class Authorization (models.Model):
    employee = models.ForeignKey(Employee)
    project = models.ForeignKey(Project)
    profile = models.ForeignKey(Profile)
    
    class Meta:
        unique_together = ("employee","project")
        
    def __unicode__(self):
        return str(self.id)
        
    def get_absolute_url(self):
        return "/projects/authorizations/" + str(self.id)


class Turnover (models.Model):
    
    year = models.IntegerField()
    project = models.ForeignKey(Project)
    amount = models.IntegerField()
    
    def __unicode__(self):
        return self.project.name + ", " + str(self.year) + ", " + str(self.amount)
        
    def get_absolute_url(self):
        return "/projects/turnover_values/" + str(self.id)
        
        
class Deliverable (models.Model):
    
    SERVICE_OWNER_APPROVAL_CHOICES = (
        ('P','Pending'),
        ('A','Approved'),
        ('R','Rejected')
        )
    
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    description = models.TextField()
    estimated_volume = models.IntegerField()
    acceptance_criteria = models.TextField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="unit price (€)")
    unit_time = models.IntegerField(verbose_name="unit time (mn)")
    turnover = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="turnover (€)")
    approved_by_service_owner = models.CharField(max_length=1, choices=SERVICE_OWNER_APPROVAL_CHOICES)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/projects/deliverables/" + str(self.id)
        
        
class SubjectFamily (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/projects/subject_families/" + str(self.id)
        

class Subject (models.Model):
    
    name = models.CharField(max_length=64)
    subject_family = models.ForeignKey(SubjectFamily, on_delete=models.PROTECT)
    description = models.TextField()
    project = models.ManyToManyField(Project)
    
    def __unicode__(self):
        return self.subject_family.name + " " + self.name
        
    def get_absolute_url(self):
        return "/projects/subjects/" + str(self.id)


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
    #requestor_type = models.ForeignKey(RequestorType)
    creator = models.ForeignKey(Employee, related_name='creator')
    deliverable = models.ForeignKey(Deliverable, on_delete=models.PROTECT)
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
        
    def get_absolute_url(self):
        return "/projects/tasks/" + str(self.id)
        
    def get_subjects(self):
        return self.subject.all()
        
    def get_owners(self):
        return self.owner.all()
        