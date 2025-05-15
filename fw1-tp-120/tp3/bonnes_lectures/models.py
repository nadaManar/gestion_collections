
from django.db import models
from .fields import IsbnField  # Importer le champ personnalisé
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    isbn =   IsbnField(unique=True)  # Utilise le champ personnalisé#models.CharField(max_length=13, unique=True)
    backCover = models.TextField()
    cover = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"