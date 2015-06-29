# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_employee_location'),
        ('recruitment', '0003_auto_20150624_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('notes', models.TextField()),
                ('applicant', models.ForeignKey(to='recruitment.Applicant')),
                ('interviewer', models.ForeignKey(to='users.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('comments', models.TextField()),
                ('css_class', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='status',
            field=models.ForeignKey(to='recruitment.InterviewStatus'),
        ),
        migrations.AddField(
            model_name='interview',
            name='type',
            field=models.ForeignKey(to='recruitment.InterviewType'),
        ),
    ]
