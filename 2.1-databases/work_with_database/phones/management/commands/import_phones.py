import csv
import uuid
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = csv.DictReader(file, delimiter=';')

            for phone in phones:
                print(phone)
                # slug = uuid.uuid4()
                release_date = datetime.strptime(phone['release_date'], '%Y-%m-%d')
                slug = str(phone['name']).replace(' ', '-')
                Phone.objects.create(name=phone['name'], image=phone['image'], price=phone['price'], release_date=release_date, lte_exists=phone['lte_exists'], slug=slug)
            # # # TODO: Добавьте сохранение модели

