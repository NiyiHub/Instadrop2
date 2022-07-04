from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm, UserChangeForm


from django.conf import settings
from Logistics.models import Parcel
from django.contrib.auth import get_user_model
from .models import Profile


def register(request):
    context={} 
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form'] = form

    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})     


def login_user(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('Instadrop-home')

    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.success(request, ("You're logged out!"))
    return render(request, 'users/logout.html')


def history(request):
    parcels = Parcel.objects.filter(email)
    users = Profile.objects.filter(email)

    if parcels == users:
        return parcels 

    user_history = parcels
    return render(request, 'users/history.html', {'user_history': user_history})


@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
    # u_form = UserUpdateForm()
    # p_form = ProfileUpdateForm()
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)