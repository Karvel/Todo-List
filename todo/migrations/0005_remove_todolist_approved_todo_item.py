# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20151106_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='approved_todo_item',
        ),
    ]
