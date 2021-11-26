from django.http import HttpResponse
from django.shortcuts import redirect, render
#from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Registration, Buy, Reserve, Borrow
from .forms import RegistrationForm, BuyForm, ReserveForm, BorrowForm

# Create your views here.

def index(request):
    return render(request, "index.html")


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = {'invalid': False}

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login_page')
    else:
        context['form'] = form
        context['invalid'] = True

    return render(request, "register.html", context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    context = {'invalid': False}
    
    if request.POST is not None and len(request.POST):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

        context['invalid'] = True

    return render(request, 'login.html', context)


def request_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login_page')
def buy(request):
    formbuy = BuyForm(request.POST or None)
    if formbuy.is_valid():
        formbuy.save()

    context = {
        'formbuy': formbuy
    }
    return render(request, "buy.html", context)


@login_required(login_url='login_page')
def reserve(request):
    formreserve = ReserveForm(request.POST or None)
    if formreserve.is_valid():
        formreserve.save()

    context = {
        'formreserve': formreserve
    }
    return render(request, "reserve.html", context)


@login_required(login_url='login_page')
def borrow(request):
    formborrow = BorrowForm(request.POST or None)
    if formborrow.is_valid():
        formborrow.save()

    context = {
        'formborrow': formborrow
    }
    return render(request, "borrow.html", context)


def student(request, pk_id):
    student_info = Registration.objects.get(id=pk_id)

    context = {"student": student_info}
    
    return render(request, 'student.html', context)


def admin(request):
    #READ/FETCH ALL THE DATABASE AND DISPLAY IN TABLES
    registration_db = Registration.objects.all
    buy_db = Buy.objects.all
    reserve_db = Reserve.objects.all
    borrow_db = Borrow.objects.all
    getdata ={
        'data': registration_db,
        'buy_data': buy_db,
        'reserve_data': reserve_db,
        'borrow_data': borrow_db
    }
    return render(request, "admin.html", getdata)
