# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0007_employeepositionstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeposition',
            name='status',
            field=models.ForeignKey(to='qualifications.EmployeePositionStatus'),
        ),
    ]
