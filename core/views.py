from django.shortcuts import render
from .models import Book, Category
from .forms import BookForm

# Create your views here.
def list_books(request):
    books = Book.objects.order_by("-id")
    categories = Category.objects.all()
    return render(request, 'core/list_books.html', { "books" : books, "categories" : categories })