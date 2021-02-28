from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
        path('customer_home_index', views.customer_home_index, name='customer_home'),
        path('sellProduct',views.sellProduct, name='sellproduct'),
        path('payment', views.payment, name='payment'),
        path('buy', views.buy, name='buy'),
        path('cart', views.cart, name='cart'),
        path('success',views.success,name='success'),
]