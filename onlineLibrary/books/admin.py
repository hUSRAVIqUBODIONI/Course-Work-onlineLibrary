from django.contrib import admin
from .models import Book, Author


class BookInline(admin.TabularInline):
    model = Book.authors.through  
    extra = 0  


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'date_of_birth', 'date_of_death')
    inlines = [BookInline]
    search_fields = ('name', 'surname')

# Настройка отображения книги
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'date_of_publish', 'rating')
    search_fields = ('title', 'isbn')
    filter_horizontal = ('authors',) 

