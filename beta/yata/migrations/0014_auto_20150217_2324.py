# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0013_timesheet_locked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='hour',
            options={},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={},
        ),
        migrations.RenameField(
            model_name='hour',
            old_name='description',
            new_name='task',
        ),
        migrations.AddField(
            model_name='hour',
            name='hours150',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hour',
            name='hours200',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hour',
            name='hourstravel',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
    ]
