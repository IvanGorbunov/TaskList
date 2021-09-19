from django.urls import path

from .views import Registration

app_name = 'signupuser'
urlpatterns = [

    # Auth
    path('', Registration.as_view(), name='signupuser')

    # Todos
]