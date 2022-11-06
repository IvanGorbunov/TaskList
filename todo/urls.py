from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', login_required(views.TaskList.as_view()), name='tasks_list'),
    path('create/', login_required(views.NewTask.as_view()), name='create_task'),
    path('<int:pk>/', login_required(views.TaskDetail.as_view()), name='current_task'),
    path('<int:pk>/completed/', login_required(views.TaskComplete.as_view()), name='tasks_complete'),
]