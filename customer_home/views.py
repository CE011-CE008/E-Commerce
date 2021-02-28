from django.shortcuts import render
from .models import ReceivedProduct, Cart
from home.models import Registration
from admin_home.models import Product_Details
from admin_home import models
from django.http import HttpResponseRedirect
# Create your views here.
def customer_home_index(request):
    return render(request,'customer_home/homepage.html')
def sellProduct(request):
    return render(request,'customer_home/SellProduct.html')
def success(request):
    p = ReceivedProduct()
    p.product_name = request.POST.get('product')
    p.description = request.POST.get('description')
    p.price = request.POST.get('price')
    p.images = request.FILES['images']
    p.save()
    return render(request,'customer_home/success.html')
def payment(request):
    carts = Cart.objects.filter(customer_id=request.COOKIES['user_id'])
    items=0
    total = 0
    products={}
    #product_price=[]
    for cart in carts:
        product = models.Product_Details.objects.get(product_id=cart.product_id)
        products[product.product_name] = product.price
        items+=cart.total
        total = total + cart.amount
    context = {
    'products': products,
    'items': items,
    'total': total
    }
    return render(request,'customer_home/payment.html',context)
def buy(request):
    products = Product_Details.objects.all()
    return render(request,'customer_home/buyProduct.html', {'products': products})
def cart(request):
    customer = Registration.objects.filter(user_id=request.COOKIES['user_id'])[0]
    if customer is None:
        HttpResponseRedirect('/login')
    c = Cart()
    c.customer_id=customer.user_id
    c.customer_name = customer.name
    c.product_id = request.GET["product_id"]
    c.total = 1
    product = models.Product_Details.objects.get(product_id=request.GET["product_id"])
    print (product.price)
    c.amount = product.price
    c.save() 
    return render(request,'customer_home/addTocart.html',{'product_id': request.GET["product_id"]})