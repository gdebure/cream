# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Removing M2M table for field skills on 'Job'
        db.delete_table('qualifications_job_skills')

        # Adding M2M table for field skill on 'Job'
        db.create_table('qualifications_job_skill', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm['qualifications.job'], null=False)),
            ('skill', models.ForeignKey(orm['qualifications.skill'], null=False))
        ))
        db.create_unique('qualifications_job_skill', ['job_id', 'skill_id'])
    
    
    def backwards(self, orm):
        
        # Adding M2M table for field skills on 'Job'
        db.create_table('qualifications_job_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm['qualifications.job'], null=False)),
            ('skill', models.ForeignKey(orm['qualifications.skill'], null=False))
        ))
        db.create_unique('qualifications_job_skills', ['job_id', 'skill_id'])

        # Removing M2M table for field skill on 'Job'
        db.delete_table('qualifications_job_skill')
    
    
    models = {
        'qualifications.job': {
            'Meta': {'object_name': 'Job'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'skill': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['qualifications.Skill']", 'symmetrical': 'False'})
        },
        'qualifications.skill': {
            'Meta': {'object_name': 'Skill'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['qualifications.SkillCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'qualifications.skillcategory': {
            'Meta': {'object_name': 'SkillCategory'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }
    
    complete_apps = ['qualifications']
