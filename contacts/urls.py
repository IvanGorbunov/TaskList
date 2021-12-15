from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.ContactList.as_view(), name='contacts_list'),
]