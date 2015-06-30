# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0016_auto_20150505_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='title',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
