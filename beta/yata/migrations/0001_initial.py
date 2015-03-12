# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.CharField(max_length=80, blank=True)),
                ('hours', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('hours150', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('hours200', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('hourstravel', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('day', models.IntegerField()),
                ('mistaken', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=30)),
                ('holiday', models.BooleanField(default=False)),
                ('oncall', models.BooleanField(default=False)),
                ('recup', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(to='yata.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField(choices=[(1, b'January'), (2, b'February'), (3, b'March'), (4, b'April'), (5, b'May'), (6, b'June'), (7, b'July'), (8, b'August'), (9, b'September'), (10, b'October'), (11, b'November')])),
                ('year', models.IntegerField()),
                ('locked', models.BooleanField(default=False)),
                ('company', models.ForeignKey(to='yata.Company')),
                ('group', models.ForeignKey(blank=True, to='auth.Group', null=True)),
                ('project', models.ForeignKey(to='yata.Project')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hour',
            name='timesheet',
            field=models.ForeignKey(to='yata.Timesheet'),
            preserve_default=True,
        ),
    ]
