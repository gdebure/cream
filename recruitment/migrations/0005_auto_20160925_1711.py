# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0004_auto_20150629_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='cv',
            field=models.FileField(upload_to='applicants/cv'),
        ),
    ]
