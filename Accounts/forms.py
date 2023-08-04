from django.forms import ModelForm
from .models import WorkOrder, Inventory, Customer,Orders
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class WorkOrderForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label="Select a customer")
    class Meta:
        model = WorkOrder
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model= Orders
        fields='__all__'



class CreateuserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']



class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields= '__all__'



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        exclude = ['user']
