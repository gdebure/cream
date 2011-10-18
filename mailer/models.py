from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group

from reversion.models import Version
import reversion

from projects.models import Deliverable
from users.models import Employee



@receiver(post_save,sender=Version)
def send_mail_on_save(sender, **kwargs):
    
    # This is the list of users that will receive the email
    recipients = User.objects.filter(groups__name='Service Catalog Admins').values_list('email',flat=True)
    # Get the object instance
    version = kwargs['instance']
    
    user = Employee.objects.get(pk=version.revision.user.id)
    date_created = version.revision.date_created
    
    mail_body = "\n"
    mail_body += "User who made the change: " + str(user) + "\n"
    mail_body += "Date: " + str(date_created) + "\n"
   
    if version.type == 0:
        # This is an object creation...
        mail_title = "[CREAM] " + str(version.content_type)+ " " + str(version.object_repr) + " created"
        mail_body += version.object.get_absolute_url() + "\n"
        for field in version.field_dict:
            mail_body += field + ": " + str(version.field_dict[field])+ "\n"
    
    elif version.type == 2:
        # This is an object deletion
        mail_title = "[CREAM] " + str(version.content_type) + " " + str(version.object_repr) + " deleted"
        for field in version.field_dict:
            mail_body += field + ": " + str(version.field_dict[field])+ "\n"
    
        
    else:
        # this is an updated object
        # Get the old version for comparison:
        instance_versions = reversion.get_for_object(version.object)
        old_version = instance_versions[1]
        
        mail_title = "[CREAM] " + str(version.content_type)+ " " + str(version.object_repr) + " updated"
        mail_body += version.object.get_absolute_url() + "\n"
        
        for field in version.field_dict:
            old_object_value = old_version.field_dict[field]
            new_object_value = version.field_dict[field]
            if old_object_value != new_object_value:
                mail_body += "\n" + field + ":\n"
                mail_body += "----------------\n"
                mail_body += "* old: " + str(old_object_value) + "\n"
                mail_body += "* new: " + str(new_object_value) + "\n"
        
    
    mail_body += "\n\nThis is an automatically generated email, please do not reply"
    send_mail(mail_title, mail_body, 'creamrobot@cimpa.com', recipients, fail_silently=False)
    




@receiver(post_save,sender=Deliverable)    
def send_mail_on_service_link(sender, **kwargs):

    deliverable = kwargs['instance']
    if deliverable.approved_by_service_owner == 'P':
        mail_title = '[CREAM] ' + 'New deliverable added to service ' + str(deliverable.service)
        mail_body = 'Please check whether the deliverable "' + str(deliverable)+ '" should be linked to the service "' + str(deliverable.service) + "\n"
        mail_body += "\n\nThis is an automatically generated email, please do not reply"
        
        send_mail(mail_title,mail_body,'creamrobot@cimpa.com',[deliverable.service.owner.user.email],fail_silently=False)