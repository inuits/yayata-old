# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yata', '0002_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', blank=True),
            preserve_default=True,
        ),
    ]
