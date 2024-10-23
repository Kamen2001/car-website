from django.db import models
from django.utils import timezone
from base.models import UserProfile


class CarBrand(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    model_name = models.CharField(max_length=15)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Ad(models.Model): 
    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('Semi Automatic', 'Semi Automatic'),
    ]
    
    FUEL_TYPE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Gas/Petrol', 'Gas/Petrol'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    ]

    EURO_STANDART_CHOICES = [
        ('Euro 1', 'Euro 1'), 
        ('Euro 2', 'Euro 2'), 
        ('Euro 3', 'Euro 3'), 
        ('Euro 4', 'Euro 4'),
        ('Euro 5', 'Euro 5'),
        ('Euro 6', 'Euro 6'),
    ]

    ad_status = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=20)
    contact_seller = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=False, default=timezone.now)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.CharField(blank=True, max_length=100)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='models')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    horse_power = models.PositiveIntegerField(null=True, blank=True)
    year = models.PositiveBigIntegerField(null=True, blank=True)
    euro_standart = models.CharField(blank=True, max_length=15, choices=EURO_STANDART_CHOICES)
    mileage = models.PositiveIntegerField(null=True, blank=True, help_text='km')
    fuel_type = models.CharField(blank=True, max_length=10, choices=FUEL_TYPE_CHOICES)
    transmission = models.CharField(blank=True, max_length=15, choices=TRANSMISSION_CHOICES)
    car_image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    saved_by = models.ManyToManyField(UserProfile, related_name='saved_ads', blank=True)
    liked_by = models.ManyToManyField(UserProfile, related_name="likes", blank=True)

    def __str__(self):
        return self.title
    