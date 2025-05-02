from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'rating', 'date_of_publish',)
    search_fields = ('title', 'isbn')
    list_filter = ('date_of_publish',)
