from django.db import models
from qualifications.models import Position, EmployeePositionStatus


class Applicant(models.Model):
    
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    first_contact = models.DateField()
    cv = models.FileField()
    comments = models.TextField()
    
    def __unicode__(self):
        return unicode(self.first_name) + " " + unicode(self.last_name)

    
class ApplicantPosition(models.Model):
    
    applicant = models.ForeignKey(Applicant)
    position = models.ForeignKey(Applicant, related_name='applicant_position')
    status = models.ForeignKey(EmployeePositionStatus)
    comments = models.TextField()
    