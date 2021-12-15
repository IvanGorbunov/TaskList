from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
   path('', login_required(views.ListNews.as_view()), name='news_list'),
]