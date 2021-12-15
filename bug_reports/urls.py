from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'bug_reports'
urlpatterns = [
    path('', login_required(views.ListBugs.as_view()), name='bug_reports_list'),
]