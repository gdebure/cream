# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0003_position_headcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeposition',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeeposition',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
