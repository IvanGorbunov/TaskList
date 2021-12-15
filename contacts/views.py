from django.shortcuts import render

from rest_framework.views import APIView


class ContactList(APIView):
    """
    Список всех контактов
    """

    def get(self, request):
        return render(request, 'contacts/contacts.html')