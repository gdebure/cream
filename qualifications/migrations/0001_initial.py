# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1, choices=[(b'I', b'Idea'), (b'S', b'Under Study'), (b'A', b'Approved'), (b'R', b'Rejected'), (b'C', b'Current Position'), (b'P', b'Previous Position')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('comments', models.TextField()),
                ('employee', models.ForeignKey(to='users.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('employee', models.ForeignKey(to='users.Employee')),
            ],
            options={
                'ordering': ['employee', '-level', 'skill'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobProfileSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('job', models.ForeignKey(to='qualifications.Job')),
            ],
            options={
                'ordering': ['job', 'profile', '-level', 'skill'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1, choices=[(b'A', b'Anticipation'), (b'C', b'Cancelled'), (b'V', b'Validated')])),
                ('job', models.ForeignKey(to='qualifications.Job')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('enabled', models.BooleanField(default=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['category', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(to='qualifications.SkillCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobprofileskill',
            name='profile',
            field=models.ForeignKey(to='qualifications.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobprofileskill',
            name='skill',
            field=models.ForeignKey(to='qualifications.Skill'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='jobprofileskill',
            unique_together=set([('job', 'profile', 'skill')]),
        ),
        migrations.AddField(
            model_name='employeeskill',
            name='skill',
            field=models.ForeignKey(to='qualifications.Skill'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='employeeskill',
            unique_together=set([('employee', 'skill')]),
        ),
        migrations.AddField(
            model_name='employeeposition',
            name='position',
            field=models.ForeignKey(to='qualifications.Position'),
            preserve_default=True,
        ),
    ]
