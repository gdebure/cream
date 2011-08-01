# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Skill.name'
        db.add_column('qualifications_skill', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=64), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Skill.name'
        db.delete_column('qualifications_skill', 'name')
    
    
    models = {
        'qualifications.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }
    
    complete_apps = ['qualifications']
