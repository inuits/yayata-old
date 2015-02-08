# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0007_auto_20150208_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timesheet',
            options={'permissions': (('view_all_timesheets', 'View all the timesheets'), ('change_timesheet_company', 'Change the company'), ('change_timesheet_user', 'Change the timesheet user'), ('change_timesheet_group', 'Change the timesheet group'))},
        ),
    ]
