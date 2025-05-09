from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.utils import timezone

from .models import Book, Author, Exampler, Issuance
from .forms import BookForm, AuthorForm, ExamplerForm
from main.models import Reader


def is_admin(request):
    return request.session.get("reader_id") == 1


def book_list(request):
    books = Book.objects.all().prefetch_related('exemplars', 'authors')
    reader = None
    reader_id = request.session.get("reader_id")
    if reader_id:
        reader = Reader.objects.filter(id=reader_id).first()
    return render(request, 'main/index.html', {'books': books, 'reader': reader})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Фильтруем только доступные экземпляры (т.е. те, которые не арендованы)
    available_examplers = book.exemplars.filter(
        issuances__return_date__isnull=True
    ).distinct()
    
    reader = None
    reader_id = request.session.get("reader_id")
    if reader_id:
        reader = Reader.objects.filter(id=reader_id).first()

    # Подсчитаем количество аренд этой книги
    times_borrowed = Issuance.objects.filter(exampler__book=book).count()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'available_examplers': available_examplers,  # Отправляем только доступные экземпляры
        'reader': reader,
        'times_borrowed': times_borrowed,
        'authors': book.authors.all(),
        'genres': book.genres.all(),
    })




def borrow_examplar(request, exampler_id):
    reader_id = request.session.get('reader_id')
    if not reader_id:
        return redirect('login')

    reader = get_object_or_404(Reader, id=reader_id)
    exampler = get_object_or_404(Exampler, id=exampler_id)

    if exampler.issuances.filter(return_date__isnull=True).exists():
        return HttpResponseForbidden("Экземпляр уже выдан")

    Issuance.objects.create(
        reader=reader,
        exampler=exampler,
        issuance_date=timezone.now().date(),
        return_date=timezone.now().date() + timezone.timedelta(weeks=2)
    )

    return redirect('book_detail', book_id=exampler.book.id)


def add_book(request):
    if not is_admin(request):
        return HttpResponseForbidden("Только админ может добавлять книги")

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def add_author(request):
    if not is_admin(request):
        return HttpResponseForbidden("Только админ может добавлять авторов")

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = AuthorForm()
    return render(request, 'books/add_author.html', {'form': form})


def delete_book(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    book.delete()
    return redirect('home')


def add_examplar(request):
    if not is_admin(request):
        return HttpResponseForbidden("Только админ может добавлять экземпляры")

    if request.method == 'POST':
        form = ExamplerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExamplerForm()
    return render(request, 'books/add_examplar.html', {'form': form})


def delete_examplar(request, id):
    if not is_admin(request):
        return HttpResponseForbidden("Только админ может удалять экземпляры")

    examplar = get_object_or_404(Exampler, id=id)
    examplar.delete()
    return redirect('home')


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'books/author_detail.html', {'author': author})
