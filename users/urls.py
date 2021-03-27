"""Defines URL patterns for users"""

from webbrowser import register

from django import urls
from django.urls import include, path

from . import views

app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    
]
