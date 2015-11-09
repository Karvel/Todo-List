# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20151108_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('todoList', models.ForeignKey(related_name='comments', to='todo.TodoList')),
            ],
        ),
    ]
