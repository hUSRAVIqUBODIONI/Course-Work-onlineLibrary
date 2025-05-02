from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('delete/<str:isbn>/', views.delete_book, name='delete_book'),
]
