from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Ad
from .form import NewAdForm
from base.models import UserProfile
from .filters import AdFilter

@login_required
def ad_new(request):
    if request.method == 'POST':
        form = NewAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            ad.created_by = user_profile
            ad.save()
            
            return redirect('ad_view', pk=ad.id)
    else:    
        form = NewAdForm()

    return render(request, 'ad_form.html', {'form': form})    

def ad_view(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    ad = get_object_or_404(Ad, pk=pk)
    context = {
        'ad': ad,
        'user_profile': user_profile
    }
    return render(request, 'ad_view.html', context)

@login_required
def ad_edit(request, pk): 
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        form = NewAdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad.ad_status = True
            ad.updated_at = timezone.now()
            form.save()
            return redirect('ad_view', pk=ad.id)
    else:    
        form = NewAdForm(instance=ad)

    context ={
        'form': form,
        'ad': ad,
        'editing': True
    }

    return render(request, 'ad_form.html', context)

@login_required
def ad_delete(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    ad = get_object_or_404(Ad, pk=pk, created_by=user_profile)
    ad.delete()

    return redirect('my_ads')

@login_required
def my_ads(request):
    user_profile = UserProfile.objects.get(user=request.user)
    ads = Ad.objects.filter(created_by=user_profile)
    
    return render(request, 'my_ads.html', {'ads': ads})

def ad_search(request):
    ad_filter = AdFilter(request.GET, queryset=Ad.objects.all()) 
    context ={
        'form': ad_filter.form,
        'ad_filter': ad_filter.qs
    }
    return render(request, 'ad_search_form.html', context)

@login_required
def ad_publish(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    ad = get_object_or_404(Ad, pk=pk, created_by=user_profile)
    ad.is_published = not ad.is_published 
    ad.published_at = timezone.now() if ad.is_published else None
    ad.save()
    return redirect('ad_view', pk=ad.pk)

@login_required
def ad_save(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    ad = get_object_or_404(Ad, pk=pk)
    if user_profile in ad.saved_by.all():
        ad.saved_by.remove(user_profile)
    else:
        ad.saved_by.add(user_profile)
    ad.save()
    return redirect('ad_view', pk=ad.pk)

