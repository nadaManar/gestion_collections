from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author
from .forms import AuthorForm
from django.contrib.auth.decorators import login_required



from .forms import BookForm,ReviewForm

from .models import Book  
def about(request):
    return HttpResponse("Application Bonnes Lectures, développée en TP de Framework Web, Université d’Orléans, 2024")

def welcome(request):
    return render(request, 'welcome.html')
def book_list(request):
    books = Book.objects.all()  # Récupérer tous les livres
    return render(request, 'book_list.html', {'books': books})
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})
@login_required
def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list after saving
    else:
        form = BookForm()
    return render(request, 'new_book.html', {'form': form})
@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    return render(request, 'confirm_delete.html', {'book': book})
@login_required
def edit_book(request, id):
    # Récupérer l'objet livre à modifier
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  
            return redirect('book_list') 
    else:
        form = BookForm(instance=book) 

    return render(request, 'edit_book.html', {'form': form, 'book': book})
def base(request) : 
    return render(request,'base.html')


#debut tp6
def review_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    return render(request, 'review_list.html', {'book': book, 'reviews': reviews})
@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'book': book})



class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')

 

@login_required
def create_review(request, book_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.book_id = book_id
            review.save()
            return redirect('book_detail', book_id=book_id)
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})
   