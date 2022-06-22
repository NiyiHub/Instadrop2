from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm


def register(request):
    context={} 
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form'] = form

    else:
        form = RegistrationForm()
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


def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your account has been updated!'))
            return redirect('Instadrop-home')
    
    else:
        form = ProfileUpdateForm(request.POST)
    return render(request, 'users/profile.html', {'form':form})
