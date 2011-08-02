from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


# The Qualifications app depends on the users app,
# we need to link against the Employee object
from users.models import Employee


class SkillCategory (models.Model):
    '''The SkillCategory object allows to categorize Skills (surprise !)'''
    
    name = models.CharField(max_length=64)
    description = models.TextField()
   
    class Meta:
        '''Default order is on name'''
        ordering = ['name']
   
    def __unicode__(self):
        '''Returns the name when printing object'''
        return self.name
        
    def get_skills(self):
        '''Returns the list of skills belonging to this category. This method
        is just for convenience'''
        return self.skill_set.all()





class Skill (models.Model):
    '''The Skill Object describes somthing (usually a Process, Method ot Tool)
    for which an employee has some knowledge. It is linked to 
    - Employees through the EmployeeSkill object
    - Jobs through the JobSkill object'''
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(SkillCategory)
    
    class Meta:
        '''Default order is category, then name'''
        ordering = ['category', 'name']
    
    def __unicode__(self):
        '''Returns the category and name when printing this object'''
        return self.category.name + ": " + self.name
        
    def get_employees (self):
        '''Returns the list of employees with this skill. This method
        is just for convenience'''
        return self.employeeskill_set.all()

    def get_jobs (self):
        '''Returns the list of jobs requiring this skill. This method
        is just for convenience'''
        return self.jobskill_set.all()




class Job (models.Model):
    '''A job is a daily activity requiring some Skills. It is linked to Skills 
    through the JobSkill object'''
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    class Meta:
        # Default order is on name
        ordering = ['name']
    
    def __unicode__(self):
        '''Returns the name when printing object'''
        return self.name
    
    def get_skills(self):
        '''Returns the list of skills required for this job. This method
        is just for convenience'''
        return self.jobskill_set.all()
        
            
   

class EmployeeSkill(models.Model):
    '''Defines the Skills levels for an employee. The level should be between 
    1 (basic knowledge) and 5 (intergalactic guru).'''    
    
    employee = models.ForeignKey(Employee)
    skill = models.ForeignKey(Skill)
    level = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    class Meta:
        #Make sure that there is unicity for an employee and a skill
        unique_together = ("employee", "skill")
        # Default order is employee, then leve (desc), then skill
        ordering = ['employee','-level','skill']
    
    def __unicode__(self):
        '''Returns the employee, skill and level when printing object'''
        return str(self.employee) + " : " + self.skill.name + " : " + str(self.level)
        
        



class JobSkill(models.Model):
    ''''Defines the Skills levels required for a Job. The level should be between 
    1 (basic knowledge) and 5 (intergalactic guru).'''
    
    job = models.ForeignKey(Job)
    skill = models.ForeignKey(Skill)
    level = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    class Meta:
        #Make sure that there is unicity for a job and a skill
        unique_together = ("job", "skill")
        # Default order is employee, then leve (desc), then skill
        ordering = ['job','-level','skill']
        
    def __unicode__(self):
        '''Returns the job, skill and level when printing object'''
        return self.job.name + " : " + self.skill.name + " : " + str(self.level)
       