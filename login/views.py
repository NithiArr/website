from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authernticate(username=username , password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home/')
        else:
            messages.info(request, 'Invalid')
    else:
        return render(request, 'login.html  ') 
def logout(request):
    return render(request,'/')