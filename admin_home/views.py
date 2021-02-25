
# Create your views here.

#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import models
from admin_home.models import Product_details
from home.models import Registration
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from . import views
import datetime

def index(request,slug):
   userdict={}
   userdict['id']=slug
   return render(request,'admin_home/homepage.html',userdict)
def addProduct(request,slug):
   p=Product_details()
   p.name=request.POST.get('product_name')
   p.price=request.POST.get('product_price')
   p.description=request.POST.get('product_description')
   p.category=request.POST.get('product_category')
   p.product_date=datetime.date.today()
   p.save()
   pth='admin_indexPage/'+str(slug)
   return render(request,pth)
def addProductPage(request,slug):
   userdict={}
   userdict['id']=slug
   return render(request,'admin_home/addProduct.html',userdict)
def deleteProduct(request,slug):
   Product_details.objects.filter(id=slug).delete()
   return HttpResponseRedirect('/viewProduct')
def updateProduct(request,slug):
   name=request.POST.get('product_name')
   price=request.POST.get('product_price')
   description=request.POST.get('product_description')
   category=request.POST.get('product_category')
   p=Product_details.objects.filter(id=slug).update(name=name)
   p=Product_details.objects.filter(id=slug).update(price=price)
   p=Product_details.objects.filter(id=slug).update(category=category)
   p=Product_details.objects.filter(id=slug).update(description=description)
   pth='/viewProduct'+str(slug)
   return HttpResponseRedirect(pth)
def updateProductPage(request,slug):
   p=Product_details.objects.filter(id=slug)[0]
   userdict={}
   userdict['id']=p.id
   userdict['name']=p.name
   userdict['category']=p.category
   userdict['price']=p.price
   userdict['description']=p.description
   return render(request,'admin_home/updateProduct.html',userdict)
def viewProduct(request,slug):
   products=Product_details.objects.all()
   userdict={}
   userdict['id']=slug
   userdict['product']=products
   return render(request,'admin_home/viewProduct.html',userdict)
def signout(request):
   return render(request,'home/login.html')
def updateProfilePage(request,slug):
   p=Registration.objects.filter(id=slug)[0]
   userdict={}
   userdict['id']=p.id
   userdict['name']=p.name
   userdict['password']=p.password
   userdict['dob']=p.dob
   userdict['email']=p.email
   userdict['address']=p.address
   userdict['phone']=p.phone
   return render(request,'admin_home/updateProfile.html',userdict)
def updateProfile(request,slug):
   name=request.POST.get('name')
   password=request.POST.get('password')
   dob=request.POST.get('dob')
   email=request.POST.get('email')
   address=request.POST.get('address')
   phone=request.POST.get('phn')
   Registration.objects.filter(id=slug).update(name=name)
   Registration.objects.filter(id=slug).update(password=password)
   Registration.objects.filter(id=slug).update(email=email)
   Registration.objects.filter(id=slug).update(address=address)
   Registration.objects.filter(id=slug).update(phone=phone)
   Registration.objects.filter(id=slug).update(name=name)
   Registration.objects.filter(id=slug).update(password=password)
   # User=get_user_model()
   # User.objects.filter(id=slug).update(username=name)
   # User.objects.filter(id=slug).update(password=password)
   pth='/admin_indexPage/'+str(slug)
   return HttpResponseRedirect(pth)