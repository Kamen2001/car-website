import django_filters
from .models import Ad


class AdFilter(django_filters.FilterSet):
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