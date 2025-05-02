from django.shortcuts import render
from django.http import HttpResponse


def books_home(request):
    return render(request,'main/profile.html')



