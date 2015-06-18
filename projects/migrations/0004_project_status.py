# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150618_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default='a', to='projects.ProjectStatus'),
            preserve_default=False,
        ),
    ]
