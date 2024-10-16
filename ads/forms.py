from django import forms
from .models import Ad, CarBrand, CarModel

INPUT_CLASSES = 'w-ful py-4 px-4 rounded-xl border'
INPUT_CLASSES_SELECT = 'w-ful px-6 rounded-xl border'

class NewAdForm(forms.ModelForm):
    car_brand = forms.ModelChoiceField(queryset=CarBrand.objects.all(), required=True)

    class Meta:
        model = Ad 
        fields = [
            'title', 'car_brand', 'car_model', 'description', 'price', 'car_image', 'horse_power',
            'year', 'mileage', 'euro_standart', 'fuel_type', 'transmission', 'contact_seller', 
            'location'
        ] 
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'car_brand': forms.Select(attrs={'class': INPUT_CLASSES_SELECT}), 
            'car_model': forms.Select(attrs={'class': INPUT_CLASSES_SELECT}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'car_image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'horse_power': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'year': forms.NumberInput(attrs={'class': INPUT_CLASSES_SELECT}),
            'mileage': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'euro_standart': forms.Select(choices=Ad.EURO_STANDART_CHOICES, attrs={'class': INPUT_CLASSES_SELECT}),
            'fuel_type': forms.Select(choices=Ad.FUEL_TYPE_CHOICES, attrs={'class': INPUT_CLASSES_SELECT}),
            'transmission': forms.Select(choices=Ad.TRANSMISSION_CHOICES, attrs={'class': INPUT_CLASSES_SELECT}),
            'contact_seller': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'location': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'car_brand' in self.data:
            try:
                car_brand_id = int(self.data.get('car_brand'))
                self.fields['car_model'].queryset = CarModel.objects.filter(brand_id=car_brand_id).order_by('model_name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['car_model'].queryset = self.instance.car_brand.models.order_by('car_model')
            self.fields['car_model'].initial = self.instance.car_model