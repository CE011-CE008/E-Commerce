from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
urlpatterns = [
        path('admin_home_index', views.admin_home_index, name='admin_home'),
        path('add', views.add, name='addProduct'),
        path('update',views.update, name='updateProduct'),
        path('delete', views.delete, name='deleteProduct'),
]