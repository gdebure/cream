# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'Skill.names'
        db.delete_column('qualifications_skill', 'names')
    
    
    def backwards(self, orm):
        
        # Adding field 'Skill.names'
        db.add_column('qualifications_skill', 'names', self.gf('django.db.models.fields.CharField')(default='', max_length=64), keep_default=False)
    
    
    models = {
        'qualifications.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['qualifications']
