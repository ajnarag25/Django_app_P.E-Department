from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Buy, Reserve, Borrow
from .forms import CreateUserForm, BuyForm, ReserveForm, BorrowForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from django.contrib.auth import authenticate, login
#from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def administrator(request):
    
    if request.user.is_authenticated and request.user.is_staff:

        #READ/FETCH ALL THE DATABASE AND DISPLAY IN TABLES  
        buy_db = Buy.objects.all()
        reserve_db = Reserve.objects.all()
        borrow_db = Borrow.objects.all()
        getdata ={
            'buy_data': buy_db,
            'reserve_data': reserve_db,
            'borrow_data': borrow_db
        }
        return render(request, "administrator.html", getdata)

    else:
        return redirect('index')


def loginuser(request):
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        if request.method == 'POST':
            userrr = request.POST.get('username')
            passw = request.POST.get('password') 
            user = authenticate(request, username=userrr,password=passw)
 
            if user is not None:
                login(request, user)

                if user.is_staff:
                    return redirect('administrator')
                else:
                    return redirect('index')
            
            else:
                messages.info(request,'Username/Password is incorrect')
        
        context = {}
        return render(request, 'login.html',context)
    
    #return render(request, 'login.html')
      
    
@login_required(login_url='login')
def index(request):
    return render(request, "index.html")


@login_required(login_url='login')
def buy(request):
    formbuy = BuyForm(request.POST or None)
    if formbuy.is_valid():
        messages.info(request,'Successfully Submitted!')
        formbuy.save()
    context = {
        'formbuy': formbuy
    }
    return render(request, "buy.html", context)


@login_required(login_url='login')
def reserve(request):
    formreserve = ReserveForm(request.POST or None)
    if formreserve.is_valid():
        messages.info(request,'Successfully Submitted!')
        formreserve.save()

    context = {
        'formreserve': formreserve
    }
    return render(request, "reserve.html", context)


@login_required(login_url='login')
def borrow(request):
    formborrow = BorrowForm(request.POST or None)
    if formborrow.is_valid():
        messages.info(request,'Successfully Submitted!')
        formborrow.save()

    context = {
        'formborrow': formborrow
    }
    return render(request, "borrow.html", context)


def register(request):  
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
 

        context = {
            'form': form
        }
        return render(request, "register.html", context)


def student(request, student_id):
    # student_info = Registration.objects.get(id=student_id)
    # form = RegistrationForm(request.POST or None, instance=student_info)
    # context = {
    #     "form": form,
    #     "student": student_info
    #     }
    
    # if form.is_valid():
    #     form.save()
    #     return redirect('administrator')

    return render(request, 'student.html')


@login_required(login_url='login')
def delete_student(request, student_id):
    if not request.user.is_superuser:
        return ...  # TODO prevent access for non-admins

    # student_info = Registration.objects.get(id=student_id)

    # if request.method == "POST":
    #     student_info.delete()
    #     return redirect('administrator')

    return render(request, 'student_delete.html')

def editBuy(request, buy_id):
    buy_info = Buy.objects.get(id=buy_id)
    form = BuyForm(request.POST or None, instance=buy_info)
    context = {
        "form": form,
        "buy": buy_info
        }
    
    if form.is_valid():
        form.save()
        return redirect('administrator')

    return render(request, 'buy_edit.html', context)

def deletebuy(request, buy_id):
    buy_del = Buy.objects.get(id=buy_id)

    if request.method == "POST":
        buy_del.delete()
        return redirect('administrator')

    return render(request, 'buy_delete.html')

def editReserve(request, reserve_id):
    reserve_info = Reserve.objects.get(id=reserve_id)
    form = ReserveForm(request.POST or None, instance=reserve_info)
    context = {
        "form": form,
        "reserve": reserve_info
        }
    
    if form.is_valid():
        form.save()
        return redirect('administrator')

    return render(request, 'reserve_edit.html', context)

def deletereserve(request, reserve_id):
    reserve_del = Reserve.objects.get(id=reserve_id)

    if request.method == "POST":
        reserve_del.delete()
        return redirect('administrator')

    return render(request, 'reserve_delete.html')


def editBorrow(request, borrow_id):
    borrow_info = Borrow.objects.get(id=borrow_id)
    form = BorrowForm(request.POST or None, instance=borrow_info)
    context = {
        "form": form,
        "borrow": borrow_info
        }
    
    if form.is_valid():
        form.save()
        return redirect('administrator')

    return render(request, 'borrow_edit.html', context)

def deleteborrow(request, borrow_id):
    borrow_del = Borrow.objects.get(id=borrow_id)

    if request.method == "POST":
        borrow_del.delete()
        return redirect('administrator')

    return render(request, 'borrow_delete.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
