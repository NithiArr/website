from ast import Not
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return render(request,'base.html')
        else:
            messages.info(request,"Doesnt Match")
            return redirect('/')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')