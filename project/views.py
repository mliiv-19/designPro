from django.shortcuts import render, redirect

def home_page(request):
    return render(request, 'home.html')

def login_view(request):
    # Здесь будет логика для страницы входа
    return render(request, 'login.html')

def register_view(request):
    # Здесь будет логика для страницы регистрации
    return render(request, 'register.html')

#для формы входа пользователя
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.username}!')
                return redirect('home')  # или 'dashboard', если будет отдельная страница кабинета
            else:
                messages.error(request, 'Неверный логин или пароль.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})