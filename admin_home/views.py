
# Create your views here.

#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import models
from admin_home.models import Product_Details
from home.models import Registration
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from . import views
from datetime import datetime

def index(request):
   userdict={}
   userdict['id']=request.COOKIES['user_id']
   print(request.COOKIES['user_id'])
   return render(request,'admin_home/homepage.html',userdict)
def addProduct(request):
      p=Product_Details()
      p.product_name =request.POST.get('product_name')
      p.price =request.POST.get('product_price')
      p.description =request.POST.get('product_description')
      p.category =request.POST.get('product_category')
      p.image=request.FILES['image']
      p.save()
      pth='/admin_indexPage'
      return HttpResponseRedirect(pth)
def addProductPage(request):
   return render(request,'admin_home/addProduct.html')
def deleteProduct(request,slug):
   Product_Details.objects.filter(product_id=slug).delete()
   pth='/viewProduct'
   return HttpResponseRedirect(pth)
def updateProduct(request,slug):
   name=request.POST.get('product_name')
   price=request.POST.get('product_price')
   description=request.POST.get('product_description')
   category=request.POST.get('product_category')
   p=Product_Details.objects.filter(product_id=slug).update(product_name=name)
   p=Product_Details.objects.filter(product_id=slug).update(price=price)
   p=Product_Details.objects.filter(product_id=slug).update(category=category)
   p=Product_Details.objects.filter(product_id=slug).update(description=description)
   pth='/viewProduct'
   return HttpResponseRedirect(pth)
def updateProductPage(request,slug):
   p=Product_Details.objects.filter(product_id=slug)[0]
   userdict={}
   userdict['product_id']=p.product_id
   userdict['name']=p.product_name
   userdict['category']=p.category
   userdict['price']=p.price
   userdict['description']=p.description
   return render(request,'admin_home/updateProduct.html',userdict)
def viewProduct(request):
   products=Product_Details.objects.all()
   userdict={}
   userdict['id']=request.COOKIES['user_id']
   userdict['product']=products
   return render(request,'admin_home/viewProduct.html',userdict)
def signout(request):
   response=HttpResponseRedirect('/')
   response.delete_cookie('user_id')
   return response
def updateProfilePage(request):
   uid=request.COOKIES['user_id']
   p=Registration.objects.filter(id=uid)[0]
   userdict={}
   userdict['id']=p.id
   userdict['name']=p.name
   userdict['password']=p.password
   userdict['dob']=p.dob
   userdict['email']=p.email
   userdict['address']=p.address
   userdict['phone']=p.phone
   return render(request,'admin_home/updateProfile.html',userdict)
def updateProfile(request):
   uid=request.COOKIES['user_id']
   name=request.POST.get('name')
   password=request.POST.get('password')
   dob=request.POST.get('dob')
   email=request.POST.get('email')
   address=request.POST.get('address')
   phone=request.POST.get('phn')
   Registration.objects.filter(id=uid).update(name=name)
   Registration.objects.filter(id=uid).update(password=password)
   Registration.objects.filter(id=uid).update(email=email)
   Registration.objects.filter(id=uid).update(address=address)
   Registration.objects.filter(id=uid).update(phone=phone)
   Registration.objects.filter(id=uid).update(name=name)
   Registration.objects.filter(id=uid).update(password=password)
   # User=get_user_model()
   # User.objects.filter(id=slug).update(username=name)
   # User.objects.filter(id=slug).update(password=password)
   pth='/admin_indexPage'
   return HttpResponseRedirect(pth)
