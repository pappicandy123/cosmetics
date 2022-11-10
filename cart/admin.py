from django.contrib import admin
from .models import Shipping, Shopcart,Payment
# Register your models here.

@admin.register(Shopcart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price','quantity','amount','cart_no','item_carted', 'paid', 'created']
    readonly_fields = ['user', 'product', 'price','quantity','amount','cart_no', 'paid', 'created']



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['status','user', 'total', 'cart_no', 'pay_code', 'paid',  'created', 'admin_note', 'updated' ]
    readonly_fields = ['user', 'total', 'cart_no', 'pay_code', 'paid', 'status', 'created', 'updated' ]


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'phone', 'billing_address', 'delivery_address','city', 'state' ]
    readonly_fields = ['user', 'first_name', 'last_name', 'email', 'phone', 'billing_address', 'delivery_address','city', 'state' ]