from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category, Book
from django.db.models import Q 

def index(request):
    return render(request, 'index.html')

class CategoriesList(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'category'

def category_books(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, 'book_list.html', {'books': books})

def BookDetail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

def search(request):
    return render(request, 'search.html')

class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        book_list = Book.objects.filter(
            Q(name__icontains=query) | Q(author__icontains=query) | Q(location__icontains=query)
        )
        return book_list
