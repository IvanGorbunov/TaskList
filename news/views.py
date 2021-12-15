from django.shortcuts import render

from rest_framework.views import APIView


class ListNews(APIView):
    """
    Список всех новостей
    """

    def get(self, request):
        return render(request, 'contacts/news.html')