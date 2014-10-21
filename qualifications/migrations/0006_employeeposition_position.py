# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0005_remove_employeeposition_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeposition',
            name='position',
            field=models.ForeignKey(default=None, to='qualifications.Position'),
            preserve_default=False,
        ),
    ]
