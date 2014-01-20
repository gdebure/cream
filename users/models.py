from django.db import models
from django import forms

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
class Employee (models.Model):
    '''A class to handle employees'''
    
    user = models.ForeignKey(User, unique=True, null=True)
    siglum = models.CharField(max_length=16)
    
    class Meta:
        ordering = ['user__last_name']
    
    def __unicode__(self):
        return self.user.last_name + " " + self.user.first_name

    def get_absolute_url(self):
        return reverse('employee',kwargs={'pk':self.id})
    
