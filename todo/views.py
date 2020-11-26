# Done by Carlos Amaral (2020/11/23)

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'home.html'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'post_detail.html'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = ['title', 'created', 'due_date', 'description', 'check']

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_edit.html'
    fields = ['title', 'due_date', 'description', 'check']

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')
