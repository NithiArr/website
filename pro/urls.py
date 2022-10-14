from django.contrib import admin
from django.urls import path,include
from home.views import home
from login.views import loginn,logout
from base.views import stedit,stupdate,stdel,stinsert,stdisplay
urlpatterns = [
    path('',loginn),
    path('logout/',logout),
    path('create/',stinsert,name='stinsert'),
    path('show/',stdisplay,name='stdisplay'),
    path('admin/', admin.site.urls),
    path('edit/<int:id>', stedit,name="stedit"),
    path('update/<int:id>',stupdate,name="stupdate"),
    path('Delete/<int:id>',stdel,name="stdel")
]
