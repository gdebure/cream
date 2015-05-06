from django.db import models
from django import forms

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from CREAM.instance_settings import USER_PICTURE_BASE_URL, USER_PICTURE_FILE_EXTENSION

from core.models import Location

class EmployeeStatus(models.Model):
    '''Indicates the status of an Employee'''
    id = models.CharField(max_length=1,primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    css_class = models.CharField(max_length=64)
    
    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return unicode(self.name)


class Employee (models.Model):
    '''A class to handle employees'''
    
    user = models.OneToOneField(User)
    siglum = models.CharField(max_length=16)
    location = models.ForeignKey(Location)
    status = models.ForeignKey(EmployeeStatus)
    category = models.CharField(max_length=1, null=True, blank=True)

    
    class Meta:
        ordering = ['user__last_name']
    
    def __unicode__(self):
        return unicode(self.user.last_name) + " " + unicode(self.user.first_name)
    
    def get_picture(self):
        return USER_PICTURE_BASE_URL + '/' + str(self.user.username) + USER_PICTURE_FILE_EXTENSION

