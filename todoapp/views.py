from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm

class TodoList(ListView):
    model = Todo
    template_name = 'todolist/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.all().order_by('-id')

class TodoAdd(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todolist/todo_create.html'
    success_url = reverse_lazy('todo_list')

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todolist/todo_update.html'
    success_url = reverse_lazy('todo_list')
    context_object_name = 'todo'

class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todolist/todo_delete.html'
    success_url = reverse_lazy('todo_list')
    context_object_name = 'todo'

