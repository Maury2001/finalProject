from django.forms import ModelForm
from .models import WorkOrder

class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrder
        fields = '__all__'