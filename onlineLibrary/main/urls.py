from django.urls import path
from books import views
from .views import profile,logout_view,login_view,register_view


urlpatterns = [
    path('', views.book_list, name='home'),  # 👈 главная страница
    path('profile/', profile, name='profile'),
    path('add/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_examplar/', views.add_examplar, name='add_examplar'),
    path('delete_examplar/<int:id>/', views.delete_examplar, name='delete_examplar'),
    path('delete/<str:isbn>/', views.delete_book, name='delete_book'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('borrow/<int:exampler_id>/', views.borrow_examplar, name='borrow_examplar'),
    path('logout/', logout_view, name='logout'),  # Маршрут для logout
    path('login/', login_view, name='login'),  # Маршрут для logout
    path('register/', register_view, name='register'),  # Маршрут для logout
]
