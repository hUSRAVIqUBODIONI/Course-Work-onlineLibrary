from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_examplar/', views.add_examplar, name='add_examplar'),
    path('delete_examplar/<int:id>/', views.delete_examplar, name='delete_examplar'),
    path('delete/<str:isbn>/', views.delete_book, name='delete_book'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_genre/', views.add_genre, name='add_genre'),
]
