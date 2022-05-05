import re
from urllib import request
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request,'contact.html')


def class2(request):
    return render(request, 'class2.html')


def placed_candidate(request):
    return render(request, 'placed_candidate.html')


def empreg(request):
     return render(request, 'empreg.html')


def emplog(request):
     return render(request, 'emplog.html')


def register(request):
     return render(request, 'register.html')
