import django_filters
from django_filters import DateFilter

from .models import*

class Orderfilter(django_filters.FilterSet):
    class Meta:
        model = WorkOrder
        fields ='__all__'
        exclude = ['customer']