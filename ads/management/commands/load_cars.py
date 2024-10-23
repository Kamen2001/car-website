import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from ads.models import CarBrand, CarModel

class Command(BaseCommand):
    help = 'Import car brands and models from CSV file'

    def handle(self, *args, **kwargs):
        file_path = settings.BASE_DIR / 'ads' / 'data' / 'car_data.csv' 

        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) 
            for row in reader:
                brand_name = row[0]
                models = row[1:]  
                brand, created = CarBrand.objects.get_or_create(name=brand_name)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created new brand: {brand_name}'))
                for model_name in models:
                    model_name = model_name.strip()  
                    CarModel.objects.get_or_create(brand=brand, model_name=model_name)

