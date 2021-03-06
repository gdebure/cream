from datetime import date

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from core.models import Location
from projects.models import Project

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
   
    def __str__(self):
        '''Returns the name when printing object'''
        return str(self.name)
        
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
    enabled = models.BooleanField(default=True)
    description = models.TextField()
    category = models.ForeignKey(SkillCategory)
    
    class Meta:
        '''Default order is category, then name'''
        ordering = ['category', 'name']
    
    def __str__(self):
        '''Returns the category and name when printing this object'''
        return str(self.category.name) + ": " + str(self.name)
        
    def get_employees(self):
        '''Returns the list of employees with this skill. This method
        is just for convenience'''
        return self.employeeskill_set.all()

    def get_jobs(self):
        '''Returns the list of jobs requiring this skill. This method
        is just for convenience'''
        return self.jobprofileskill_set.all()




class Job (models.Model):
    '''A job is a daily activity requiring some Skills. It is linked to Skills 
    through the JobSkill object'''
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    class Meta:
        # Default order is on name
        ordering = ['name']
    
    def __str__(self):
        '''Returns the name when printing object'''
        return str(self.name)
     
    def get_profile_skills(self):
        '''Returns the list of skills required for this job. This method
        is just for convenience'''
        return self.jobprofileskill_set.all()
        
    def get_employees(self):
        return self.jobemployee_set.all()
        


class PositionStatus(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=64)
    css_class = models.CharField(max_length=64)
    
    def __str__(self):
        return str(self.name)



class Profile (models.Model):
    '''A profile is attached to a job to define the qualification levels for this job'''
    
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return str(self.name)

 

class Position(models.Model):
    '''A Position is the implementation of a Job in a specific context'''
    
    title = models.CharField(max_length=128,null=True,blank=True)
    job = models.ForeignKey(Job)
    profile = models.ForeignKey(Profile)
    project = models.ForeignKey(Project)
    status = models.ForeignKey(PositionStatus)
    location = models.ForeignKey(Location)
    publish_date = models.DateField(default=timezone.now)
    headcount = models.DecimalField(max_digits=5,decimal_places=2)
    comment = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering=['project','job','profile']

    def __str__(self):
        if self.title is not None:
            return str(self.title)
        else:
            return str(self.project) + " - " + str(self.job) + " - " + str(self.location)
            
   

class EmployeeSkill(models.Model):
    '''Defines the Skills levels for an employee. The level should be between 
    1 (basic knowledge) and 4 (intergalactic guru).'''    
    
    employee = models.ForeignKey(Employee)
    skill = models.ForeignKey(Skill)
    level = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)])
    
    class Meta:
        #Make sure that there is unicity for an employee and a skill
        unique_together = ("employee", "skill")
        # Default order is employee, then level (desc), then skill
        ordering = ['employee','-level','skill']
    
    def __str__(self):
        '''Returns the employee, skill and level when printing object'''
        return str(self.employee) + " : " + self.skill.name + " : " + str(self.level)
        
    

class JobProfileSkill(models.Model):
    ''''Defines the Skills levels required for a Job. The level should be between 
    1 (basic knowledge) and 5 (intergalactic guru).'''
    
    job = models.ForeignKey(Job)
    profile = models.ForeignKey(Profile)
    skill = models.ForeignKey(Skill)
    level = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    class Meta:
        #Make sure that there is unicity for a job and a skill
        unique_together = ("job", "profile", "skill")
        # Default order is job, then profile, then level (desc), then skill
        ordering = ['job', 'profile', '-level','skill']
        
    def __str__(self):
        '''Returns the job, skill and level when printing object'''
        return str(self.job.name) + " : " + str(self.profile.name) +" : " + str(self.skill.name) + " : " + str(self.level)

        

class EmployeePositionStatus(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=64)
    css_class = models.CharField(max_length=64)
    
    def __str__(self):
        return str(self.name)
    
        
class EmployeePosition(models.Model):
    '''Defines the Positions that are linked to an amployee'''
    
    employee = models.ForeignKey(Employee)
    position = models.ForeignKey(Position)
    status = models.ForeignKey(EmployeePositionStatus)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    comments = models.TextField()
    
    
    def __str__(self):
        return str(self.employee) + ": " + str(self.position)