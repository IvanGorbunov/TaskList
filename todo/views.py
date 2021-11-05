from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


class HomePage(APIView):

    def get(self, request):
        return render(request, 'todo/home.html')


class Registration(APIView):
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'todo/signupuser.html', context)

    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttasks')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'error': 'Это имя пользователя уже используется.'
                }
                return render(request, 'todo/signupuser.html', context)

        else:
            context = {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают!'
            }
            return render(request, 'todo/signupuser.html', context)


class LoginUser(APIView):

    def get(self, request):
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'todo/loginuser.html', context)

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': 'Логин или пароль не совпадают.'
            }
            return render(request, 'todo/loginuser.html', context)
        else:
            try:
                login(request, user)
                return redirect('currenttasks')
            except IntegrityError:
                context = {
                    'error': 'Это имя пользователя уже используется.'
                }
                return render(request, 'todo/loginuser.html', context)


class LogoutUser(APIView):

    def get(self, request):
        pass

    def post(self, request):
        logout(request)
        return redirect('home')


class CurrentTasks(APIView):

    def get(self, request):
        return render(request, 'todo/current_tasks_list.html')
