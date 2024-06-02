from django.shortcuts import render, redirect
import csv
from .models import Phone

# def create_phones(request):
#     with open('..\phones.csv', encoding="utf-8") as csvfile:
#         phones = csv.reader(csvfile, delimiter=';')
#         phones_list = list(phones)
#         # print(phones_list)
#         for phone in phones_list:
            # Phone.objects.create(name=phone[1], image=phone[2], price=phone[3], release_date=phone[4], lte_exists=phone[5])




def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
