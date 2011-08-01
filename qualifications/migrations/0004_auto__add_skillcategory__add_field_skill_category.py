# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'SkillCategory'
        db.create_table('qualifications_skillcategory', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('qualifications', ['SkillCategory'])

        # Adding field 'Skill.category'
        db.add_column('qualifications_skill', 'category', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['qualifications.SkillCategory']), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'SkillCategory'
        db.delete_table('qualifications_skillcategory')

        # Deleting field 'Skill.category'
        db.delete_column('qualifications_skill', 'category_id')
    
    
    models = {
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
