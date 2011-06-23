# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Profile.id'
        db.alter_column('users_profile', 'id', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True))


    def backwards(self, orm):
        
        # Changing field 'Profile.id'
        db.alter_column('users_profile', 'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))


    models = {
        'users.profile': {
            'Meta': {'object_name': 'Profile'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['users']
