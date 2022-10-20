from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout

def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username , password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home/')
        else:
            messages.info(request, 'Invalid')
    return render(request, 'login.html') 


def logout(request):

    return render(request,'/')