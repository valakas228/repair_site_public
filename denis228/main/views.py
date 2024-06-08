from django.shortcuts import render
from django.apps import apps
from store.forms import EstimateForm
from store.models import Product, City

PriceList = apps.get_model('store', 'PriceList')

def index(request):
    price_list = PriceList.objects.all()
    estimate_form = EstimateForm()
    products = Product.objects.all()
    cities = City.objects.all()
    return render(request, 'main/index.html', {'price_list': price_list, 'estimate_form': estimate_form,'products': products, 'cities': cities})
