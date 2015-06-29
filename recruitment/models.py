from django.db import models
from django.utils import timezone

from qualifications.models import Position, EmployeePositionStatus
from users.models import Employee


class Applicant(models.Model):
    
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    first_contact = models.DateField()
    cv = models.FileField(upload_to='applicants/cv')
    comments = models.TextField()
    
    def __unicode__(self):
        return unicode(self.first_name) + " " + unicode(self.last_name)

    
class ApplicantPosition(models.Model):
    
    applicant = models.ForeignKey(Applicant)
    position = models.ForeignKey(Position, related_name='applicant_position')
    status = models.ForeignKey(EmployeePositionStatus)
    comments = models.TextField()
    
    def __unicode__(self):
        return unicode(self.name)
    
    
class InterviewType(models.Model):
    
    name = models.CharField(max_length=32)
    comments = models.TextField()
    
    def __unicode__(self):
        return unicode(self.name)
    

class InterviewStatus(models.Model):
    
    name = models.CharField(max_length=32)
    comments = models.TextField()
    css_class = models.CharField(max_length=128)
    
    def __unicode__(self):
        return unicode(self.name)
    
    
class Interview(models.Model):
    
    applicant = models.ForeignKey(Applicant)
    type = models.ForeignKey(InterviewType)
    date = models.DateField(default=timezone.now)
    interviewer = models.ForeignKey(Employee)
    status = models.ForeignKey(InterviewStatus)
    notes = models.TextField()