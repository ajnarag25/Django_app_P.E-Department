from getpass import getuser
from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from django.contrib.auth import authenticate, login
#from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        buy_db = Buy.objects.all()
        reserve_db = Reserve.objects.all()
        borrow_db = Borrow.objects.all()

        storeLen1 = len(buy_db)
        storeLen2 = len(reserve_db)
        storeLen3 = len(borrow_db)

        store1 = [storeLen1]
        store2 = [storeLen2]
        store3 = [storeLen3]

        getDataInventory = Inventory.objects.all()

        inventory = InventoryForm(request.POST or None)   

        if inventory.is_valid():
            messages.info(request,'Successfully Added the Equipment')
            inventory.save()

        context = {
            'inventory': getDataInventory,
            'length1': store1,
            'length2': store2,
            'length3': store3
        } 
        return render(request, "admin.html", context)

    else:
        return redirect('index')

@login_required(login_url='login')
def adminBuy(request):
    buy_db = Buy.objects.all()

    ids1 = request.POST.get('getId')
    stat1 = request.POST.get('stats')

    getMsg1 = request.POST.get('note')
    getIdmsg1 = request.POST.get('idMsg')    

    if ids1 != None and stat1 != None:
        Buy.objects.filter(id = ids1).update(status=stat1)
        messages.info(request,'Successfully Updated the status')

    if getMsg1 != None:
        Buy.objects.filter(id = getIdmsg1).update(note=getMsg1)
        messages.info(request,'Successfully submitted the message!')

    context = {
        'buy_data': buy_db,
    }
    return render(request, "buy_admin.html", context)

@login_required(login_url='login')
def adminReserve(request):
    reserve_db = Reserve.objects.all()

    ids2 = request.POST.get('getId2')
    stat2 = request.POST.get('stats2')

    
    getMsg2 = request.POST.get('note')
    getIdmsg2 = request.POST.get('idMsg')   

    if ids2 != None and stat2 != None:
        Reserve.objects.filter(id = ids2).update(status=stat2)
        messages.info(request,'Successfully Updated the status')

    if getMsg2 != None:
        Reserve.objects.filter(id = getIdmsg2).update(note=getMsg2)
        messages.info(request,'Successfully submitted the message!')

    context = {
        'reserve_data': reserve_db,
    }

    return render(request, "reserve_admin.html", context)

@login_required(login_url='login')
def adminBorrow(request):
    borrow_db = Borrow.objects.all()

    ids3 = request.POST.get('getId3')
    stat3 = request.POST.get('stats3')

    getMsg3 = request.POST.get('note')
    getIdmsg3 = request.POST.get('idMsg')  

    if ids3 != None and stat3 != None:
        Borrow.objects.filter(id = ids3).update(status=stat3)
        messages.info(request,'Successfully Updated the status')

    if getMsg3 != None:
        Borrow.objects.filter(id = getIdmsg3).update(note=getMsg3)
        messages.info(request,'Successfully submitted the message!')

    context ={
        'borrow_data': borrow_db
    }
    return render(request, "borrow_admin.html", context)

def loginuser(request):
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        if request.method == 'POST':
            userrr = request.POST.get('username')
            passw = request.POST.get('password') 
            request.session['username'] = userrr
            user = authenticate(request, username=userrr,password=passw)
 
            if user is not None:
                login(request, user)

                if user.is_staff:
                    return redirect('admin')
                else:
                    return redirect('index')
            
            else:
                messages.info(request,'Username/Password is Incorrect')
        
        context = {
        }
        return render(request, 'login.html',context)
    
    #return render(request, 'login.html')
      
    
@login_required(login_url='login')
def index(request):
    return render(request, "index.html")


