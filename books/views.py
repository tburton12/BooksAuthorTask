from django.shortcuts import render
from books.models import Book


# Create your views here.
def home(request):
    books = Book.objects

    return render(request, 'books/home.html', {'books': books})

