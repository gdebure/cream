# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('users', '0007_auto_20150305_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(default=1, to='core.Location'),
            preserve_default=False,
        ),
    ]
