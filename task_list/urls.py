"""task_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include


from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.Registration.as_view(), name='signupuser'),
    path('login/', views.LoginUser.as_view(), name='loginuser'),
    path('logout/', views.LogoutUser.as_view(), name='logoutuser'),

    # Todos
    path('', login_required(views.HomePage.as_view()), name='home'),
    path('tasks/', include('todo.urls')),
    path('contacts/', include('contacts.urls')),
    path('news/', include('news.urls')),
    path('bug_reports/', include('bug_reports.urls')),
]
