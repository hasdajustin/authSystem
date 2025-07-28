from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home_view(request):
    return render(request, 'pages/index.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'uername already taken.')
            return redirect('register_view')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register_view')

        if password1 != password2:
            messages.error(request, 'Password do not match.')
            return redirect('register_view')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login_view')
    return render(request, 'pages/register.html')

def login_view(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        userPassword = request.POST.get('userpassword')
        print(userName, userPassword)

        user = authenticate(request, username = userName, password=userPassword)

        if user is not None:
            login(request, user)
            messages.success(request, f'Hello {user.username}')
            return redirect('home_view')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login_view')
    return render(request, 'pages/login.html')