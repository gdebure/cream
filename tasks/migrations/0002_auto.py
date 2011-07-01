# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field subject on 'Task'
        db.create_table('tasks_task_subject', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm['tasks.task'], null=False)),
            ('subject', models.ForeignKey(orm['subjects.subject'], null=False))
        ))
        db.create_unique('tasks_task_subject', ['task_id', 'subject_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field subject on 'Task'
        db.delete_table('tasks_task_subject')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projects.deliverable': {
            'Meta': {'object_name': 'Deliverable'},
            'acceptance_criteria': ('django.db.models.fields.TextField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'estimated_volume': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['services.Service']"}),
            'turnover': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'unit_time': ('django.db.models.fields.IntegerField', [], {})
        },
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
        'services.domain': {
            'Meta': {'object_name': 'Domain'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'services.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'service_family': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['services.ServiceFamily']"})
        },
        'services.servicefamily': {
            'Meta': {'object_name': 'ServiceFamily'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['services.Domain']"}),
            'focal_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'growth_potential': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'service_lifecycle': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'service_position': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'trend': ('django.db.models.fields.IntegerField', [], {})
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
        },
        'tasks.requestortype': {
            'Meta': {'object_name': 'RequestorType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'close_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Employee']"}),
            'criticity': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'deliverable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Deliverable']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'open_date': ('django.db.models.fields.DateField', [], {}),
            'reject_reason': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'requestor': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'requestor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.RequestorType']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'subject': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['subjects.Subject']", 'symmetrical': 'False'}),
            'time_spent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'users.employee': {
            'Meta': {'object_name': 'Employee'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siglum': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['tasks']
