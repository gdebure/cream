# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_employeestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeestatus',
            name='id',
            field=models.CharField(max_length=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
