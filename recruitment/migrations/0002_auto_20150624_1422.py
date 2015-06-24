# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantposition',
            name='position',
            field=models.ForeignKey(related_name='applicant_position', to='qualifications.Position'),
        ),
    ]
