from django.http import HttpResponse
from .models import Products
from django.shortcuts import render


def index(request):
    products = Products.objects.all()
    return render(request, 'shop.html', {'products': products})


def product(request):
    products = Products.objects.all()
    return render(request, 'product_preview.html', {'products': products})
