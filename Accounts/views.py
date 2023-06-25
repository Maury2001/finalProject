from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import * 

# Create your views here.


def dashboard(request):
    orders = WorkOrder.objects.all()

    total_orders = orders.count()
    pending = orders.filter(status='pending').count()
    completed = orders.filter(status='completed').count()

    context ={
        'total_orders': total_orders, 
        'pending': pending, 
         'completed': completed
    }

    return render(request, 'Accounts/dashboard.html', {'orders': orders} )

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    # orders = WorkOrder.objects.all()

    # content = Article.objects.get(id=article_id).content

    context = {'customer': customer, 'orders': orders, 'pk_test': pk_test }
    # 'orders': orders

    return render(request, 'Accounts/customer.html', context)


def inventory(request):
    inventory = Inventory.objects.all()
    return render(request, 'Accounts/inventory.html', {'inventory': inventory} ) 

def workorder(request):
    workorder = WorkOrder.objects.all()
    return render(request, 'Accounts/workorder.html', {'workorder': workorder} ) 

def createorder(request):
    form =  WorkOrderForm()

    if request.method == 'POST':
        # print ('printing request:' ,request.POST)
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render (request, 'Accounts/createorder.html', context)


def updateOrder(request):
    form = WorkOrderForm()

    context = {}
    return render(request, 'Accounts/createorder.html', context)






