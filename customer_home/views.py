from django.shortcuts import render
from .models import ReceivedProduct, Cart, Cart_Details
from home.models import Registration
from admin_home.models import Product_Details
from admin_home import models
from django.http import HttpResponseRedirect
from django.db.models import Q
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
    crt = Cart.objects.get(customer_id=request.COOKIES["user_id"])
    carts = Cart_Details.objects.filter(cart_id=crt.cart_id)
    items=0
    total = 0
    products = {}
    for cart in carts:
        product = Product_Details.objects.get(product_id=cart.product_id)
        products[product.product_name] = product.price
        items=items+cart.items
        total = total + cart.price
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
    customer = Registration.objects.get(user_id=request.COOKIES['user_id'])
    if customer is None:
        return render(request,'home/index.html')
    crt = Cart.objects.get(customer_id=customer.user_id)
    print(crt.customer_id)
    c = Cart_Details()
    #c.customer_id=customer.user_id
    #c.customer_name = customer.name
    c.cart_id = crt.cart_id
    c.product_id = request.GET["product_id"]
    c.items = 1
    product = models.Product_Details.objects.get(product_id=request.GET["product_id"])
    print (product.price)
    c.price = product.price
    c.save() 
    return render(request,'customer_home/addTocart.html')
def logout(request):
    return HttpResponseRedirect('signout')
def search(request):
    #result={}
    #p=Product_Details.objects.all()
    qry = request.GET["search"]
    p = Product_Details.objects.filter(Q(product_name__icontains=qry) | Q(description__icontains=qry) | Q(category__icontains=qry))
    # results= Product_Details.objects.filter(lookups).distinct()
    result={'products':p,'search':qry}
    return render(request,'customer_home/buyProduct.html',result)