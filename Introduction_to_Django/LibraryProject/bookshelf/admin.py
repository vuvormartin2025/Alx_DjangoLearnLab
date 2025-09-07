
from django.contrib import admin
from .models import Book

# Custom Admin configuration for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ("title", "author", "publication_year")

    # Sidebar filters
    list_filter = ("author", "publication_year")

    # Search functionality
    search_fields = ("title", "author")
