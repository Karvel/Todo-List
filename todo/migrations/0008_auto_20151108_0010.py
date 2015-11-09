# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20151107_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completeditem',
            name='todoList',
        ),
        migrations.AddField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CompletedItem',
        ),
    ]
