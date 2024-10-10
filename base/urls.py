from django.urls import path
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from . import views
 

urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign_up, name='sign_up'),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login')
]