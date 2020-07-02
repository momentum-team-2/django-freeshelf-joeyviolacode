from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from users.models import User
from .forms import BookForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_books(request):
    books = Book.objects.order_by("-id")
    categories = Category.objects.all()
    return render(request, 'core/list_books.html', { "books" : books, "categories" : categories })

def list_books_oldest(request):
    books = Book.objects.all
    categories = Category.objects.all()
    return render(request, 'core/list_books.html', { "books" : books, "categories" : categories })

def list_books_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    return render(request, 'core/list_category.html', {"category":category, "categories":categories})

def list_books_title(request):
    books = Book.objects.order_by("title")
    categories = Category.objects.all()
    return render(request, 'core/list_books.html', { "books" : books, "categories" : categories })

def show_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    categories = Category.objects.all()
    form = CommentForm()
    return render(request, 'core/show_book.html', { "book" : book, "categories" : categories, "form":form })

def show_user(request, pk): 
    user = get_object_or_404(User, pk=pk)
    comments = user.comments.all
    return render(request, 'core/show_user.html', { "user": user, "comments" : comments})

def add_comment(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    form = CommentForm(data=request.POST)
    comment = None
    if form.is_valid():
        comment = form.save(commit=False)
        comment.book = book
        comment.author = user
        comment.save()
    return redirect(to="show_book", pk=pk)

def mark_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    book.favorited_by.add(user)
    return redirect(to="show_book", pk=pk)

def mark_not_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    book.favorited_by.remove(user)
    return redirect(to="show_book", pk=pk)

def show_favorites(request):
    user = request.user
    books = user.favorite_books.all()
    categories = Category.objects.all()
    return render(request, 'core/show_favorites.html', { "books":books, "categories":categories} )



