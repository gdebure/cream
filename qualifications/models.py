from django.db import models


class SkillCategory (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name



class Skill (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(SkillCategory)
    
    def __unicode__(self):
        return self.name
        
