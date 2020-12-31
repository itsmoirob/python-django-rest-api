from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.taskList, name='task-list'),
    path('', views.apiOverview, name='api-overview'),
]
