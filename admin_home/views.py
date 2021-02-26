
# Create your views here.

#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import models
from admin_home.models import Product_details
from home.models import Registration
from admin_home.forms import Add_product_form
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

def index(request,slug):
   userdict={}
   userdict['id']=slug
   return render(request,'admin_home/homepage.html',userdict)
def addProduct(request,slug):
   form = Add_product_form(request.POST, request.FILES)
   if form.is_valid():
      product_img = form.cleaned_data['product_img']
      name = form.cleaned_data['name']
      price = form.cleaned_data['price']
      description = form.cleaned_data['description']
      category = form.cleaned_data['category']
      print(product_img,name,price,description,category)
      timestamp=str(datetime.timestamp(datetime.now()))
      p=Product_details()
      p.name=name
      p.price=price
      p.description=description
      p.category=category
      path = default_storage.save('product_images/'+timestamp+'.jpg', ContentFile(product_img.read()))
      p.img_url='http://localhost:8000/media/product_images/'+timestamp+'.jpg'
      p.save()
   else :
      print('not valid')
   pth='/admin_indexPage/'+str(slug)
   return HttpResponseRedirect(pth)
def addProductPage(request,slug):
   userdict={}
   userdict['id']=slug
   form=Add_product_form()
   userdict['form']=form
   return render(request,'admin_home/addProduct.html',userdict)
def deleteProduct(request,slug):
   Product_details.objects.filter(product_id=slug).delete()
   pth='/viewProduct/'+str(slug)
   return HttpResponseRedirect(pth)
def updateProduct(request,slug):
   name=request.POST.get('product_name')
   price=request.POST.get('product_price')
   description=request.POST.get('product_description')
   category=request.POST.get('product_category')
   p=Product_details.objects.filter(product_id=slug).update(name=name)
   p=Product_details.objects.filter(product_id=slug).update(price=price)
   p=Product_details.objects.filter(product_id=slug).update(category=category)
   p=Product_details.objects.filter(product_id=slug).update(description=description)
   pth='/viewProduct/'+str(slug)
   return HttpResponseRedirect(pth)
def updateProductPage(request,slug):
   p=Product_details.objects.filter(product_id=slug)[0]
   userdict={}
   userdict['product_id']=p.product_id
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
   return render(request,'home/index.html')
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
