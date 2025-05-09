from django.contrib import admin
from .models import Book, Author
from .models import Genre, Exampler, Issuance

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



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Exampler)
class ExamplerAdmin(admin.ModelAdmin):
    list_display = ('inventory_number', 'book', 'condition')

@admin.register(Issuance)
class IssuanceAdmin(admin.ModelAdmin):
    list_display = ('reader', 'exampler', 'issuance_date', 'return_date', 'rating')
