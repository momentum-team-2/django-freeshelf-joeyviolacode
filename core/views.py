from django.shortcuts import render
from .models import Book, Category
from .forms import BookForm

# Create your views here.
def list_books(request):
    return render(request, 'core/list_books.html')