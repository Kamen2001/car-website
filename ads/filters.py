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
    sort_by = django_filters.ChoiceFilter(
        choices=[
        ('newest', 'Newest'),
        ('oldest', 'Oldest'),
        ('price_up', 'Price: Low to High'),
        ('price_down', 'Price: High to Low'),
        ], 
        label="Sort by",
        method='filter_sort_by',
        required=False,
        initial='newest',
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'car_brand' in self.data:  
            car_brand_id = self.data.get('car_brand')
            if car_brand_id:
                car_brand_id = int(car_brand_id)
                self.filters['car_model'].queryset = CarModel.objects.filter(brand_id=car_brand_id).order_by('model_name')  

    def filter_sort_by(self, queryset, name, value):
        match(value):
            case('price_up'):
                return queryset.order_by('price')  
            case('price_down'):
                return queryset.order_by('-price')  
            case('newest'):
                return queryset.order_by('-created_at')  
            case('oldest'):
                return queryset.order_by('created_at')  
        return queryset
    

    class Meta:
        model = Ad
        fields = {
            'car_brand':['exact'],
            'car_model': ['exact'],
            'fuel_type': ['exact'],
            'price': ['lt', 'gt'],
            'mileage': ['lt', 'gt'],
            'year': ['lt', 'gt'], 
            'transmission': ['exact'],
            'horse_power': ['lt', 'gt'],
            'euro_standart': ['exact'],
            'location': ['icontains'],
        }