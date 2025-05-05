from django.db import models
from management.models import User, Menu

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    customer_city = models.CharField(max_length=50)
    customer_phone = models.IntegerField(default=0)
    def __str__(self):
        return self.customer_name
    

class Orders(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default='ADDED')



    def total_price(self):
        return self.name.food_price * self.quantity
    
    def __str__(self):
        return f'{self.quantity} x {self.name.food_name}'

