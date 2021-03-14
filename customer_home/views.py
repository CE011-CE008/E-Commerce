from django.shortcuts import render, redirect
from .models import ReceivedProduct, Cart, Cart_Details, Order, Order_Details
from home.models import Registration
from admin_home.models import Product_Details
from admin_home import models
from django.http import HttpResponseRedirect
from django.db.models import Q
import smtplib
from email.message import EmailMessage
# Create your views here.
def customer_home_index(request):
    return buy(request)
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
    cart_det= Cart_Details.objects.filter(cart_id=cart)
    if not cart_det.exists():
        return HttpResponseRedirect('customer_home_index')
    details = {}
    itm = {}
    items=0
    total=0
    for c in cart_det:
        product = Product_Details.objects.filter(product_id=c.product_id.product_id)[0]
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
    return render(request,'customer_home/homepage.html', {'products': products})
def cart(request,slug):
    customer = Registration.objects.get(user_id=request.COOKIES['user_id'])
    if customer is None:
        return render(request,'home/index.html')
    crt = Cart.objects.get(customer_id=customer)
    crt_det=Cart_Details.objects.filter(cart_id=crt,product_id=slug).first()
    if crt_det is not None:
        itm=crt_det.items
        itm+=1
        Cart_Details.objects.filter(cart_id=crt,product_id= slug).update(items=itm)
        return HttpResponseRedirect('/showCart')
    c = Cart_Details()
    c.cart_id = crt
    product = Product_Details.objects.filter(product_id=slug).first()
    c.product_id = product
    c.items=1
    c.save()
    cart = Cart_Details.objects.filter(cart_id=crt)
    items=0
    for c in cart:
        items+=c.items
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
    cart_details = Cart_Details.objects.filter(cart_id=cart)
    details = {}
    itm = {}
    items=0
    total=0
    for c in cart_details:
        product = Product_Details.objects.filter(product_id=c.product_id.product_id)[0]
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

def place_order(request):
    odr=Order()
    usr=Registration.objects.filter(user_id=request.COOKIES['user_id']).first()
    odr.user_id=usr
    odr.status='pending'
    odr.amount=0
    odr.save()
    odr=Order.objects.filter(user_id=request.COOKIES['user_id']).first()
    cart = Cart.objects.get(customer_id=request.COOKIES['user_id'])
    cart_det= Cart_Details.objects.filter(cart_id_id=cart).all()
    print (cart_det)
    amount=0
    for p in cart_det:
        odr_det=Order_Details()
        odr_det.order_id=odr
        prdt=Product_Details.objects.filter(product_id=p.product_id.product_id)[0]
        odr_det.items=p.items
        odr_det.product_id=prdt
        odr_det.save()
        amount+=prdt.price*p.items
        print(amount)
        cart_det= Cart_Details.objects.filter(product_id=p.product_id).delete()
    Order.objects.filter(user_id=request.COOKIES['user_id']).update(amount=amount)
    odr = Order.objects.filter(user_id = request.COOKIES['user_id']).first()
    content = 'Your order on Old-One with following details is confirmed!\n Order Status = '+odr.status+'\nTotal Amount= '+str(odr.amount)+'\nOrder Id= '+str(odr.order_id)
    send_email(request,content)
    return render(request,'customer_home/place_order.html')
def send_email(request,content):
        msg = EmailMessage()
        #content = 'Your order on Old-One with following details is confirmed!\n'
        msg.set_content(content)
        fromEmail = 'jaydevbambhaniya45@gmail.com'
        toEmail = Registration.objects.filter(user_id= request.COOKIES['user_id'])[0].email
        msg['Subject'] = 'You have successfully placed your order'
        msg['From'] = fromEmail
        msg['To'] = toEmail
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(fromEmail, 'jaydev1@2*')
        s.send_message(msg)
        s.quit()
        return