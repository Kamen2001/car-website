from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, EditUserProfileForm
from .models import UserProfile

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    is_edit = False
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

    context = {
        'form': form,  
        'is_update': is_edit
    }

    return render(request, 'sign_up.html', context)

@login_required
def logout_view(request):  
    logout(request)

    return redirect('index') 

@login_required
def edit_profile(request):
    is_edit = True
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  
            return redirect('index')  

    else:
        form = EditUserProfileForm(instance=request.user)  

    context = {
        'form': form,  
        'is_update': is_edit
    }

    return render(request, 'sign_up.html', context)  