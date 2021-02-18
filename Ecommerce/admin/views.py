from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf
from home.models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.db import connection
from . import views

def admin(request):
    render(request,'admin/homepage.html')