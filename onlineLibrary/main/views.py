
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import Reader
from django.utils import timezone


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
    return render(request, 'main/profile.html', {'reader': reader})

def logout_view(request):
    request.session.flush()
    return redirect('login')
