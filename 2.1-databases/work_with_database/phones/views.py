from django.shortcuts import render, redirect
import csv
from phones.models import Phone

# def create_phones(request):
#     with open('..\phones.csv', encoding="utf-8") as csvfile:
#         phones = csv.reader(csvfile, delimiter=';')
#         phones_list = list(phones)
#         # print(phones_list)
#         for phone in phones_list:
            # Phone.objects.create(name=phone[1], image=phone[2], price=phone[3], release_date=phone[4], lte_exists=phone[5])

# def check():
#     phones = Phone.objects.all()
#     for p in phones:
#         print(p.name)
# check()


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
