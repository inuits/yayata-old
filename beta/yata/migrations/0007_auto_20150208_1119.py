# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0006_auto_20150207_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='group',
            field=models.ForeignKey(blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
