from django.db import IntegrityError
from django.forms import model_to_dict
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
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
        return render(request, 'todo/home.html', status=status.HTTP_200_OK)


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
                return redirect('home')
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
        return render(request, 'todo/loginuser.html', context, status=status.HTTP_200_OK)

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if not user:
            context = {
                'form': AuthenticationForm(),
                'error': 'Логин или пароль не совпадают.'
            }
            return render(request, 'todo/loginuser.html', context, status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {
                    'error': 'Это имя пользователя уже используется.'
                }
                return render(request, 'todo/loginuser.html', context, status=status.HTTP_200_OK)


class LogoutUser(APIView):

    def get(self, request):
        logout(request)
        return redirect('loginuser')

    def post(self, request):
        logout(request)
        return redirect('loginuser')


class TaskList(View):
    """
    Список всех задач
    """

    def get(self, request):
        form = TaskForm()
        tasks = Tasks.objects.filter(user=request.user).all()
        serializer = TaskSerializer(tasks, many=True)
        context = {
            'form': form,
            'tasks': serializer.data
        }
        return render(request, 'todo/task_list.html', context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            new_task = form.save()
            return JsonResponse(
                {
                    'task': model_to_dict(new_task),
                },
                status=200
            )
        else:
            return redirect('todo:tasks_list')


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

    def get_object(self, pk, user):
        try:
            return Tasks.objects.get(pk=pk, user=user)
        except Tasks.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        task = self.get_object(pk, user=request.user)
        if task is None:
            return HttpResponse('Not found: 404')
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


class TaskComplete(View):

    def post(self, request, pk):
        task = Tasks.objects.get(id=pk)
        task.completed = True
        task.save()
        return JsonResponse(
            {
                'task': model_to_dict(task)
            },
            status=200
        )
