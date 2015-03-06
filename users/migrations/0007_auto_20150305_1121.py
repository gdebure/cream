# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150305_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.ForeignKey(to='users.EmployeeStatus'),
            preserve_default=True,
        ),
    ]
