
# Create your views here.

#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.db import connection
from . import views


def index(request):
   return render(request,'admin_home/homepage.html')
