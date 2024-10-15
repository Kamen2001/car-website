from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, EditUserProfileForm
from .models import UserProfile
from ads.models import Ad

def index(request):
    latest_ads = Ad.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'index.html', {'latest_ads': latest_ads})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES) 
        if form.is_valid():
            user = form.save(commit=False)  
            user.save()  
            if form.cleaned_data.get('profile_image'):
                profile_image = form.cleaned_data.get('profile_image')
                UserProfile.objects.create(user=user, profile_image=profile_image)
            else:
                UserProfile.objects.create(user=user)

            return redirect('/login/') 
    else:
        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'sign_up.html', context)

@login_required
def logout_view(request):  
    logout(request)

    return redirect('index') 

@login_required
def profile(request, username):
    if request.user.username != username:

        return redirect('index')
    user_profile = get_object_or_404(UserProfile, user=request.user)
    saved_ads = user_profile.saved_ads.all()
    context={
        'user_profile': user_profile,
        'saved_ads': saved_ads
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request, username):
    user = request.user  
    user_profile = get_object_or_404(UserProfile, user=user)
    
    if request.user.username != username:
        return redirect('index')
    
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 and password1 == password2:
                user.set_password(password1) 
            else:
                form.add_error('password2', 'Паролите не съвпадат.')
            user.save()
            user_profile.profile_image = form.cleaned_data['profile_image']
            user_profile.save()  
            update_session_auth_hash(request, user) 
            return redirect('index')  
    else:
        form = EditUserProfileForm(instance=user)

    context = {
        'form': form,  
        'username': user_profile.user.username  
    }

    return render(request, 'edit_profile.html', context)