# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0013_auto_20150305_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 10, 15, 39, 27, 80000)),
        ),
    ]
