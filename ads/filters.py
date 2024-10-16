import django_filters
from django import forms
from .models import Ad, CarBrand, CarModel


class AdFilter(django_filters.FilterSet):

    car_brand = django_filters.ModelChoiceFilter(
        queryset=CarBrand.objects.all(),
        label="Car Brand",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_car_brand'})
    )
    car_model = django_filters.ModelChoiceFilter(
        queryset=CarModel.objects.none(),  
        label="Car Model",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_car_model'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'car_brand' in self.data:  
            try:
                car_brand_id = int(self.data.get('car_brand'))
                self.filters['car_model'].queryset = CarModel.objects.filter(brand_id=car_brand_id).order_by('model_name')
            except (ValueError, TypeError):
                pass  

    sort_by = django_filters.ChoiceFilter(
        choices=[
        ('newest', 'Newest'),
        ('oldest', 'Oldest'),
        ('price_up', 'Price: Low to High'),
        ('price_down', 'Price: High to Low'),
        ], 
        label="Sort by",
        method='filter_sort_by',
        required=False
    )
    
    def filter_sort_by(self, queryset, name, value):
        if value == 'price_up':
            return queryset.order_by('price')  
        elif value == 'price_down':
            return queryset.order_by('-price')  
        elif value == 'newest':
            return queryset.order_by('-created_at')  
        elif value == 'oldest':
            return queryset.order_by('created_at')  
        return queryset
    

    class Meta:
        model = Ad
        fields = {
            'car_brand':['exact'],
            'car_model': ['exact'],
            'price': ['lt', 'gt'],
            'mileage': ['lt', 'gt'],
            'year': ['lt', 'gt'], 
            'fuel_type': ['exact'],
            'transmission': ['exact'],
            'horse_power': ['lt', 'gt'],
            'euro_standart': ['exact'],
            'location': ['icontains'],
        }