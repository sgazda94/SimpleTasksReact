from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('tasks/', views.TaskView),
    # path('tasks/<int:pk>/', views.task_detail),
]