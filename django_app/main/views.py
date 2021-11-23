from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration, Buy, Reserve, Borrow
from .forms import RegistrationForm, BuyForm, ReserveForm, BorrowForm
from .models import Registration

# Create your views here.

def login(request):
    return render(request, "login.html")
    

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
    


def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "register.html", context)

def student(request, pk_id):
    student_info = Registration.objects.get(id=pk_id)

    context = {"student": student_info}
    
    # contents of context dict can be accessed by the template receiving it
    # had to browse django docs to understand since it wasn't obvious
    #
    # anyway, inside functions/methods, the steps are more or less
    # 1. query the database or something
    # 2. place result(s) inside a dict
    # 3. pass the dict to the template
    #
    # inside the template, access the dict contents using syntax
    # {{ dictkey }}
    # attribute access works similar
    # {{ dictkey.attr }}
    #
    # feel free to remove this comment if you understand already

    return render(request, 'student.html', context)
