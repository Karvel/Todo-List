# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todolist_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
