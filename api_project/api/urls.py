from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old list view
    path('books/', BookList.as_view(), name='book-list'),

    # New router endpoints
    path('', include(router.urls)),
]