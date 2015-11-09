# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20151108_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeditem',
            name='todoList',
            field=models.ForeignKey(related_name='comments', to='todo.TodoList'),
        ),
    ]
