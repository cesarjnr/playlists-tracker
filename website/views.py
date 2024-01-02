from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
  return render(request, 'home.html', {})

def login_user(request):
  if (request.user.is_authenticated):
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