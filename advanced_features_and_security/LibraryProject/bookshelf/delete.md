from bookshelf.models import Book 

# Delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm
Book.objects.all()

