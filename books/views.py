from django.shortcuts import render
from django.db.models import Q
from .models import Book
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
class BookListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books_list'
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'books.special_status'

class SearchResultListView(ListView):
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))