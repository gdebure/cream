# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('siglum', models.CharField(max_length=16)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['user__last_name'],
            },
            bases=(models.Model,),
        ),
    ]
