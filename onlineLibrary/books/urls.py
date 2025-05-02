from . import views
from django.urls import path

urlpatterns = [
    path('',views.books_home,name='books_home'),

]
