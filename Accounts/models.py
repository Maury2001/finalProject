from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self) :
        return self.name
    

class Inventory (models.Model):
    reference_no = models.AutoField(primary_key=True, default=0)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    quantity = models.FloatField(null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) :
        return (self.name + '' + self.category)

class WorkOrder(models.Model):
    STATUS= {
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('repair in progress', 'repair in progress')
    }

    SPARESTATUS= {
        ('available', 'available'),
        ('unavailable', 'unavailable'),
        ('requested', 'requested')
    }
    # ref = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    customer = models.ForeignKey(Customer ,null=True, on_delete=models.CASCADE)
    device = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    spare_status= models.CharField(max_length=100, null=True, choices=SPARESTATUS)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) :
        return self.customer.name +"  "+ self.device

    


