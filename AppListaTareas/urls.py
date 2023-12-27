from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listatareas, name='lista'),
    path('eliminar/<int:tarea_id>/', views.eliminar, name='eliminar'),
]
