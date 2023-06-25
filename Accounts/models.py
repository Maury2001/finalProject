from django.db import models
import uuid

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self) :
        return self.name
    

class Inventory (models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) :
        return self.name + '' + self.category

class WorkOrder(models.Model):
    STATUS= {
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('ready for pickup', 'ready for pickup')
    }
    # ref = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    device = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    


