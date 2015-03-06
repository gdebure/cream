# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('qualifications', '0012_position_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='location',
            field=models.ForeignKey(to='core.Location'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
