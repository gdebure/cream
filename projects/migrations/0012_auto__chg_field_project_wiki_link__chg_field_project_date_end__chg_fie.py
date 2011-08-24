# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Project.wiki_link'
        db.alter_column('projects_project', 'wiki_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True))

        # Changing field 'Project.date_end'
        db.alter_column('projects_project', 'date_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True))

        # Changing field 'Project.date_start'
        db.alter_column('projects_project', 'date_start', self.gf('django.db.models.fields.DateField')(null=True, blank=True))

        # Changing field 'Project.customer_siglum'
        db.alter_column('projects_project', 'customer_siglum', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True))

        # Changing field 'Project.customer_name'
        db.alter_column('projects_project', 'customer_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True))

        # Deleting field 'Deliverable.estimated_volume'
        db.delete_column('projects_deliverable', 'estimated_volume')

        # Adding field 'Deliverable.contractual_volume'
        db.add_column('projects_deliverable', 'contractual_volume', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Changing field 'Deliverable.code'
        db.alter_column('projects_deliverable', 'code', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True))

        # Changing field 'Deliverable.unit_time'
        db.alter_column('projects_deliverable', 'unit_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'Deliverable.approved_by_service_owner'
        db.alter_column('projects_deliverable', 'approved_by_service_owner', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True))

        # Changing field 'Deliverable.unit_price'
        db.alter_column('projects_deliverable', 'unit_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True))

        # Changing field 'Deliverable.acceptance_criteria'
        db.alter_column('projects_deliverable', 'acceptance_criteria', self.gf('django.db.models.fields.TextField')(null=True, blank=True))

        # Changing field 'Deliverable.turnover'
        db.alter_column('projects_deliverable', 'turnover', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'Project.wiki_link'
        db.alter_column('projects_project', 'wiki_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Project.date_end'
        db.alter_column('projects_project', 'date_end', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Project.date_start'
        db.alter_column('projects_project', 'date_start', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Project.customer_siglum'
        db.alter_column('projects_project', 'customer_siglum', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Project.customer_name'
        db.alter_column('projects_project', 'customer_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Adding field 'Deliverable.estimated_volume'
        db.add_column('projects_deliverable', 'estimated_volume', self.gf('django.db.models.fields.IntegerField')(default=''), keep_default=False)

        # Deleting field 'Deliverable.contractual_volume'
        db.delete_column('projects_deliverable', 'contractual_volume')

        # Changing field 'Deliverable.code'
        db.alter_column('projects_deliverable', 'code', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'Deliverable.unit_time'
        db.alter_column('projects_deliverable', 'unit_time', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Deliverable.approved_by_service_owner'
        db.alter_column('projects_deliverable', 'approved_by_service_owner', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Deliverable.unit_price'
        db.alter_column('projects_deliverable', 'unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

        # Changing field 'Deliverable.acceptance_criteria'
        db.alter_column('projects_deliverable', 'acceptance_criteria', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Deliverable.turnover'
        db.alter_column('projects_deliverable', 'turnover', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2))
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projects.authorization': {
            'Meta': {'unique_together': "(('employee', 'project'),)", 'object_name': 'Authorization'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Employee']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Profile']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"})
        },
        'projects.deliverable': {
            'Meta': {'object_name': 'Deliverable'},
            'acceptance_criteria': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'approved_by_service_owner': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'contractual_volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['services.Service']"}),
            'turnover': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'unit_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'projects.profile': {
            'Meta': {'object_name': 'Profile'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'customer_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'customer_siglum': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'wiki_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'projects.subject': {
            'Meta': {'object_name': 'Subject'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Project']", 'symmetrical': 'False'}),
            'subject_family': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.SubjectFamily']"})
        },
        'projects.subjectfamily': {
            'Meta': {'object_name': 'SubjectFamily'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'projects.task': {
            'Meta': {'object_name': 'Task'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'close_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['users.Employee']"}),
            'criticity': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'deliverable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Deliverable']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'open_date': ('django.db.models.fields.DateField', [], {}),
            'owner': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'owner'", 'symmetrical': 'False', 'to': "orm['users.Employee']"}),
            'reject_reason': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'requestor': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'subject': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Subject']", 'symmetrical': 'False'}),
            'time_spent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'projects.turnover': {
            'Meta': {'object_name': 'Turnover'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'services.domain': {
            'Meta': {'object_name': 'Domain'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Employee']"})
        },
        'services.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Employee']", 'null': 'True', 'blank': 'True'}),
            'service_family': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['services.ServiceFamily']"})
        },
        'services.servicefamily': {
            'Meta': {'object_name': 'ServiceFamily'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['services.Domain']"}),
            'focal_point': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Employee']", 'null': 'True', 'blank': 'True'}),
            'growth_potential': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'service_lifecycle': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'service_position': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'trend': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'users.employee': {
            'Meta': {'object_name': 'Employee'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siglum': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True'})
        }
    }
    
    complete_apps = ['projects']
