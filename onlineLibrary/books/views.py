from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book
from django.http import HttpResponseForbidden

def is_admin(request):
    return request.session.get('reader_id') == 1  # Заменить на реальную проверку is_admin, если реализована

def add_book(request):
    if not is_admin(request):
        return HttpResponseForbidden("Доступ только для администратора")
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def delete_book(request, isbn):
    if not is_admin(request):
        return HttpResponseForbidden("Доступ только для администратора")
    
    book = get_object_or_404(Book, isbn=isbn)
    book.delete()
    return redirect('home')

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'main/index.html', {'books': books})
