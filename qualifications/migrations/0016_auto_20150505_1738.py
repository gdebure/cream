# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0015_auto_20150413_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['project', 'job', 'profile']},
        ),
        migrations.AddField(
            model_name='position',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