@login_required(login_url='login')
def buy(request):
    getUser = request.session['username'] 
    d1 = request.POST.get('fullname')
    d2 = request.POST.get('email')
    d3 = request.POST.get('contact')
    d4 = request.POST.get('course')
    d5 = request.POST.get('mop')
    d6 = request.POST.get('addresses')
    d7 = request.POST.get('total')
    formbuy = BuyForm(request.POST or None)
    if request.method == 'POST':
        messages.info(request,'Something went wrong!')
        if formbuy.is_valid():
            messages.info(request,'Successfully Submitted!')
            request.session['fullname'] = d1
            request.session['email'] = d2
            request.session['contact'] = d3
            request.session['course'] = d4
            request.session['mop'] = d5
            request.session['address'] = d6
            request.session['total'] = d7
            formbuy.save()
            return redirect('success')
    
    context = {
        'formbuy': formbuy,
        'username': getUser
    }
    return render(request, "buy.html", context)


@login_required(login_url='login')
def reserve(request):
    getUser = request.session['username'] 
    formreserve = ReserveForm(request.POST or None)
    if request.method == 'POST':
        messages.info(request,'Something went wrong!')
        if formreserve.is_valid():
            messages.info(request,'Successfully submitted please wait for the confirmation in your order, kindly check your transaction for the meantime if it is available for pick up')
            formreserve.save()
            return redirect('index')
    context = {
        'formreserve': formreserve,
        'username': getUser
    }
    return render(request, "reserve.html", context)


@login_required(login_url='login')
def borrow(request):
    getUser = request.session['username'] 
    getEquipment = request.POST.get('items')
    currentQuants = request.POST.get('quantity')

    b1 = request.POST.get('fullname')
    b2 = request.POST.get('email')
    b3 = request.POST.get('contact')
    b4 = request.POST.get('course')
    b5 = request.POST.get('items')
    b6 = request.POST.get('quantity')
    b7 = request.POST.get('dateofborrow')
    b8 = request.POST.get('dateofreturn')
    b9 = request.POST.get('timeofborrow')
    b10 = request.POST.get('timeofreturn')

    check = Inventory.objects.filter(equipment = getEquipment).values()
    for x in check:
        getQuants = x['quantity']
        getBorrowed = x['borrowers']

        totalQuants = getQuants - int(currentQuants)
        totalBorrowers = getBorrowed + 1

        Inventory.objects.filter(equipment = getEquipment).update(quantity = totalQuants, borrowers = totalBorrowers)

    getDataInventory = Inventory.objects.all()
    formborrow = BorrowForm(request.POST or None)
    if request.method == 'POST':
        messages.info(request,'Something went wrong!')
        if formborrow.is_valid():
            messages.info(request,'Successfully Submitted!')
            request.session['fullname'] = b1
            request.session['email'] = b2
            request.session['contact'] = b3
            request.session['course'] = b4
            request.session['items'] = b5
            request.session['quantity'] = b6
            request.session['dateofborrow'] = b7
            request.session['dateofreturn'] = b8
            request.session['timeofborrow'] = b9
            request.session['timeofreturn'] = b10
            formborrow.save()
            return redirect('success2')

    context = {
        'formborrow': formborrow,
        'inventory': getDataInventory,
        'username': getUser
    }
    return render(request, "borrow.html", context)


def register(request):  
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            messages.info(request,'Something went wrong!')
            if form.is_valid():
                messages.info(request,'Successfully Registered your Account!')
                form.save()
                return redirect('login')

        context = {
            'form': form
        }
        return render(request, "register.html", context)

def editBuy(request, buy_id):
    buy_info = Buy.objects.get(id=buy_id)
    form = BuyForm(request.POST or None, instance=buy_info)
    context = {
        "form": form,
        "buy": buy_info
        }
    
    if form.is_valid():
        messages.info(request,'Successfully Updated!')
        form.save()
        return redirect('adminbuy')

    return render(request, 'buy_edit.html', context)

def deletebuy(request, buy_id):
    buy_info = Buy.objects.get(id=buy_id)
    buy_del = Buy.objects.get(id=buy_id)

    context = {
        "buy": buy_info
        }
    if request.method == "POST":
        messages.info(request,'Successfully Deleted!')
        buy_del.delete()
        return redirect('adminbuy')

    return render(request, 'buy_delete.html', context)

