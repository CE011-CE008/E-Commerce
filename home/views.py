
# Create your views here.

#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render
from . import views
def login(request):
    return render(request,'home/login.html')
def index(request):
   return render(request,"home/base.html")
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        return render(request,'home/loggedin.html')
    else:
        return render(request,'home/invalidlogin.html')
def registration(request):
    return render(request,'home/registration.html')
def loggedin(request):
    return render(request,'home/loggedin.html', {"full_name":request.user.username})
def invalidlogin(request):
    return render(request,'home/invalidlogin.html')
def logout(request):
    auth.logout(request)
    return render(request,'home/logout.html')