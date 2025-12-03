from django.contrib import admin
from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.todos, name="todos"),
    path('<int:pk>/',views.todo_details ,name="todo_details"),
    path('addTodo', views.addTodo, name="addTodo"),
    path('<int:pk>/edit/', views.edit_todo, name="edit_todo"),
    path('<int:pk>/toggle-complete/', views.toggle_todo_complete, name="toggle_todo_complete"),
    path('<int:pk>/delete/', views.delete_todo, name="delete_todo"),
] 
