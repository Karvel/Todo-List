# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20151108_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeditem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
