from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, BuyForm, ReserveForm, BorrowForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def buy(request):
    formbuy = BuyForm(request.POST or None)
    if formbuy.is_valid():
        formbuy.save()

    context = {
        'formbuy': formbuy
    }
    return render(request, "buy.html", context)

def reserve(request):
    formreserve = ReserveForm(request.POST or None)
    if formreserve.is_valid():
        formreserve.save()

    context = {
        'formreserve': formreserve
    }
    return render(request, "reserve.html", context)

def borrow(request):
    formborrow = BorrowForm(request.POST or None)
    if formborrow.is_valid():
        formborrow.save()

    context = {
        'formborrow': formborrow
    }
    return render(request, "borrow.html", context)

def login(request):
    return render(request, "login.html")

def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "register.html", context)
