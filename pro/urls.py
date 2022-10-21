from django.contrib import admin
from django.urls import path,include
from login.views import loginn,logout,adminlogin, registerr,   register
from base.views import stedit,stupdate,stdel,stinsert,stdisplay,homee,searchpage
from home.views  import totalorder,orderdelivered,pending
urlpatterns = [
    path('',loginn),
    path('adminlogin/',adminlogin),
    path('registerr',registerr),
    path('register',register),
    path('logout/',logout),
    path('home/',homee),
    path('create/',stinsert,name='stinsert'),
    path('show/',stdisplay,name='stdisplay'),
    path('admin/', admin.site.urls),
    path('edit/<int:id>', stedit,name="stedit"),
    path('update/<int:id>',stupdate,name="stupdate"),
    path('searchpage/',searchpage,name="search"),
    path('totalorder/',totalorder,name="totalorder"),
    path('orderdelivered/',orderdelivered,name="orderdelivered"),
    path('pending/',pending,name="pending"),
    path('Delete/<int:id>',stdel,name="stdel")
]
