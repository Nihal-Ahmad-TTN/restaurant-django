from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import AddMenu
from django.http import HttpResponseRedirect
from .models import Menu
from customer.models import Orders
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url="/login")
def manager_login(request):
    return render(request, 'dashboard.html')

@login_required(login_url="/login")
def show_menu(request):
    data = Menu.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'viewmenu.html', {'data' : page_obj})

@login_required(login_url="/login")
def add_menu(request):
    if request.method == "POST":
        form = AddMenu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manager/menu')
    else:
        form = AddMenu()
    return render(request, 'addmenu.html', {'form' : form})

@login_required(login_url="/login")
def update_item(request, menu_id):
    query = request.POST.get("update_dish")
    if query=="update":
        price = request.POST.get('price')
        Menu.objects.filter(pk = menu_id).update(food_price = price)
    else:
        Menu.objects.filter(pk = menu_id).delete()
    return redirect('update_menu')


@login_required(login_url="/login")
def customer_orders(request):
    status = Q(status__iexact="PENDING")| Q(status__iexact="ACCEPTED")| Q(status__iexact="REJECTED")
    pending_orders = Orders.objects.filter(status)
    return render(request, 'orders.html', {'items': pending_orders})


@login_required(login_url="/login")
def update_order(request, id):
    accept = request.POST.get('accept')
    if accept == "accept":
        Orders.objects.filter(name_id = id, status = "PENDING").update(status = "ACCEPTED")
    else:
        Orders.objects.filter(name_id = id, status = "PENDING").update(status = "REJECTED")
    
    return redirect('customer_orders')


@login_required(login_url="/login")
def update_menu(request):
    data = Menu.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'update_menu.html', {'data' : page_obj})

