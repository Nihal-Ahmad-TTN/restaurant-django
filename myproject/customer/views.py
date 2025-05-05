from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from management.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from management.models import Menu
from django.db.models import Q
from .models import Orders


# Create your views here.

def home(request):
    return render(request, 'base.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            messages.success(
                request,
                'Registration successful, Please Login Now'
            )
            return redirect('customer_login')
    else :
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form})


def login_view(request):
    form = LoginForm()
    if request.user.is_authenticated:
        if request.user.is_manager:
            return redirect('manager_login')
        elif request.user.is_customer:
            return redirect('customer_dashboard')
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            messages.error(request, "Both fields are required")
            return redirect('customer_login')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid Credentials")
            return redirect('customer_login')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_manager:
                return redirect('manager_login')
            elif request.user.is_customer:
                return redirect('customer_login')
            else:
                messages.error(request, 'you cant access this')
                return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('customer_login')
    return render(request, 'login.html', {'form' : form})



@login_required(login_url="/login")
def customer_dashboard(request):
    return render(request, 'customerdashboard.html')


@login_required(login_url="/login")
def order_food(request):
    types = ['Vegetarian', 'Non Vegetarian']
    categories = ['starters', 'south indian', 'chinese','main course', 'dessert', 'snacks', 'breads']
    query=''
    if request.GET.get('q','') and request.GET.get('q','')!='all':
        query = request.GET.get('q','')
        search = Q(food_name__icontains=query) | Q(food_price__icontains=query)| Q(food_type__iexact=query)| Q(food_category__iexact=query)
        menu = Menu.objects.filter(search)
        return render(request,
                   'filterfood.html',  {'menu': menu,
                       'query':query, 
                       'types' : types, 
                       'categories' : categories
                       })
    else :
        main_course = Menu.objects.filter(food_category__icontains = 'main course')
        starters = Menu.objects.filter(food_category__icontains = 'starters')
        breads = Menu.objects.filter(food_category__icontains = 'breads')
        south_indian = Menu.objects.filter(food_category__icontains = 'south indian')
        chinese = Menu.objects.filter(food_category__icontains = 'chinese')                                                 
        dessert = Menu.objects.filter(food_category__icontains = 'dessert')
        snacks = Menu.objects.filter(food_category__icontains = 'snacks')

    return render(request,
                   'orderfood.html', 
                   {
                       'menu': {
                           'starters': starters,
                           'main course': main_course,
                           'breads': breads,
                           'south indian': south_indian,
                           'chinese': chinese,
                           'dessert': dessert,
                           'snacks': snacks,
                       },
                       'query':query, 
                       'types' : types, 
                       'categories' : categories
                    })


@login_required(login_url="/login")
def add_to_cart(request, food_id):
    userinfo = User.objects.get(name = request.user)
    if request.method == 'POST':
        qua = request.POST.get("quantity")
        if Orders.objects.filter(name_id = food_id):
            temp = Orders.objects.get(name_id = food_id)
            if temp.status=="ADDED":
                Orders.objects.filter(name_id = food_id, status = "ADDED").update(quantity = int(qua) + temp.quantity)
                return redirect('view_cart')
        food_info = Menu.objects.get(pk = food_id)
        order = Orders(user = userinfo, name = food_info, quantity = qua)
        order.save()
        return redirect('view_cart')
    return render(request, 'order_food.html')


@login_required(login_url="/login")
def view_cart(request):
    items = Orders.objects.filter(user = request.user)
    total = sum(item.total_price() for item in items if item.status=='ADDED')
    return render(request, 'carts.html', {'items' : items, 'total': total})


@login_required(login_url="/login")
def remove_item(request, food_id):
    Orders.objects.filter(name_id = food_id, status = "ADDED").delete()
    return redirect('view_cart')


@login_required(login_url="/login")
def update_cart(request, food_id):
    quantity = int(request.POST.get("quantity"))
    if quantity > 0:
        Orders.objects.filter(name_id = food_id, status = "ADDED").update(quantity = quantity)
    else:
        remove_item(request, food_id)
    return redirect('view_cart')


@login_required(login_url="/login")
def thank_you(request):
    user = User.objects.get(name = request.user)
    Orders.objects.filter(user_id = user, status='ADDED').update(status = "PENDING")
    return redirect('view_cart')