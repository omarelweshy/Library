from django.urls import path
from lib import views
from django.views.generic import TemplateView
from lib.views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('categories', CategoriesList.as_view(), name='categories'),
    path('categories/<slug:slug>', views.category_books, name='books'),
    path('categories/books/<int:id>', views.BookDetail, name='details'),
    path('search', views.search, name='search'),
    path('search_results', SearchResultsView.as_view(), name='search_results'),
]
