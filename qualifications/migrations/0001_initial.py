# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Skill'
        db.create_table('qualifications_skill', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('names', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('qualifications', ['Skill'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Skill'
        db.delete_table('qualifications_skill')
    
    
    models = {
        'qualifications.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'names': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }
    
    complete_apps = ['qualifications']
