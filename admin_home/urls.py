"""Ecommerce URL Configuration

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
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
urlpatterns = [
        path('admin_indexPage/<slug:slug>', views.index, name='index'),
        path('addProduct/<slug:slug>', views.addProduct, name='addProduct'),
        path('viewProduct/<slug:slug>', views.viewProduct, name='viewProduct'),
        path('addProductPage/<slug:slug>', views.addProductPage, name='addProductPage'),
        path('updateProductPage/<slug:slug>', views.updateProductPage, name='updateProductPage'),
        path('DeleteProduct/<slug:slug>', views.deleteProduct, name='deleteProduct'),
        path('UpdateProduct/<slug:slug>', views.updateProduct, name='updateProduct'),
        path('updateProfilePage/<slug:slug>', views.updateProfilePage, name='updateProfilePage'),
        path('UpdateProfile/<slug:slug>', views.updateProfile, name='updateProfile'),
        path('signout', views.signout, name='signout'),
        
]

