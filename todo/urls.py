from django.urls import path
from todo.views import IndexView,CompleteTodo,DeleteCompleted,DeleteAllTodo,delete_todo

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('complete/<todo_id>',CompleteTodo.as_view(), name='complete'),
    path('delete_complete',DeleteCompleted.as_view(), name='delete_completed'),
    path('delete_all',DeleteAllTodo.as_view(), name='delete_all'),
    path('todo-delete/<id>/',delete_todo.as_view(),name='todo-delete')
    #path('add/', TodoFormView.as_view() ,name='todo_form'),
]