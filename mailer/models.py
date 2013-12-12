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
    
    user = Employee.objects.get(user=version.revision.user)
    date_created = version.revision.date_created
    
    mail_title_prefix = '[CREAM]'
    
    mail_body = "\n"
    mail_body += "Edited by: " + str(user) + "\n"
    mail_body += "Date: " + str(date_created) + "\n"
   
    updated_fields = 0
        
    if version.type == 0:
        # This is an object creation...
        updated_fields += 1
        mail_title_prefix += '[created]'
        mail_body += version.object.get_absolute_url() + "\n"
        for field in version.field_dict:
            mail_body += field + ": " + unicode(version.field_dict[field])+ "\n"
    
    elif version.type == 2:
        # This is an object deletion
        updated_fields += 1
        mail_title_prefix += '[deleted]'
        for field in version.field_dict:
            mail_body += field + ": " + unicode(version.field_dict[field])+ "\n"
    
        
    else:
        # this is an updated object
        # Get the old version for comparison:
        instance_versions = reversion.get_for_object(version.object)
        old_version = instance_versions[1]
        
        mail_title_prefix += '[updated]'
        
        mail_body += version.object.get_absolute_url() + "\n"
        
        for field in version.field_dict:
            old_object_value = old_version.field_dict[field]
            new_object_value = version.field_dict[field]
            if old_object_value != new_object_value:
                updated_fields += 1
                mail_body += "\n" + field + ":\n"
                mail_body += "----------------\n"
                mail_body += "* old: " + unicode(old_object_value) + "\n"
                mail_body += "* new: " + unicode(new_object_value) + "\n"
        
    mail_title = mail_title_prefix + unicode(version.content_type) + " \"" + unicode(version.object) + "\""
        
    mail_body += "\n\nThis is an automatically generated email, please do not reply"
    if updated_fields > 0:
        send_mail(mail_title, mail_body, 'creamrobot@cimpa.com', recipients, fail_silently=False)
    
