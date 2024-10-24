from django.urls import path
from .views import TodoList, TodoAdd, TodoUpdate, TodoDelete

urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('add/', TodoAdd.as_view(), name='todo_create'),
    path('edit/<int:pk>', TodoUpdate.as_view(), name='todo_update'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='todo_delete'),
]
