from django.shortcuts import render

from rest_framework.views import APIView


class ListBugs(APIView):
    """
    Список всех ошибок
    """

    def get(self, request):
        return render(request, 'contacts/bugs.html')