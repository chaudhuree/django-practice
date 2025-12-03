from django.contrib import admin
from . import views
from django.urls import path,include


urlpatterns = [
    path('<int:pk>/',views.employee_detail ,name="employee_detail"),
] 
