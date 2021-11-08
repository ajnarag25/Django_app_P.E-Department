from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration

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
    firstname = request.POST.get('firstname', "default value")
    lastname = request.POST.get('lastname', "default value")
    username = request.POST.get('username', "default value")
    password = request.POST.get('password', "default value")
    email = request.POST.get('email', "default value")
    
    saverecord = Registration(firstname=firstname, lastname=lastname, username=username, password=password, email=email)
    saverecord.save()
    
    return render(request, "register.html")
