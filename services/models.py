from django.db import models
from users.models import User

class Domain (models.Model):
    
    name = models.CharField(max_length=64)
    is_active = models.BooleanField()
    owner = models.ForeignKey(User)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name