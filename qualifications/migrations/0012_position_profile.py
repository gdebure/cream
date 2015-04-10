# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0011_auto_20141128_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='profile',
            field=models.ForeignKey(default=1, to='qualifications.Profile'),
            preserve_default=False,
        ),
    ]
