from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('registration/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
]