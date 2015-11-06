from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import TodoList
from .forms import TodoForm

def todo_list(request):
    todo_items = TodoList.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo/todo_list.html', {'todo_items': todo_items})
    
def add_item_to_list(request, pk):
    todo_items = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.todo_items = todo_items
            new_item.save()
            return redirect('todo.views.todo_list', pk=todo_items.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/add_item_to_list.html', {'form': form})
    
def item_remove(request, pk):
    new_item = get_object_or_404(TodoList, pk=pk)
    todo_items_pk = new_item.pk
    new_item.delete()
    return redirect('todo.views.todo_list', pk=todo_items_pk)