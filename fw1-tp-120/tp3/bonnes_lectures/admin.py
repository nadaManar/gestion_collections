from django.contrib import admin
from .models import Review, Author, Book  

admin.site.register(Review)
admin.site.register(Author)
admin.site.register(Book)
