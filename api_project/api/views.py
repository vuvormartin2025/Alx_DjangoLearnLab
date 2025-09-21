from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Book API. Visit /api/books/ to see all books."})

# api/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Existing imports like ListAPIView etc.

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions for Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer