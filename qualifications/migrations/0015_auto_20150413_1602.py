# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0014_auto_20150410_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
