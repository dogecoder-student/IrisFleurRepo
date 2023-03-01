from django.http import HttpResponse
from . models import Product
from django.shortcuts import render


def index(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
