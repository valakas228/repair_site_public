from django.shortcuts import render
from django.apps import apps
PriceList = apps.get_model('store', 'PriceList')

def index(request):
    price_list = PriceList.objects.all()
    return render(request, 'main/index.html', {'price_list': price_list} )


