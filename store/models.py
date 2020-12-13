from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

        

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=50, null=True)


    #  def __str__(self):
    #     return self.Food.name



class OrderItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

#class for UDT generation.  
