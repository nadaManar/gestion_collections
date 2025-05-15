from django import forms
from .models import Book
from .models import Review
from .models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year', 'isbn', 'backCover', 'cover']
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']      