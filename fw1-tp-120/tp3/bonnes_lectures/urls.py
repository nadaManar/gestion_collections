from django.shortcuts import redirect
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('books/', views.book_list, name='book_list'),
        path('book/<int:id>/', views.book_detail, name='book_detail'),
            path('new_book/', views.new_book, name='new_book'),
      path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
          path('edit_book/<int:id>/', views.edit_book, name='edit_book'),  
 path('', views.base, name='base'),

 path('reviews/<int:book_id>', views.review_list, name='review_list'),
    path('reviews/new/<int:book_id>', views.add_review, name='add_review'),
path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='author_add'),
   path('authors/edit/<pk>/', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('authors/delete/<pk>/', views.AuthorDeleteView.as_view(), name='author_delete'),

     
]