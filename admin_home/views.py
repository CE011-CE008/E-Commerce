
# Create your views here.

#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from admin_home.models import Product_details
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from . import views
import datetime

def index(request):
   return render(request,'admin_home/homepage.html')
def addProduct(request):
   p=Product_details()
   p.name=request.POST.get('product_name')
   p.price=request.POST.get('product_price')
   p.description=request.POST.get('product_description')
   p.category=request.POST.get('product_category')
   p.product_date=datetime.date.today()
   p.save()
   return render(request,'admin_home/homepage.html')
def addProductPage(request):
   return render(request,'admin_home/addProduct.html')
def deleteProduct(request,slug):
   Product_details.objects.filter(id=slug).delete()
   return HttpResponseRedirect('/viewProduct')
def updateProduct(request,slug):
   print(slug)
   name=request.POST.get('product_name')
   price=request.POST.get('product_price')
   description=request.POST.get('product_description')
   category=request.POST.get('product_category')
   p=Product_details.objects.filter(id=slug).update(name=name)
   p=Product_details.objects.filter(id=slug).update(price=price)
   p=Product_details.objects.filter(id=slug).update(category=category)
   p=Product_details.objects.filter(id=slug).update(description=description)
   return HttpResponseRedirect('/viewProduct')
def updateProductPage(request,slug):
   p=Product_details.objects.filter(id=slug)[0]
   userdict={}
   userdict['id']=p.id
   userdict['name']=p.name
   userdict['category']=p.category
   userdict['price']=p.price
   userdict['description']=p.description
   return render(request,'admin_home/updateProduct.html',userdict)
def viewProduct(request):
   products=Product_details.objects.all()
   return render(request,'admin_home/viewProduct.html',{'product':products})
