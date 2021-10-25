from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def buy(request):
    return render(request, "buy.html")

def reserve(request):
    return render(request, "reserve.html")

def borrow(request):
    return render(request, "borrow.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")
