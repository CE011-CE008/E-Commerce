from django.shortcuts import render
from .models import ReceivedProduct
from admin_home.models import Product_Details
# Create your views here.
def customer_home_index(request):
    return render(request,'customer_home/homepage.html')
def sellProduct(request):
    return render(request,'customer_home/SellProduct.html')
def payment(request):
    p = ReceivedProduct()
    p.product_name = request.POST.get('product')
    p.description = request.POST.get('description')
    p.price = request.POST.get('price')
    p.images = request.POST.get('images')
    p.save()
    return render(request,'customer_home/payment.html')
def buy(request):
    products = Product_Details.objects.all()
    return render(request,'customer_home/buyProduct.html', {'products': products})
def cart(request):
    c = cart()
    
    return render(request,'customer_home/addTocart.html')