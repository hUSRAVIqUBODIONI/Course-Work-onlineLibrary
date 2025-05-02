from django.urls import include, path
from books.views import book_list
from . import views

urlpatterns = [
    path('', book_list, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('books/', include('books.urls')),  # Подключаем app
]
