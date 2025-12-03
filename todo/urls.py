from django.contrib import admin
from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.todos, name="todos"),
    path('<int:pk>/',views.todo_details ,name="todo_details"),
    path('addTodo', views.addTodo, name="addTodo"),
] 
