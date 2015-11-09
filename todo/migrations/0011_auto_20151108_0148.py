# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_remove_todolist_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeditem',
            name='completed',
            field=models.NullBooleanField(default=False),
        ),
    ]
