# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'domain name')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'domaine is active')),
                ('description', models.TextField(null=True)),
                ('owner', models.ForeignKey(verbose_name=b'domain owner', to='users.Employee')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name=b'service name')),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('owner', models.ForeignKey(verbose_name=b'service owner', blank=True, to='users.Employee', null=True)),
            ],
            options={
                'ordering': ['service_family__name', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceFamily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'service family name')),
                ('description', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'domain', to='services.Domain')),
                ('owner', models.ForeignKey(verbose_name=b'service family owner', blank=True, to='users.Employee', null=True)),
            ],
            options={
                'ordering': ['domain', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='service',
            name='service_family',
            field=models.ForeignKey(to='services.ServiceFamily', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
    ]
