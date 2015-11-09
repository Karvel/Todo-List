# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20151107_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed', models.BooleanField(default=False)),
                ('todoList', models.ForeignKey(related_name='completed', to='todo.TodoList')),
            ],
        ),
        migrations.DeleteModel(
            name='ApproveItem',
        ),
    ]
