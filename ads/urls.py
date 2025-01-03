from django.urls import path
from . import views

urlpatterns=[
    path('new/', views.ad_new, name='ad_new'),
    path('my_ads/', views.my_ads, name='my_ads'),
    path('<int:pk>/', views.ad_view, name='ad_view'),
    path('<int:pk>/edit', views.ad_edit, name='ad_edit'),
    path('<int:pk>/delete', views.ad_delete, name='ad_delete'),
    path('<int:pk>/publish', views.ad_publish, name='ad_publish'),
    path('<int:pk>/save', views.ad_save, name='ad_save'),
    path('<int:pk>/like', views.ad_like, name='ad_like'),
    path('search/', views.ad_search, name='ad_search_form'),
    path('load-car-models/', views.load_car_models, name='load_car_models')
    
]