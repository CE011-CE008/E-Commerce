from django.urls import path
from Home.views import login, auth_view, logout, loggedin, invalidlogin, registration, base
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout),
    url(r'^loggedin/$', loggedin),
    url(r'^invalidlogin/$', invalidlogin),
    url(r'^registration/$', registration),
    url(r'^base/$', base),
    path('',views.registration)
]