
from django.shortcuts import get_object_or_404, render, redirect
from .forms import LoginForm, RegisterForm
from .models import Reader
from books.views import Issuance
from django.utils import timezone
from books.models import Issuance
from django.contrib.auth.decorators import login_required


from django.utils import timezone
from books.models import Issuance

def return_book(request, issuance_id):
    issuance = get_object_or_404(Issuance, id=issuance_id)

    # Если книга ещё не возвращена, то возвращаем её
    issuance.return_date = timezone.now()
    issuance.status = 'returned'
    issuance.save()

    return redirect('reader_profile', reader_id=issuance.reader.id)


from django.utils import timezone

@login_required
def reader_profile(request, reader_id):
    # Если это админ, то можем показывать профиль другого читателя
    reader = get_object_or_404(Reader, id=reader_id)
    issuances = Issuance.objects.filter(reader=reader)
    today = timezone.now().date()  # Получаем текущую дату
    
    return render(request, 'reader_profile.html', {
        'reader': reader,
        'issuances': issuances,
        'today': today,  # Передаем текущую дату в шаблон
    })

def search_reader(request):
    query = request.GET.get('reader_number')
    reader = None
    if query:
        reader = Reader.objects.filter(reader_number=query).first()
    return render(request, 'main/search_reader.html', {'reader': reader})


def index(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            reader = Reader.objects.filter(name=name, surname=surname, email=email).first()
            if reader:
                request.session['reader_id'] = reader.id
                return redirect('profile')
            else:
                form.add_error(None, "Пользователь не найден. Зарегистрируйтесь.")
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Reader.objects.filter(email=email).exists():
                form.add_error('email', "Пользователь с таким email уже зарегистрирован.")
            else:
                reader = form.save(commit=False)
                reader.date_of_registration = timezone.now().date()
                reader.save()
                request.session['reader_id'] = reader.id
                return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def profile(request):
    reader_id = request.session.get('reader_id')
    reader = Reader.objects.filter(id=reader_id).first() if reader_id else None

    if reader:
        issuances = Issuance.objects.filter(reader=reader)
    else:
        issuances = []

    return render(request, 'main/profile.html', {
        'reader': reader,
        'issuances': issuances  # передаем список аренд
    })

def logout_view(request):
    request.session.flush()  # Очистка сессии
    return redirect('login')  # Перенаправление на страницу входа


def logout_view(request):
    request.session.flush()
    return redirect('login')
