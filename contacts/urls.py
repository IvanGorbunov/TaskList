from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', login_required(views.ContactList.as_view()), name='contacts_list'),
]