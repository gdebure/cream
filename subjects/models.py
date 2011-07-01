from django.db import models
from projects.models import Project

class SubjectFamily (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
        

class Subject (models.Model):
    
    name = models.CharField(max_length=64)
    subject_family = models.ForeignKey(SubjectFamily)
    description = models.TextField()
    project = models.ManyToManyField(Project)
    
    def __unicode__(self):
        return self.subject_family.name + " " + self.name
