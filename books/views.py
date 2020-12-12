from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books_list'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'