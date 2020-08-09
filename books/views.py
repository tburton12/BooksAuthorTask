from django.shortcuts import render
from books.models import Book
from authors.models import Author


# Create your views here.
def home(request):
    books_objects = Book.objects.all()
    authors_objects = Author.objects.all()

    prepared_books = []
    for book in books_objects:
        author_dict = next(author for author in authors_objects if author.id == book.author_id)
        current_book = {
            "title": book.title,
            "author": author_dict.name + " " + author_dict.surname
        }
        prepared_books.append(current_book)

    return render(request, 'books/home.html', {'books': prepared_books})

