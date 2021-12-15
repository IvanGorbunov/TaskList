from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
   path('', views.ListNews.as_view(), name='news_list'),
]