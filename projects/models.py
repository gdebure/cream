from django.db import models

class Project (models.Model):
    '''A class to handle projects'''
    
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=255, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    customer_name = models.CharField(max_length=128, null=True)
    customer_siglum = models.CharField(max_length=16, null=True)
    wiki_link = models.CharField(max_length=255, null=True)
    
    def __unicode__(self):
        return self.name