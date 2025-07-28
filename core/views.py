from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'pages/index.html')

def register_view(request):
    return render(request, 'pages/register.html')

def login_view(request):
    return render(request, 'pages/login.html')