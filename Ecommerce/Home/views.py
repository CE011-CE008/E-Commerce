from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.template.context_processors import csrf
from Home.models import Registration

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html',c)
    
def  auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    us = auth.authenticate(username=username,password=password)
    if us is not None:
        return HttpResponseRedirect('/Home/loggedin/')
    else:
        return HttpResponseRedirect('/Home/invalidlogin/')
    
def loggedin(request):
    return render(request,'loggedin.html', {"full name": request.user.username})
    
def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
    
def base(request):
    return render(request,'base.html')
def registration(request):
    if(request.POST.get('name') and request.POST.get('password')):
        User = get_user_model()  
        user = User.objects.create_user(username=request.POST.get('name'), password=request.POST.get('password'))
        saverecord = Registration()
        saverecord.name = request.POST.get('name')
        saverecord.password = request.POST.get('password')
        saverecord.email = request.POST.get('email')
        saverecord.address = request.POST.get('address')
        saverecord.dob = request.POST.get('dob')
        saverecord.phone = request.POST.get('phn')
        saverecord.save()
        return HttpResponseRedirect('/Home/login')
    messages.success(request,'Sorry some error occurred')
    return render(request,'registration.html')
    