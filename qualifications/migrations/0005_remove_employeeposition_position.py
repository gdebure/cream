# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0004_auto_20141021_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeposition',
            name='position',
        ),
    ]
