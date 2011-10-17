from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group

import reversion

from services.models import Domain, Service, ServiceFamily
from projects.models import Project, Deliverable, DeliverableVolume

@receiver(post_save,sender=Domain)
@receiver(post_save,sender=Service)
@receiver(post_save,sender=ServiceFamily)
@receiver(post_save,sender=Project)
@receiver(post_save,sender=Deliverable)
@receiver(post_save,sender=DeliverableVolume)
def send_mail_on_save(sender, **kwargs):
    
    # This is the list of users that will receive the email
    recipients = User.objects.filter(groups__name='Service Catalog Admins').values_list('email',flat=True)
    # Get the object instance
    instance = kwargs['instance']
   
    mail_body = "\n"
   
    print 'New Instance:' + str(kwargs['created'])
   
    if kwargs['created']:
        # This is a new object, so we don't have any history yet...
        mail_title = "[CREAM] " + str(sender._meta.verbose_name)+ " " + str(instance) + " created"
        
        for field in instance._meta.get_all_field_names():
            mail_body += field + ": " + str(getattr(instance, field,"")) + "\n"
    
    else:
    
        # Get the latest two version for comparison:
        instance_versions = reversion.get_for_object(instance)
        old_version = instance_versions[0]
        new_version = instance
        
        mail_title = str(sender._meta.verbose_name)+ " " + str(instance) + " updated"
    
        for field in old_version.field_dict:
            old_object_value = old_version.field_dict[field]
            new_object_value = str(getattr(instance,field,""))
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