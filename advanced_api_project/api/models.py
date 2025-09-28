from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Author model stores basic author information.
    One author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Book(models.Model):
    """
    Book model stores book details.
    Each book is linked to one Author via a ForeignKey relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.title} ({self.publication_year})"