from django.contrib import admin

from .models import *

admin.site.register(Food)   
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)