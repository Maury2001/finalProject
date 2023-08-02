import django_filters
from django_filters import DateFilter

from .models import*

class Orderfilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_created', lookup_expr='gte ')
    class Meta:
        model = WorkOrder
        fields ='__all__'
        exclude = ['customer']


class OrderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_created', lookup_expr='gte ')
    class Meta:
        model = WorkOrder
        fields ='__all__'
        exclude = ['description','date']
        


class Inventoryfilter(django_filters.FilterSet):
    
    class Meta:
        model = Inventory
        fields ='__all__'
        exclude =['date']
        #  


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['date','name','profile_pic']