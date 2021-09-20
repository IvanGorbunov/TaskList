from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login


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
                return HttpResponse('Приняли! Спасибо за вашу регистрацию.')
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

