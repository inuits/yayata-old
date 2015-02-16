# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0012_auto_20150215_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='locked',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
