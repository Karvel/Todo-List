from django.shortcuts import render
from django.utils import timezone
from .models import TodoList

def todo_list(request):
    todo_items = TodoList.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo/todo_list.html', {'todo_items': todo_items})