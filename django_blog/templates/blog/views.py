from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm, ProfileForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # saves User and triggers profile creation signal
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    # Show and edit profile
    if request.method == 'POST':
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # optionally allow changing username/email via UserChangeForm or manual update
        if pform.is_valid():
            pform.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        pform = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/profile.html', {'pform': pform})