"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('blog-single.html', views.blog_single, name='blog-single'),
    path('blog.html', views.blog, name='blog'),
    path('cases.html', views.cases, name='cases'),
    path('contact.html', views.contact, name='contact'),
    path('services.html', views.services, name='services'),
    path('cards.html', views.cards, name='cards'),
]
