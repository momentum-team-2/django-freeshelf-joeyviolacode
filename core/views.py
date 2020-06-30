from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
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
