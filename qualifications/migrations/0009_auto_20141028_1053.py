# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0008_auto_20141021_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionStatus',
            fields=[
                ('id', models.CharField(max_length=1, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('css_class', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='position',
            name='status',
            field=models.ForeignKey(to='qualifications.PositionStatus'),
        ),
    ]
