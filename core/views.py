from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from users.models import User
from .forms import BookForm

# Create your views here.
def list_books(request):
    books = Book.objects.order_by("-id")
    categories = Category.objects.all()
    return render(request, 'core/list_books.html', { "books" : books, "categories" : categories })

def list_books_oldest(request):
    books = Book.objects.all
    categories = Category.objects.all()
    return render(request, 'core/list_books.html', { "books" : books, "categories" : categories })

def list_books_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    categories = Category.objects.all()
    return render(request, 'core/list_category.html', {"category":category, "categories":categories})

def list_books_title(request):
    books = Book.objects.order_by("title")
    categories = Category.objects.all()
    return render(request, 'core/list_books.html', { "books" : books, "categories" : categories })

def show_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    categories = Category.objects.all()
    return render(request, 'core/show_book.html', { "book" : book, "categories" : categories })

def show_user(request, pk): 
    user = get_object_or_404(User, pk=pk)
    comments = user.comments.all
    return render(request, 'core/show_user.html', { "user": user, "comments" : comments})



def mark_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    pass

