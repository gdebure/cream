from django.db import models

from users.models import Employee


class SkillCategory (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
   
    class Meta:
        ordering = ['name']
   
    def __unicode__(self):
        return self.name





class Skill (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(SkillCategory)
    
    class Meta:
        ordering = ['category', 'name']
    
    def __unicode__(self):
        return self.category.name + ": " + self.name
        




class Job (models.Model):
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    skill = models.ManyToManyField(Skill)
    
    def __unicode__(self):
        return self.name
        
        


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee)
    skill = models.ForeignKey(Skill)
    level = models.IntegerField()
    
    class Meta:
        unique_together = ("employee", "skill")
    
    def __unicode__(self):
        return self.employee.name + " : " + self.skill.name + " : " + str(self.level)