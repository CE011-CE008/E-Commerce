
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
   if request.method=='GET':
      return render(request,'admin_home/addProduct.html')
   else:
      p=Product_Details()
      p.product_name =request.POST.get('product_name')
      p.price =request.POST.get('product_price')
      p.description =request.POST.get('product_description')
      p.category =request.POST.get('product_category')
      p.image=request.FILES['image']
      p.save()
      pth='/admin_indexPage'
      return HttpResponseRedirect(pth)
def deleteProduct(request,slug):
   Product_Details.objects.filter(product_id=slug).delete()
   pth='/viewProduct'
   return HttpResponseRedirect(pth)
def updateProduct(request,slug):
   if request.method=='GET':
      p=Product_Details.objects.filter(product_id=slug)[0]
      userdict={}
      userdict['product_id']=p.product_id
      userdict['name']=p.product_name
      userdict['category']=p.category
      userdict['price']=p.price
      userdict['description']=p.description
      return render(request,'admin_home/updateProduct.html',userdict)
   else:
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
def updateProfile(request):
   if request.method=='GET':
      uid=request.COOKIES['user_id']
      p=Registration.objects.filter(user_id=uid)[0]
      userdict={}
      userdict['id']=p.user_id
      userdict['name']=p.name
      userdict['password']=p.password
      userdict['dob']=p.dob
      userdict['email']=p.email
      userdict['address']=p.address
      userdict['phone']=p.phone
      return render(request,'admin_home/updateProfile.html',userdict)
   else:
      uid=request.COOKIES['user_id']
      r=Registration.objects.filter(user_id=uid)[0]
      name=request.POST.get('name')
      password=request.POST.get('password')
      dob=request.POST.get('dob')
      email=request.POST.get('email')
      address=request.POST.get('address')
      phone=request.POST.get('phn')
      Registration.objects.filter(user_id=uid).update(name=name)
      Registration.objects.filter(user_id=uid).update(password=password)
      Registration.objects.filter(user_id=uid).update(email=email)
      Registration.objects.filter(user_id=uid).update(address=address)
      Registration.objects.filter(user_id=uid).update(phone=phone)
      Registration.objects.filter(user_id=uid).update(name=name)
      Registration.objects.filter(user_id=uid).update(password=password)
      if r.role=='customer':
         pth='/customer_home_index'
      else :
         pth='/admin_indexPage'
      return HttpResponseRedirect(pth)
   return HttpResponseRedirect('/login')
def addAdmin(request):
   if request.method=='GET':
      return render(request,'admin_home/registration.html')
   if request.POST.get('name') and request.POST.get('password'):
        # name= request.POST.get('name')
        # User=get_user_model()
        # password=request.POST.get('password')
        # temp_user=User.objects.create_user(username=name,password=password)
        # temp_user.save()
        saverecord = Registration()
        # saverecord.user=temp_user
        saverecord.name = request.POST.get('name')
        saverecord.password = request.POST.get('password')
        saverecord.dob = request.POST.get('dob')
        saverecord.email = request.POST.get('email')
        saverecord.address = request.POST.get('address')
        saverecord.phone = request.POST.get('phn')
        saverecord.role="admin"
        saverecord.save()
        return render(request,'home/login.html')