import os
import django

# Configure Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
books_by_author = Book.objects.filter(author__name=author_name)

print(f"\nBooks by {author_name}:")
if books_by_author.exists():
    for book in books_by_author:
        print(f"- {book.title}")
else:
    print("No books found for this author.")


# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"\nLibrary '{library_name}' does not exist.")


# 3. Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"\nNo librarian assigned to '{library_name}'.")