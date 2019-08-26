from django.contrib import admin

# Register your models here.
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class Oplata(admin.TabularInline):
    model = Oplata
    raw_id_field = ['name']

class Delivery(admin.TabularInline):
    model = Delivery
    raw_id_field = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline,Oplata,Delivery,]


admin.site.register(Order, OrderAdmin)
admin.site.register(DeliveryMetod) 

admin.site.register(OplataMetod) 