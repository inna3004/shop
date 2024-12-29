from django.contrib import admin
from flowers.models import Flower, Order, OrderItem


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
   pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
   pass