from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update-task/<int:pk>/', views.UpdateTask, name="update_task"),
    path('delete-task/<int:pk>/', views.DeleteTask, name="delete_task"),
]
