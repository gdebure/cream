from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Profile (models.Model):
    '''A Class to handle user profiles'''
    
    id = models.CharField(max_length=1,primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
    
    
class Employee (models.Model):
    '''A class to handle employees'''
    
    user = models.ForeignKey(User, unique=True, null=True)
    siglum = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.user.last_name + " " + self.user.first_name
    
    
class Authorization (models.Model):
    employee = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    profile = models.ForeignKey(Profile)
    
    class Meta:
        unique_together = ("employee","project")