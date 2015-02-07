# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yata', '0005_auto_20150207_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=80, blank=True)),
                ('hours', models.DecimalField(max_digits=4, decimal_places=2)),
                ('day', models.DateField()),
            ],
            options={
                'permissions': (('view_hour', 'View hour'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.DateField()),
                ('company', models.ForeignKey(to='yata.Company')),
                ('group', models.ForeignKey(to='auth.Group')),
                ('project', models.ForeignKey(to='yata.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_timesheet', 'View timesheet'), ('change_timesheet_company', 'Change the company'), ('change_timesheet_user', 'Change the timesheet user'), ('change_timesheet_group', 'Change the timesheet group')),
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
