from django.urls import path
from . import views

urlpatterns = [
    path('createtask', views.create_task, name='createtask'),
    path('listtask', views.list_tasks, name='listtask'),
    path('updatetask<int:id>', views.update_task, name='updatetask'),
    path('deletetask<int:id>', views.delete_task, name='deletetask'),
]
