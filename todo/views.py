from django.db import IntegrityError
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.viewsets import ViewSetMixin

from .forms import TaskForm

from todo.models import Tasks
from .serializers import TaskSerializer


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


class ListTasks(APIView):
    """
    Список всех задач
    """
    def get(self, request):
        tasks = Tasks.objects.filter(user=request.user, date_completed__isnull=True).all()
        serializer = TaskSerializer(tasks, many=True)
        context = {
            'tasks': serializer.data
        }
        return render(request, 'todo/current_tasks_list.html', context)


class NewTask(APIView):
    """
    Новая задача
    """
    def get(self, request):
        serializer = TaskSerializer()
        context = {
            'user': request.user,
            'form': TaskForm(serializer.data),
        }
        return render(request, 'todo/create_task.html', context)

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'form': TaskForm(serializer.data),
            }
            return render(request, 'todo/create_task.html', context)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        context = {
            'user': request.user,
            'form': TaskForm(serializer.data),
        }
        return render(request, 'todo/edit_task.html', context)

    def post(self, request, *args, **kwargs):
        task = self.get_object(kwargs['pk'])
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'form': TaskForm(serializer.data),
            }
            return render(request, 'todo/edit_task.html', context)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

