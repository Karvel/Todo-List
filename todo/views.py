from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import TodoList
from .forms import TodoForm

def todo_list(request):
    new_item = TodoList.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo/todo_list.html', {'new_item': new_item})
    
def item_detail(request, pk):
	todo_item = get_object_or_404(TodoList, pk=pk)
	return render(request, 'todo/item_detail.html', {'todo_item': todo_item})
    
def item_new(request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo_item = form.save(commit=False)
			todo_item.save()
			return redirect('todo.views.item_detail', pk=todo_item.pk)
	else:
		form = TodoForm()
	return render(request, 'todo/item_edit.html', {'form': form})

def item_edit(request, pk):
	todo_item = get_object_or_404(TodoList, pk=pk)
	if request.method == "POST":
		form = TodoForm(request.POST, instance=todo_item)
		if form.is_valid():
			todo_item = form.save(commit=False)
			todo_item.save()
			return redirect('todo.views.item_detail', pk=todo_item.pk)
	else:
		form = TodoForm(instance=todo_item)
	return render(request, 'todo/item_edit.html', {'form': form})
 
def item_remove(request, pk):
    new_item = get_object_or_404(TodoList, pk=pk)
    new_item.delete()
    return redirect('todo.views.todo_list')