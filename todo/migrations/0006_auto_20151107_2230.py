# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_todolist_approved_todo_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApproveItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='completed',
        ),
    ]
