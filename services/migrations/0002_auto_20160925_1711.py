# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='is_active',
            field=models.BooleanField(verbose_name='domaine is active', default=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(verbose_name='domain name', max_length=64),
        ),
        migrations.AlterField(
            model_name='domain',
            name='owner',
            field=models.ForeignKey(verbose_name='domain owner', to='users.Employee'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(verbose_name='service name', max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='owner',
            field=models.ForeignKey(verbose_name='service owner', to='users.Employee', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicefamily',
            name='domain',
            field=models.ForeignKey(verbose_name='domain', to='services.Domain', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='servicefamily',
            name='name',
            field=models.CharField(verbose_name='service family name', max_length=128),
        ),
        migrations.AlterField(
            model_name='servicefamily',
            name='owner',
            field=models.ForeignKey(verbose_name='service family owner', to='users.Employee', blank=True, null=True),
        ),
    ]
