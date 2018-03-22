from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Book


def index(request):
    author_list = Author.objects.order_by('-was_born')[:10]
    context = {'author_list': author_list}
    return render(request, 'books/index.html', context)


def books(request, author_id):
    book_list = Author.objects.get(pk=author_id)
    context = {'book_list': book_list}
    return render(request, 'books/books.html', context)
