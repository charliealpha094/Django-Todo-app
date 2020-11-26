# Done by Carlos Amaral (2020/11/23)

from django.urls import path
from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
)

urlpatterns = [
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_edit'),
    path('todo/new/', TodoCreateView.as_view(), name='todo_new'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='post_detail'),
    path('', TodoListView.as_view(), name='home'),
]
