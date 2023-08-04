from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null= True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(default="prof.jpg",null=True, blank=True)
    email = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name if self.name else ''
    

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
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    device = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    spare_status= models.CharField(max_length=100, null=True, choices=SPARESTATUS)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer.name if self.customer.name else ''
    
    def save(self, *args, **kwargs):

        if self.status == 'completed':
            account_sid ='AC953e668ad54bca2a9d5e094dd89be91e'
            auth_token = '98557124cb9a63b233b229bb35b87364'
            
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                body=f"Hey {self.customer.name},\n your {self.device} is ready for pickup \n price is:{self.price}",
                                from_='+17622495418',
                                to=self.customer.phone
                            )

            print(message.sid)
        return super().save(*args, **kwargs) 
    


class Orders(models.Model):
    pending = 'pending'
    completed = 'completed'
    repair_in_progress = 'repair in progress'
    status_choice = [
        (pending ,'Pending'),
        (completed, 'Completed'),
        (repair_in_progress, 'Repair in Progress')
    ]

    available = 'available'
    unavailable = 'unavailable'
    requested = 'requested'
    spare_status = [
        (available, 'Available'),
        (unavailable, 'Unavailable'),
        (requested, 'Requested')
    ]

    # Rest of the model fields...
    customer = models.ForeignKey(Customer ,null=True, on_delete=models.CASCADE)
    device = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=status_choice)
    spare_status = models.CharField(max_length=100, null=True, choices=spare_status)

    def __str__(self):
        return self.customer.name if self.customer.name else ''



    


