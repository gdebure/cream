# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SubjectFamily'
        db.create_table('subjects_subjectfamily', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('subjects', ['SubjectFamily'])

        # Adding model 'Subject'
        db.create_table('subjects_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('subject_family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['subjects.SubjectFamily'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('subjects', ['Subject'])


    def backwards(self, orm):
        
        # Deleting model 'SubjectFamily'
        db.delete_table('subjects_subjectfamily')

        # Deleting model 'Subject'
        db.delete_table('subjects_subject')


    models = {
        'subjects.subject': {
            'Meta': {'object_name': 'Subject'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'subject_family': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subjects.SubjectFamily']"})
        },
        'subjects.subjectfamily': {
            'Meta': {'object_name': 'SubjectFamily'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['subjects']
