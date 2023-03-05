from django.contrib import admin
from .models import Product
from .models import Offer
from .models import Products
from .models import Customer
from .models import OrderContents
from .models import OrderHistory


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image_url', 'category', 'rating')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ()


class OrderContentsAdmin(admin.ModelAdmin):
    list_display = ()


class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(OrderContents, OrderContentsAdmin)
admin.site.register(OrderHistory, OrderHistoryAdmin)
