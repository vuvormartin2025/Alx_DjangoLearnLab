from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='tester', password='pass1234')
        self.client = APIClient()

        # Obtain token if using token authentication
        self.client.login(username='tester', password='pass1234')

        # Create some test books
        self.book1 = Book.objects.create(title="Django Basics", author="John Doe", publication_year=2021)
        self.book2 = Book.objects.create(title="Advanced Django", author="Jane Smith", publication_year=2023)

        # URL endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book1.id])

    def test_get_books_list(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """Test creating a new book"""
        data = {"title": "New Book", "author": "New Author", "publication_year": 2025}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "New Book")

    def test_update_book(self):
        """Test updating a book"""
        data = {"title": "Updated Django Basics", "author": "John Doe", "publication_year": 2021}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Basics")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(self.list_url, {'author': 'Jane Smith'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Jane Smith')

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(self.list_url, {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication year"""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))