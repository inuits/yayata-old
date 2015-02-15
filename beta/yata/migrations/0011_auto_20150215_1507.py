# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0010_auto_20150215_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': (('api_read_only', 'Read-Only full API access'),)},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('api_read_only', 'Read-Only full API access'),)},
        ),
        migrations.AlterModelOptions(
            name='hour',
            options={'permissions': (('api_read_only', 'Read-Only full API access'),)},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('api_read_only', 'Read-Only full API access'),)},
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={'permissions': (('api_read_only', 'Read-Only full API access'),)},
        ),
    ]
