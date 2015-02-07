# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('yata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('billable', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(to='yata.Customer')),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
