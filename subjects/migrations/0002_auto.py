# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field project on 'Subject'
        db.create_table('subjects_subject_project', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subject', models.ForeignKey(orm['subjects.subject'], null=False)),
            ('project', models.ForeignKey(orm['projects.project'], null=False))
        ))
        db.create_unique('subjects_subject_project', ['subject_id', 'project_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field project on 'Subject'
        db.delete_table('subjects_subject_project')


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
        'subjects.subject': {
            'Meta': {'object_name': 'Subject'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Project']", 'symmetrical': 'False'}),
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
