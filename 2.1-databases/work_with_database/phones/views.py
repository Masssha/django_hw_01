from django.shortcuts import render, redirect
import csv
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    phone_list = phones

    sorting = request.GET.get('sort')
    if sorting == 'max_price':
        phone_list = sorted(phones, key=lambda x: x.price, reverse=True)
    if sorting == 'min_price':
        phone_list = sorted(phones, key=lambda x: x.price)
    if sorting == 'name':
        phone_list = sorted(phones, key=lambda x: x.name)
    context = {
        'phones': phone_list
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
