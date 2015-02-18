# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0014_auto_20150217_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hour',
            name='hours',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hour',
            name='hours150',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hour',
            name='hours200',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hour',
            name='hourstravel',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
