from django.db import models
from django import forms

from django.contrib.auth.models import User

class Profile (models.Model):
    '''A Class to handle user profiles'''
    
    id = models.CharField(max_length=1,primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
    
    
    
class Employee (models.Model):
    '''A class to handle employees'''
    
    user = models.ForeignKey(User, unique=True, null=True)
    siglum = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.user.last_name + " " + self.user.first_name

    def get_absolute_url(self):
        return "/users/employees/" + str(self.id)

    def get_skills(self):
        return self.employeeskill_set.all()
    
    
