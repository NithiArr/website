from django.contrib import admin
from django.urls import path,include
from home.views import home
from login.views import loginn
from base.views import stedit,stupdate,stdel
urlpatterns = [
    path('',home),
    path('login/',loginn),
    path('show/',include('base.urls')),
    path('admin/', admin.site.urls),
    path('edit/<int:id>', stedit,name="stedit"),
    path('update/<int:id>',stupdate,name="stupdate"),
    path('Delete/<int:id>',stdel,name="stdel")
]
