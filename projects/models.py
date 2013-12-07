# -*- coding: utf-8 -*-
from datetime import date

from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

import reversion

from users.models import Employee
from services.models import Service

class Project (models.Model):
    '''A class to handle projects'''
    
    NATCO_CHOICES = (
        ('D','CIMPA GmbH'),
        ('F','CIMPA SAS'),
        ('U','CIMPA Ltd'),
        )
    
    name = models.CharField(max_length=64, verbose_name="project name")
    number = models.CharField(max_length=32, unique=True, verbose_name="project number")
    description = models.TextField()
    date_start = models.DateField(null=True, blank=True, verbose_name="project start date", help_text='YYYY-MM-DD' )
    date_end = models.DateField(null=True, blank=True, verbose_name="project end date", help_text='YYYY-MM-DD' )
    customer_name = models.CharField(max_length=128, null=True, blank=True)
    customer_siglum = models.CharField(max_length=16, null=True, blank=True)
    wiki_link = models.URLField(null=True, blank=True)
    project_leader = models.ForeignKey(Employee, null=True, blank=True, related_name="project_leader")
    department = models.CharField(max_length=2,null=True, blank=True, verbose_name="CIMPA department")
    natco = models.CharField(max_length=2, choices=NATCO_CHOICES, verbose_name="turnover allocation natco", null=True, blank=True)
    
    class Meta:
        ordering = ["number", "name"]
        
    
    def __unicode__(self):
        return self.number + ": " + self.name
        
    def get_authorizations(self):
        return self.authorization_set.all()
        
    def get_deliverables(self):
        return self.deliverable_set.all()
        
    def get_tasks(self):
        tasks = list()
        for deliverable in self.get_deliverables():
            tasks += deliverable.task_set.all()
            
        return tasks
    
    def get_absolute_url(self):
        return reverse('project',kwargs={'pk':self.id})
        
    def get_total_turnover(self):
        turnover = 0
        for deliverable in self.deliverable_set.all():
            turnover += deliverable.get_turnover()
        return turnover
        
    def get_turnover_per_year(self):
        year_min = self.date_start.year
        year_max = self.date_end.year
        turnover = dict()
        for year in range(year_min,year_max+1):
            year_turnover = 0
            for deliverable in self.deliverable_set.all():
                year_turnover += deliverable.get_turnover_year(year)
            turnover[year] = year_turnover
        return turnover

# Register this object in reversion, so that we can track its history
#reversion.register(Project)




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
    acceptance_criteria = models.TextField(null=True, blank=True)
    unit_time = models.IntegerField(verbose_name="unit time (mn)", null=True, blank=True, editable=False, validators=[validate_positive]) # Unit time is not used for the moment
    turnover = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="turnover (€)", null=True, blank=True, editable=False, validators=[validate_positive]) # FIXME: Turnover will be computed, to be removed from datamodel
    
    class Meta:
        ordering = ['project','code','name']
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('deliverable', kwargs={'pk':self.id})
        
    def get_tasks(self):
        return self.task_set.all()
        
    def get_turnover(self):
        turnover = 0
        for volume in self.deliverablevolume_set.all():
            if volume.quantity != None and volume.unit_price != None:
                turnover += volume.quantity * volume.unit_price
        return turnover
        

    def get_turnover_year(self,year):
        
        date_start = date(year,01,01).toordinal()
        date_end = date(year,12,31).toordinal()
        year_range = range(date_start,date_end+1)
        days_year = len(year_range)
        
        year_turnover = 0
        
        for volume in self.get_volumes():
            date_volume_start = volume.date_start.toordinal()
            date_volume_end = volume.date_end.toordinal()
            volume_range = range(date_volume_start,date_volume_end+1)
            days_volume = len(volume_range)
            
            intersect = list(set(volume_range) & set(year_range))
            days_intersect = len(intersect)
            
            volume_price = round((volume.get_total_price()/days_volume)*days_intersect,2)
            
            year_turnover += volume_price
            
        return year_turnover


    def get_volumes(self):
        return self.deliverablevolume_set.all()
        
    def get_total_volume(self):
        volumes = self.get_volumes()
        total = 0
        for volume in volumes:
            total += volume.quantity
        return total
        
# Register this object in reversion, so that we can track its history
reversion.register(Deliverable)



class DeliverableVolume(models.Model):

    deliverable = models.ForeignKey(Deliverable)
    date_start = models.DateField(help_text='YYYY-MM-DD')
    date_end = models.DateField(help_text='YYYY-MM-DD')
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['deliverable','date_start']
        
    def __unicode__(self):
        return self.deliverable.name+ ' : ' + str(self.date_start) + " : " + str(self.date_end) + " : " + str(self.quantity)
        
    def get_absolute_url(self):
        return reverse('deliverablevolume', kwargs={'pk':self.id})
        
    def get_total_price(self):
        return self.quantity * self.unit_price

# Register this object in reversion, so that we can track its history
reversion.register(DeliverableVolume)


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
        ('P','In Progress'),
        ('C','Closed'),
        ('X','Cancelled'),
    )
    
    # Base information
    name = models.CharField(max_length=128)
    open_date = models.DateField()
    criticity = models.CharField(max_length=1,choices=CRITICITY_CHOICES)
    description = models.TextField()
    requestor = models.CharField(max_length=64)
    creator = models.ForeignKey(Employee, related_name='creator')
    deliverable = models.ForeignKey(Deliverable, on_delete=models.PROTECT)
    subject = models.ManyToManyField(Subject)
        
    # Answer information
    answer = models.TextField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default='O')
    reject_reason = models.CharField(max_length=64,null=True, blank=True)
    time_spent = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True, help_text="hours")
    owner = models.ManyToManyField(Employee, related_name='owner',null=True, blank=True)
    number_of_units = models.IntegerField(default=1)
    
    class Meta:
        ordering = ['-id'] # Sort per id (descending)
    
    def __unicode__(self):
        return str(self.id) + ":" + self.name
        
    def get_absolute_url(self):
        return "/projects/tasks/" + str(self.id)
        
    def get_subjects(self):
        return self.subject.all()
        
    def get_owners(self):
        return self.owner.all()
        
       