# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0016_auto_20150505_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('first_contact', models.DateField()),
                ('cv', models.FileField(upload_to=b'')),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField()),
                ('applicant', models.ForeignKey(to='recruitment.Applicant')),
                ('position', models.ForeignKey(related_name='applicant_position', to='recruitment.Applicant')),
                ('status', models.ForeignKey(to='qualifications.EmployeePositionStatus')),
            ],
        ),
    ]
