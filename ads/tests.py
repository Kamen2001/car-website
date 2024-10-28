from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import Ad, CarBrand, CarModel
from base.models import User, UserProfile



class AdViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.car_brand = CarBrand.objects.create(name='BMW')
        self.car_model = CarModel.objects.create(model_name='M2', brand=self.car_brand)

    def test_ad_new(self):
        response = self.client.post(reverse('ad_new'), {
            'title': 'New Ad',
            'contact_seller': 1234567890,
            'price': 20000.0,
            'car_brand': self.car_brand.id,
            'car_model': self.car_model.id,
            'is_published': True,
            'description': 'This is a new ad.'
        })
        self.assertEqual(response.status_code, HTTPStatus.FOUND)  
        self.assertTrue(Ad.objects.filter(title='New Ad').exists()) 

    def test_ad_view(self):
        ad = Ad.objects.create(
            title='Test Ad',
            contact_seller=1234567890,
            price=15000.0,
            created_by=self.user_profile,
            car_brand=self.car_brand,
            car_model=self.car_model,
            is_published=True
        )
        response = self.client.get(reverse('ad_view', kwargs={'pk': ad.pk}))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Test Ad')

    def test_ad_delete(self):
        ad = Ad.objects.create(
            title='Test Ad',
            contact_seller=1234567890,
            price=15000.0,
            created_by=self.user_profile,
            car_brand=self.car_brand,
            car_model=self.car_model,
            is_published=True
        )
        response = self.client.post(reverse('ad_delete', kwargs={'pk': ad.pk}))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)  
        self.assertFalse(Ad.objects.filter(pk=ad.pk).exists())
