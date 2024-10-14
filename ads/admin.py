from django.contrib import admin
from .models import CarBrand, CarModel, Ad

admin.site.register(Ad)
admin.site.register(CarBrand)
admin.site.register(CarModel)
