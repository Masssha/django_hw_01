
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
import os


def index(request):
    return redirect(reverse('bus_stations'))

# content =

# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
with open('../data-398-2018-08-30.csv', newline='', encoding='utf-8') as f:
    rows = csv.DictReader(f)
    stations_list = []
    for station in rows:
        stations_list.append(station)
print(stations_list)

def bus_stations(request):
    paginator = Paginator(stations_list, 10)
    current_page = int(request.GET.get("page", 1))
    page = paginator.get_page(current_page)
    context = {
        'page': current_page,
        'bus_stations': page

    }
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    # context = {
    # #     'bus_stations': ...,
    # #     'page': ...,
    # }
    return render(request, 'stations/index.html', context)

