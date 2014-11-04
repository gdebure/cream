# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='location',
            field=models.ForeignKey(default=1, to='qualifications.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='position',
            name='publish_date',
            field=models.DateField(default='2014-09-01'),
            preserve_default=False,
        ),
    ]
