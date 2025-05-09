
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from books.views import author_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/<int:author_id>/', author_detail, name='author_detail'), 
    path('',include('main.urls')),
    
]
