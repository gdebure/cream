from django.db import models

class project (models.Model):
    
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=32,unique=True)
    description = models.CharField(max_length=255,null=True)
    date_start = models.DateField()
    date_end = models.DateField()