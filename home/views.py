
# Create your views here.

#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import get_user_model

from django.template.context_processors import csrf
from home.models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from . import views

def index(request):
    return render(request,'home/index.html')

def login(request):
    return render(request,'home/login.html')

def auth_view(request):
    name=request.POST.get('username')
    password=request.POST.get('password')
    #check=auth.authenticate(username=name,password=password)
    all_user=Registration.objects.all()
   
    #if check is not None:
    for us in all_user:
        if us.role=="admin" and us.name==name and us.password==password:
            pth='admin_indexPage/'+str(us.id)
            return HttpResponseRedirect(pth)
        elif us.role=="customer" and us.name==name and us.password==password:
            return render(request,'customer/homepage.html')
    return render(request,'home/invalidlogin.html')
def registration(request):
    #messages.success(request,'Sorry some error occurred')
    return render(request,'home/registration.html')
def register(request):
    if(request.POST.get('name') and request.POST.get('password')):
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
        saverecord.role="customer"
        saverecord.save()
        
        return render(request,'home/login.html')
def loggedin(request):
    return render(request,'home/loggedin.html', {"full_name":request.user.username})
def invalidlogin(request):
    return render(request,'home/invalidlogin.html')
def logout(request):
    #auth.logout(request)
    return render(request,'home/logout.html')
def term_condition(request):
    return render(request,'home/term_condition.html')