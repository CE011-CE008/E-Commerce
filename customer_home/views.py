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
    customer = Registration.objects.filter(user_id=request.COOKIES['user_id'])[0]
    p.seller_name = customer.name
    p.seller_email = customer.email
    p.product_name = request.POST.get('product')
    p.description = request.POST.get('description')
    p.price = request.POST.get('price')
    p.images = request.FILES['images']
    p.save()
    return render(request,'customer_home/success.html')
def payment(request):
    cart = Cart.objects.get(customer_id=request.COOKIES['user_id'])
    cart_det= Cart_Details.objects.filter(cart_id=cart.cart_id)
    details = {}
    itm = {}
    items=0
    total=0
    for c in cart_det:
        product = Product_Details.objects.filter(product_id=c.product_id)[0]
        details[c.product_id]=product
        itm[c.product_id]=c.items
        items += c.items
        total = total + product.price*c.items
    
    context={
        'product':details,
        'itm': itm,
        'items':items,
        'total':total
    }
    return render(request,'customer_home/payment.html',context)
def buy(request):
    products = Product_Details.objects.all()
    return render(request,'customer_home/buyProduct.html', {'products': products})
def cart(request):
    customer = Registration.objects.get(user_id=request.COOKIES['user_id'])
    print(request.COOKIES['user_id'])
    if customer is None:
        return render(request,'home/index.html')
    ct = Cart.objects.get(customer_id=customer.user_id)
    #print(crt.customer_id)
    crt = Cart_Details.objects.filter(cart_id=ct.cart_id,product_id=request.GET['product_id']).first()
    if crt is not None:
        itm = crt.items
        itm+=1
        Cart_Details.objects.filter(cart_id=crt.cart_id,product_id=request.GET['product_id']).update(items=itm)
        return HttpResponseRedirect('/showCart')
    #c.customer_id=customer.user_id
    #c.customer_name = customer.name
    c = Cart_Details()
    c.cart_id = ct.cart_id
    c.product_id = request.GET["product_id"]
    c.items = 1
    product = models.Product_Details.objects.get(product_id=request.GET["product_id"])
    print (product.price)
    #c.price = product.price
    c.save() 
    return HttpResponseRedirect('/showCart')
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

def showCart(request):
    cart = Cart.objects.get(customer_id=request.COOKIES['user_id'])
    cart_details = Cart_Details.objects.filter(cart_id=cart.cart_id)
    details = {}
    itm = {}
    items=0
    total=0
    for c in cart_details:
        product = Product_Details.objects.filter(product_id=c.product_id)[0]
        details[c.product_id]=product
        itm[c.product_id]=c.items
        items += c.items
        total = total + product.price
    
    context={
        'product':details,
        'itm': itm,
        'items':items,
        'total':total
    }
    return render(request,'customer_home/showCart.html',context)

def remove_from_cart(request,slug):
    crt = Cart.objects.get(customer_id=request.COOKIES['user_id'])
    Cart_Details.objects.filter(cart_id=crt.cart_id, product_id=slug).delete()
    return HttpResponseRedirect('/showCart')

def read_more(request,slug):
    products = Product_Details.objects.filter(product_id=slug)
    return render(request,'customer_home/description.html', {'products': products})