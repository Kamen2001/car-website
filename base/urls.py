from django.urls import path
from .forms import LoginForm
from django.contrib import auth
from . import views
 

urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign_up, name='sign_up'),
    path('login/', auth.views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login')
]