from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import login
from .forms import RegisterForm

# login/views.py

from django.shortcuts import render


def login_view(request):
    form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index/')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'login/logout.html')
