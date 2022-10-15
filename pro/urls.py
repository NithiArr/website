from django.contrib import admin
from django.urls import path,include
from login.views import loginn,logout
from base.views import stedit,stupdate,stdel,stinsert,stdisplay,homee,searchpage
urlpatterns = [
    path('',loginn),
    path('logout/',logout),
    path('home/',homee),
    path('create/',stinsert,name='stinsert'),
    path('show/',stdisplay,name='stdisplay'),
    path('admin/', admin.site.urls),
    path('edit/<int:id>', stedit,name="stedit"),
    path('update/<int:id>',stupdate,name="stupdate"),
    path('searchpage/',searchpage,name="search"),
    path('Delete/<int:id>',stdel,name="stdel")
]
