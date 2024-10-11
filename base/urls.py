from django.urls import path
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from . import views
 

urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign_up, name='sign_up'),
    path('edit/', views.edit_profile, name='edit'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login')
]