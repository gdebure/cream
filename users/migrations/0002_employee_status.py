# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default='P', max_length=1, choices=[(b'I', b'Intercontract'), (b'S', b'Structure'), (b'P', b'On Project')]),
            preserve_default=False,
        ),
    ]
