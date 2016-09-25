# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverable',
            name='code',
            field=models.CharField(verbose_name='project deliverable identifier', null=True, max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='name',
            field=models.CharField(verbose_name='project deliverable name', max_length=128),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='project',
            field=models.ForeignKey(verbose_name='project name', to='projects.Project', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='service',
            field=models.ForeignKey(verbose_name='service family / service', to='services.Service', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='turnover',
            field=models.DecimalField(verbose_name='turnover (€)', max_digits=12, blank=True, null=True, editable=False, decimal_places=2, validators=[projects.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='unit_time',
            field=models.IntegerField(verbose_name='unit time (mn)', null=True, blank=True, editable=False, validators=[projects.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='deliverablevolume',
            name='date_end',
            field=models.DateField(help_text='YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='deliverablevolume',
            name='date_start',
            field=models.DateField(help_text='YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateField(verbose_name='project end date', help_text='YYYY-MM-DD', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateField(verbose_name='project start date', help_text='YYYY-MM-DD', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='department',
            field=models.CharField(verbose_name='CIMPA department', null=True, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(verbose_name='project name', max_length=64),
        ),
        migrations.AlterField(
            model_name='project',
            name='natco',
            field=models.CharField(verbose_name='turnover allocation natco', null=True, max_length=2, choices=[('D', 'CIMPA GmbH'), ('F', 'CIMPA SAS'), ('U', 'CIMPA Ltd')], blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='number',
            field=models.CharField(verbose_name='project number', max_length=32, unique=True),
        ),
    ]
