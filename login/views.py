from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome! ' + username)
            return redirect('../')
        else:
            messages.info(request, 'Email or Password is Incorrect')

    context = {}
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')
