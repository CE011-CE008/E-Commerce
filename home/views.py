from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template.context_processors import csrf
from home.models import Registration
from home.models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from . import views
import random
from django.conf import settings
import smtplib
from email.message import EmailMessage


def forgot(request):
    if request.method=='GET':
        return render(request,'home/forgot.html')
    else:
        us=Registration.objects.filter(email=request.POST.get("email"))
        if us is not None:
            cont='Your Password is:'+Registration.objects.filter(email=request.POST.get("email"))[0].password+'\n if you are not requested for forgot password kindly ignore this.'
            send_email(request,cont)
        else:
            context={'message':'Please Provide registered email ...'}
            return render(request,'home/forgot.html',context)
    return HttpResponseRedirect('/login')



def index(request):
    return render(request,'home/index.html')

def login(request):
    return render(request,'home/login.html')
def auth_view(request):
    email=request.POST.get('email_id')
    password=request.POST.get('password')    
    us=Registration.objects.filter(email=email,password=password).first()
    if us is not None:
        if (us.role=="Admin" or us.role=="admin") :
            if us.otp=='none':
                context={'message':'Please Verify Your mobile number first....'}
                return render(request,'home/registration.html',context)
            pth='admin_indexPage'
            response = HttpResponseRedirect(pth)
            response.set_cookie("user_id", us.user_id)
            return response
        elif us.role=="customer" :
            if us.otp=='none':
                context={'message':'Please Verify Your mobile number first....'}
                return render(request,'home/registration.html',context)
            pth='customer_home_index'
            response = HttpResponseRedirect(pth)
            return response
    return render(request,'home/invalidlogin.html')
def register(request):
    if request.method=='GET':
        return render(request,'home/registration.html')
    elif request.POST.get('name') and request.POST.get('password'):
        name= request.POST.get('name')
        password=request.POST.get('password')
        saverecord = Registration()
        saverecord.name = request.POST.get('name')
        saverecord.password = request.POST.get('password')
        saverecord.dob = request.POST.get('dob')
        saverecord.email = request.POST.get('email')
        saverecord.address = request.POST.get('address')
        saverecord.phone = request.POST.get('phn')
        exit_user=Registration.objects.filter(email=request.POST.get('email')).first()
        if exit_user:
            context={'message':'Email already registered try with different..','class':'danger'}
            return render(request,'home/registration.html',context)
        saverecord.role="admin"
        otp=str(random.randint(99999,999999))
        request.session['otp']=otp
        request.session['email']=request.POST.get('email')
        send_email(request,'Your Otp is:'+otp)
        saverecord.otp='none'
        saverecord.save()
        return HttpResponseRedirect('/otp')
    return render(request,'home/registration.html')
def otp(request):
    return render(request,'home/otp.html')
def loggedin(request):
    return render(request,'home/loggedin.html', {"full_name":request.user.username})
def invalidlogin(request):
    return render(request,'home/invalidlogin.html')
def logout(request):
    return render(request,'home/index.html')
def term_condition(request):
    return render(request,'home/term_condition.html')
def about_us(request):
    return render(request,'home/about_us.html')
def contactUs(request):
    return render(request,'home/contactUs.html')
def verify_otp(request):
    cur_otp=request.POST.get('otp')
    if cur_otp==request.session['otp']:
        Registration.objects.filter(email=request.session['email']).update(otp=request.session['otp'])
        return HttpResponseRedirect('/login')
    else:
        context={'message':'Invalid Otp....'}
        return render(request,'home/otp.html',context)
def send_email(request,content):
        msg = EmailMessage()
        msg.set_content(content)
        fromEmail = 'bkevin6566@gmail.com'
        toEmail = request.POST.get('email')
        msg['Subject'] = 'otp for ecoomerce website'
        msg['From'] = fromEmail
        msg['To'] = toEmail
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(fromEmail, 'Bkevin@5997')
        s.send_message(msg)
        s.quit()
        return
def contactUs(request):
    if request.method=='GET':
        return render(request,'home/contactUs.html')
    else:
        f = Feedback()
        f.name = request.POST.get("name")
        f.email = request.POST.get("email")
        f.comment = request.POST.get("comment")
        f.status = 'unseen'
        f.save()
        return render(request,'home/index.html')