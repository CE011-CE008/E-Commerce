from django.shortcuts import render
from .models import ReceivedProduct, Cart
from home.models import Registration
from admin_home.models import Product_Details
from admin_home import models
from customer_home.models import cart_detail
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
    cart_det= cart_detail.objects.filter(cart_id=cart.cart_id)
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
    if customer is None:
        return render(request,'home/index.html')
    crt = Cart.objects.get(customer_id=customer.user_id)
    crt_det=cart_detail.objects.filter(cart_id=crt.cart_id,product_id= request.GET["product_id"]).first()
    if crt_det is not None:
        itm=crt_det.items
        itm+=1
        cart_detail.objects.filter(cart_id=crt.cart_id,product_id= request.GET["product_id"]).update(items=itm)
        return HttpResponseRedirect('/showCart')
    c = cart_detail()
    c.cart_id = crt.cart_id
    c.product_id = request.GET["product_id"]
    c.items=1
    c.save()
    return HttpResponseRedirect('/showCart')
def search(request):
    qry = request.GET["search"]
    p = Product_Details.objects.filter(Q(product_name__icontains=qry) | Q(description__icontains=qry) | Q(category__icontains=qry))
    result={'products':p,'search':qry}
    return render(request,'customer_home/buyProduct.html',result)
def read_more(request,slug):
    products = Product_Details.objects.filter(product_id=slug)
    return render(request,'customer_home/description.html', {'products': products})
def showCart(request):
    cart = Cart.objects.get(customer_id=request.COOKIES['user_id'])
    cart_det= cart_detail.objects.filter(cart_id=cart.cart_id)
    details = {}
    itm = {}
    items=0
    total=0
    for c in cart_det:
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
    cart_detail.objects.filter(cart_id=crt.cart_id, product_id=slug).delete()
    return HttpResponseRedirect('/showCart')