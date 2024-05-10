from django.shortcuts import render
from .models import Product

def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products':products})