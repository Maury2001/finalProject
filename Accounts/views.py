from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db import models
from .decorators import unauthenticated_user, allowed_user,admin_only
from .forms import WorkOrderForm, CreateuserForm, InventoryForm, CustomerForm,OrderForm
from .filters import Orderfilter, Inventoryfilter, CustomerFilter, OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.

@unauthenticated_user
def registration(request):

    form = CreateuserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CreateuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name ='customers')
            user.groups.add(group)
            Customer.objects.create(user = user)
            
            messages.success(request, 'Account created for ' + username)
            return redirect('login')

    return render(request, 'Accounts/registration.html', context)


@unauthenticated_user
def Login(request):
    form = CreateuserForm()
    if request.method == 'POST':
        form = CreateuserForm(request.POST)
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {'form': form}

    return render(request, 'Accounts/login.html', context)


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
# @allowed_user(allowed_roles = ['admin','customers'])
@admin_only
def dashboard(request):
    orders = WorkOrder.objects.all()
    customer = Customer.objects.all()
    customer_count = customer.count()
    inventory = Inventory.objects.all()

    total_orders = orders.count()
    total_inventory = inventory.count()

    pending = orders.filter(status='pending').count()
    completed = orders.filter(status='completed').count()

    context = {
        'total_orders': total_orders,
        'pending': pending,
        'completed': completed,
        'orders': orders,
        'customer': customer,
        'customer_count': customer_count,
        'inventory': inventory,
        'total_inventory': total_inventory
    }

    return render(request, 'Accounts/dashboard.html', context)


@login_required(login_url='login')
def allCustomers(request):

    customer = Customer.objects.all()

    myfilter = CustomerFilter(request.GET, queryset= customer)
    customer = myfilter.qs
    return render(request, 'Accounts/allCustomers.html', {'customer': customer, 'myfilter': myfilter})


@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id= pk)
    order = WorkOrder.objects.filter(id= pk)
   
    orders = WorkOrder.objects.all()
    order_count = order.count()
    

    myfilter = Orderfilter(request.GET, queryset=orders)
    orders = myfilter.qs

    # content = Article.objects.get(id=article_id).content

    context = {'customer': customer,
               'orders': orders,
               'order': order,
               'order_count': order_count,
               'myfilter': myfilter,
               }
    #

    return render(request, 'Accounts/customer.html', context)

@login_required(login_url='login')
def InventoryAdjustment(request):

    form = InventoryForm()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    context = {'form': form}
    return render(request, 'Accounts/InventoryAdjustment.html', context)


@login_required(login_url='login')
def inventory(request):
    inventory = Inventory.objects.all()

    myfilter = Inventoryfilter(request.GET, queryset=inventory)
    inventory = myfilter.qs
    context = {'inventory': inventory, 'myfilter': myfilter}
    return render(request, 'Accounts/inventory.html', context)



@login_required(login_url='login')
def workorder(request):
    workorder = WorkOrder.objects.all()

    myfilter = OrderFilter(request.GET, queryset=workorder)
    workorder = myfilter.qs

    context ={'workorder': workorder, 'myfilter': myfilter}
    return render(request, 'Accounts/workorder.html', context)



@login_required(login_url='login')
def createorder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = WorkOrderForm(initial={'customer': customer})

    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Accounts/createorder.html', context)



@login_required(login_url='login')
def createorder2(request):

    
    form = WorkOrderForm()

    if request.method == 'POST':
        # print ('printing request:' ,request.POST)
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Accounts/createorder.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles = ['admin'])
def updateOrder(request, pk):
    order = WorkOrder.objects.get(id=pk)
    form = WorkOrderForm(instance=order)
    if request.method == 'POST':
        form = WorkOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Accounts/order_form.html', context)


def delete(request, pk):
    order = WorkOrder.objects.get(id=pk)
    context = {'item': order}

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'Accounts/delete.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles = ['admin'])
def createOrder(request):

    form = WorkOrderForm()
    if request.method == 'POST':
        # print('printing post', request.POST)
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Accounts/order_form.html', context)



def base(request):
    workorder = WorkOrder.objects.all()
    myfilter = OrderFilter(request.GET, queryset=workorder)
    workorder = myfilter.qs

    myform = OrderForm()
    if request.method == 'POST':
        form = WorkOrderForm()
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'workorder':workorder, 'myfilter': myfilter,'myform':myform}

    return render(request, 'Accounts/base3.html',context)


def index(request):

    context = {
        'css_file': 'css/sb-admin-2.css',
        'js_file': 'js/script1.js',
    }

    return render(request, 'Accounts/index.html', context)


def dash(request):

    context = {
        'css_file': 'css/sb-admin-2.css',
        'js_file': 'js/script1.js',
    }

    return render(request, 'Accounts/dash2.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles = ['customers'])
def UserPage(request):
    orders = WorkOrder.objects.filter(customer=request.user.customer)

    total_orders = orders.count()  
    customer = request.user.customer
    form = CustomerForm(instance= customer)
    pending = orders.filter(status='pending').count()
    completed = orders.filter(status='repair in progress').count()

    if request.method == 'POST':
        form =CustomerForm(request.POST, request.FILES, instance= customer)
        if form.is_valid():
            form.save()
            return redirect('user')

    print('orders' , orders)
    context = {'orders': orders ,
               'total_orders': total_orders,
               'pending': pending,
               'completed': completed,
               'form': form
               }

    return render(request, 'Accounts/user.html', context)



def engineer(request):
    orders = WorkOrder.objects.all()
    
    

    pend = orders.filter(status='pending')
    pending = orders.filter(status='pending').count()
    completed = orders.filter(status='completed').count()

    context = { 'pending': pending,
        'completed': completed,
        'orders': orders,
        'pend': pend}

    return render(request, 'Accounts/engineer.html', context)
