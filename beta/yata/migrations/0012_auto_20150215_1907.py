# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0011_auto_20150215_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('read_only_customer', 'Read-Only all the customers'),)},
        ),
        migrations.AlterModelOptions(
            name='hour',
            options={'permissions': (('read_only_hours', 'Read-Only all the hours'),)},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('read_only_project', 'Read-Only all the projects'),)},
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={'permissions': (('read_only_timesheet', 'Read-Only all the timesheets'),)},
        ),
    ]
