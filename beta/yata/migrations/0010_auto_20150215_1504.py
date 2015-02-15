# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0009_apistatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apistatus',
            name='user',
        ),
        migrations.DeleteModel(
            name='ApiStatus',
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={'permissions': (('api_read_only', 'Read-Only API access to every timesheet'),)},
        ),
    ]
