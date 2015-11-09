from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    completed = models.BooleanField(default = False)

    def complete_iten(self):
        self.completed = True
        self.save()

    def __str__(self):
        return self.text