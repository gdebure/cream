# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150202_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.CharField(max_length=1, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('css_class', models.CharField(max_length=64)),
            ],
        ),
    ]
