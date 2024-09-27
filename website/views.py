from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm

def home(request):
  if request.user.is_authenticated:
    return render(request, 'home.html', {})
  else:
    return redirect('login')

def login_user(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)

        return redirect('home')
      else:
        messages.error(request, 'Invalid credentials')

        return redirect('login')
    else:
      return render(request, 'login.html', {})

def logout_user(request):
  logout(request)

  return redirect('login')

def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)

    if form.is_valid():
      form.save()

      return redirect('login')
    else:
      return render(request, 'register.html', {'form': form})
  else:
    form = SignUpForm()

    return render(request, 'register.html', {'form': form})