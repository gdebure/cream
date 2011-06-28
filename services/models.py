from django.db import models
from users.models import User

class domain (models.Model):
    
    name = models.CharField(max_length=64)
    is_active = models.BooleanField()
    owner = models.ForeignKey(User)
    description = models.TextField(null=True)
