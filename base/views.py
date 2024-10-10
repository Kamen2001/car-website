from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignUpForm
from .models import UserProfile

def index(request):
    return render(request, 'base/index.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  # Добави request.FILES за файлове
        if form.is_valid():
            user = form.save(commit=False)  # Спираме временно запазването на потребителя
            user.save()  # Запазваме потребителя
            # Ако има качена снимка, добавяме профил със снимката
            if form.cleaned_data.get('profile_image'):
                profile_image = form.cleaned_data.get('profile_image')
                UserProfile.objects.create(user=user, profile_image=profile_image)
            else:
                # Създаваме потребителски профил без снимка
                UserProfile.objects.create(user=user)
            
            return redirect('/login/') 
    else:
        form = SignUpForm()

    return render(request, 'base/sign_up.html', {'form': form})

def logout_view(request):  
    logout(request)
    
    return redirect('index')