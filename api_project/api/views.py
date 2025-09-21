from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Book API. Visit /api/books/ to see all books."})