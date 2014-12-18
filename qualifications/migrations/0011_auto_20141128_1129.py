# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0010_position_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='headcount',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
