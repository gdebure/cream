from django.db import models

class Location(models.Model):
    '''A class that lists the possible locations, used in other apps'''
    
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return str(self.name)
