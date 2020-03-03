from django.urls import path
from lib import views
#from django.views.generic import TemplateView
from lib.views import *
from .admin import *

admin.site.site_header = "HIET Library"
admin.site.site_title = "Welcome to HIET Library Admin Panel"
admin.site.index_title = "Welcome to HIET Library Admin Panel"

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', CategoriesList.as_view(), name='categories'),
    path('categories/<slug:slug>', views.category_books, name='books'),
    path('categories/books/<int:id>', views.BookDetail, name='details'),
    path('search', views.search, name='search'),
    path('search_results', SearchResultsView.as_view(), name='search_results'),
]
