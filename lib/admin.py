from django.contrib import admin
from .models import Category, Book
from django.db.models import Count


admin.site.register(Category)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'availability','quantity')
    list_filter = ('location','category')