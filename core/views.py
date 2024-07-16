from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm


def todo_list(request):
    items = ToDo.objects.all()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm()
    return render(request, 'todo_list.html', {'items': items, 'form': form})


def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm()
    return render(request, 'add_todo.html', {'form': form})


def complete_todo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')


def delete_todo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')
