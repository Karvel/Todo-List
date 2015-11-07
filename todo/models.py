from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    approved_todo_item = models.BooleanField(default=False)
    completed = models.BooleanField(default = False)

    def publish(self):
        self.approved_todo_item = True
        self.save()

    def __str__(self):
        return self.text