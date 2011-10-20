from django.db import models

from services.models import Domain


def get_database_fields():
    fields = Domain._meta.get_all_field_names()
    return fields



class Report(models.Model):
    
    OPERATORS_CHOICES=(
        ('=','='),
        ('!=','!='),
        ('<','<'),
        ('<=','<='),
        ('>','>'),
        ('>=','>='),
        ('in','in range'),
        ('not in','not in range'),
    )
    
    title = models.CharField(max_length=256, choices=get_database_fields())
    x_data = models.CharField(max_length=128)
    y_data = models.CharField(max_length=128)
    split_per = models.CharField(max_length=128)
    filter_field = models.CharField(max_length=128)
    filter_operator = models.CharField(max_length=4, choices=OPERATORS_CHOICES)
    filter_value = models.CharField(max_length=256)
    graph_type = models.CharField(max_length=1)
    
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return "/reports/" + str(self.id)
    

    
