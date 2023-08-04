from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(WorkOrder)
admin.site.register(Inventory)
admin.site.register(Orders)
