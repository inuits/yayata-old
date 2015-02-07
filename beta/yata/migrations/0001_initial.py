# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
    ]
