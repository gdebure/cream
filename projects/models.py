# -*- coding: utf-8 -*-
from django.db import models

from services.models import Service
from users.models import Employee 


from django.core.exceptions import ValidationError

class Project (models.Model):
    '''A class to handle projects'''
    
    NATCO_CHOICES = (
        ('D','CIMPA GmbH'),
        ('F','CIMPA SAS'),
        ('U','CIMPA Ltd'),
        )
    
    name = models.CharField(max_length=64, verbose_name="project name")
    number = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    date_start = models.DateField(null=True, blank=True )
    date_end = models.DateField(null=True, blank=True)
    customer_name = models.CharField(max_length=128, null=True, blank=True)
    customer_siglum = models.CharField(max_length=16, null=True, blank=True)
    wiki_link = models.URLField(null=True, blank=True)
    project_leader = models.ForeignKey(Employee, null=True, blank=True, related_name="project_leader")
    department = models.CharField(max_length=2,null=True, blank=True)
    natco = models.CharField(max_length=2, choices=NATCO_CHOICES, verbose_name="turnover allocation natco", null=True, blank=True)
    
    class Meta:
        ordering = ["number", "name"]
    
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
    employee = models.ForeignKey(Employee, related_name="authorization_employee")
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
        

def validate_positive(value):
    if value < 0:
        raise ValidationError(u'%s is not a positive value !' % value)


class Deliverable (models.Model):
    
    SERVICE_OWNER_APPROVAL_CHOICES = (
        ('P','Pending'),
        ('A','Approved'),
        ('R','Rejected')
        )
    
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name="project name")
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True, blank=True, verbose_name="service family / service")
    code = models.CharField(max_length=32, null=True, blank=True, verbose_name="project deliverable identifier")
    name = models.CharField(max_length=128, verbose_name="project deliverable name")
    description = models.TextField()
    contractual_volume = models.IntegerField(null=True, blank=True, verbose_name="number of units", validators=[validate_positive])
    acceptance_criteria = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="unit price (€)",null=True, blank=True, validators=[validate_positive])
    unit_time = models.IntegerField(verbose_name="unit time (mn)", null=True, blank=True, editable=False, validators=[validate_positive]) # Unit time is not used for the moment
    turnover = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="turnover (€)", null=True, blank=True, editable=False, validators=[validate_positive]) # FIXME: Turnover will be computed, to be removed from datamodel
    approved_by_service_owner = models.CharField(max_length=1, choices=SERVICE_OWNER_APPROVAL_CHOICES, default="P")
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/projects/deliverables/" + str(self.id)
        
    def get_tasks(self):
        return self.task_set.all()
        
        
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
        