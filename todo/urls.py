from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [

    # Auth
    # path('', Registration.as_view(), name='currenttasks'),

    # Todos
    path('', views.ListTasks.as_view(), name='list_tasks'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task'),

]