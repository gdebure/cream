# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0002_auto_20141021_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='headcount',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
