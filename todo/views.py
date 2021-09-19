from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView


class Registration(APIView):
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'todo/signupuser.html', context)
