# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todolist_approved_todo_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