def editReserve(request, reserve_id):
    reserve_info = Reserve.objects.get(id=reserve_id)
    form = ReserveForm(request.POST or None, instance=reserve_info)
    context = {
        "form": form,
        "reserve": reserve_info
        }
    
    if form.is_valid():
        messages.info(request,'Successfully Updated!')
        form.save()
        return redirect('adminreserve')

    return render(request, 'reserve_edit.html', context)

def deletereserve(request, reserve_id):
    reserve_info = Reserve.objects.get(id=reserve_id)
    reserve_del = Reserve.objects.get(id=reserve_id)

    context = {
        "reserve": reserve_info
    }
    if request.method == "POST":
        messages.info(request,'Successfully Deleted!')
        reserve_del.delete()
        return redirect('adminreserve')

    return render(request, 'reserve_delete.html', context)


def editBorrow(request, borrow_id):
    borrow_info = Borrow.objects.get(id=borrow_id)
    form = BorrowForm(request.POST or None, instance=borrow_info)
    context = {
        "form": form,
        "borrow": borrow_info
        }
    
    print(form)
    if form.is_valid():
        messages.info(request,'Successfully Updated!')
        form.save()
        return redirect('adminborrow')

    return render(request, 'borrow_edit.html', context)

def deleteborrow(request, borrow_id):
    borrow_info = Borrow.objects.get(id=borrow_id)
    borrow_del = Borrow.objects.get(id=borrow_id)

    context = {
        "borrow": borrow_info
        }
    if request.method == "POST":
        messages.info(request,'Successfully Deleted!')
        borrow_del.delete()
        return redirect('adminborrow')

    return render(request, 'borrow_delete.html', context)


def editEquipment(request, equipment_id):
    equipment_info = Inventory.objects.get(id = equipment_id)
    equipment_form = InventoryForm(request.POST or None, instance = equipment_info)

    context = {
        'equipments': equipment_info
    }

    if equipment_form.is_valid():
        messages.info(request,'Successfully Updated!')
        equipment_form.save()
        return redirect('admin')

    return render(request, 'inventory_edit.html', context)

def deleteequipment(request, equipment_id):
    equipment_info = Inventory.objects.get(id = equipment_id)
    equipment_del = Inventory.objects.get(id=equipment_id)

    context = {
        'equipments': equipment_info
    }

    if request.method == "POST":
        messages.info(request,'Successfully Deleted!')
        equipment_del.delete()
        return redirect('admin')

    return render(request, 'inventory_delete.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def SuccessPage(request):
    g1 = request.session['fullname']
    g2 = request.session['email']
    g3 = request.session['contact']
    g4 = request.session['course']
    g5 = request.session['mop']
    g6 = request.session['address']
    g7 = request.session['total']

    context ={
        'get1': g1,
        'get2': g2,
        'get3': g3,
        'get4': g4,
        'get5': g5,
        'get6': g6,
        'get7': g7

    }
    return render(request, 'success.html', context)

def Transaction(request):
    getusername = request.session['username']
    checkForm1= Buy.objects.filter(username=getusername).values()
    checkForm2= Reserve.objects.filter(username=getusername).values()
    checkForm3= Borrow.objects.filter(username=getusername).values()

    storeList1 = []
    storeList2 = []
    storeList3 = []
    for x in checkForm1:
        storeList1.append(x)
    for x in checkForm2:
        storeList2.append(x)
    for x in checkForm3:
        storeList3.append(x)
    
    context={
        'buyData': storeList1,
        'reserveData': storeList2,
        'borrowData': storeList3
    }
    return render(request, 'transaction.html', context)


def SuccessPage2(request):
    p1 = request.session['fullname']
    p2 = request.session['email']
    p3 = request.session['contact']
    p4 = request.session['course']
    p5 = request.session['items']
    p6 = request.session['quantity']
    p7 = request.session['dateofborrow']
    p8 = request.session['dateofreturn']
    p9 = request.session['timeofborrow']
    p10 = request.session['timeofreturn']

    context ={
        'get1': p1,
        'get2': p2,
        'get3': p3,
        'get4': p4,
        'get5': p5,
        'get6': p6,
        'get7': p7,
        'get8': p8,
        'get9': p9,
        'get10': p10

    }

    return render(request, 'success2.html', context)