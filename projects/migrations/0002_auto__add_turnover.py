# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Turnover'
        db.create_table('projects_turnover', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('projects', ['Turnover'])


    def backwards(self, orm):
        
        # Deleting model 'Turnover'
        db.delete_table('projects_turnover')


    models = {
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'customer_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'customer_siglum': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'wiki_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'projects.turnover': {
            'Meta': {'object_name': 'Turnover'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['projects']
