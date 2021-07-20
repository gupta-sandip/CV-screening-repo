from typing import Text
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        Password = request.POST['Password']
        password2 = request.POST['Password2']

        if Password == password2:
            if User.objects.filter(email=email).exists():
                messages.imfo(request, 'Email Already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=Password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password is not same')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credential Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def counter(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
    return render(request, 'counter.html', {'posts': posts})


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
