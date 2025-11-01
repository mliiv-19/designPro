
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),          # Главная страница
    path('login/', views.login_view, name='login'),  # Страница входа
    path('register/', views.register_view, name='register'), # Страница регистрации
]

