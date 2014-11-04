# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=32, null=True, verbose_name=b'project deliverable identifier', blank=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'project deliverable name')),
                ('description', models.TextField()),
                ('acceptance_criteria', models.TextField(null=True, blank=True)),
                ('unit_time', models.IntegerField(blank=True, verbose_name=b'unit time (mn)', null=True, editable=False, validators=[projects.models.validate_positive])),
                ('turnover', models.DecimalField(decimal_places=2, validators=[projects.models.validate_positive], editable=False, max_digits=12, blank=True, null=True, verbose_name=b'turnover (\xe2\x82\xac)')),
            ],
            options={
                'ordering': ['project', 'code', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeliverableVolume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(help_text=b'YYYY-MM-DD')),
                ('date_end', models.DateField(help_text=b'YYYY-MM-DD')),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('unit_price', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('deliverable', models.ForeignKey(to='projects.Deliverable')),
            ],
            options={
                'ordering': ['deliverable', 'date_start'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'project name')),
                ('number', models.CharField(unique=True, max_length=32, verbose_name=b'project number')),
                ('description', models.TextField()),
                ('date_start', models.DateField(help_text=b'YYYY-MM-DD', null=True, verbose_name=b'project start date', blank=True)),
                ('date_end', models.DateField(help_text=b'YYYY-MM-DD', null=True, verbose_name=b'project end date', blank=True)),
                ('customer_name', models.CharField(max_length=128, null=True, blank=True)),
                ('customer_siglum', models.CharField(max_length=16, null=True, blank=True)),
                ('wiki_link', models.URLField(null=True, blank=True)),
                ('department', models.CharField(max_length=2, null=True, verbose_name=b'CIMPA department', blank=True)),
                ('natco', models.CharField(blank=True, max_length=2, null=True, verbose_name=b'turnover allocation natco', choices=[(b'D', b'CIMPA GmbH'), (b'F', b'CIMPA SAS'), (b'U', b'CIMPA Ltd')])),
                ('project_leader', models.ForeignKey(related_name=b'project_leader', blank=True, to='users.Employee', null=True)),
            ],
            options={
                'ordering': ['number', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deliverable',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'project name', to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deliverable',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'service family / service', to='services.Service'),
            preserve_default=True,
        ),
    ]
