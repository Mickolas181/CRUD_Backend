from . import views
from django.urls import path

urlpatterns = [
    
    path('tasks/',views.Task_list,name='Task_list'),
    path('tasks/delete/<int:pk>/',views.Task_delete,name='Task_delete'),
    path('tasks/update/<int:pk>/',views.Task_update,name='Task_update'),
    path('tasks/create/',views.Task_create,name='Task_create'),

]
