from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User

def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home/')
        else:
<<<<<<< HEAD
            messages.info(request,"Doesnt Match")
            return redirect('/')
=======
            messages.info(request, 'Doesnt Match')
            return render(request,'login.html')
>>>>>>> 5babdfb4f7536e3ce2b0efc8392c7e418ed14582
    else:
        return render(request, 'login.html') 


def logout(request):
    auth.logout(request)
    return render(request,'/')

def adminlogin(request):
     if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('registerr/')
        else:
            messages.info(request, 'Invalid')
            return render(request,'adminlogin.html')
     else:
        return render(request  ,'adminlogin.html') 
def registerr(request):
        return render(request  ,'register.html')    

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user= User.objects.create_user(username=username,password=password)
        user.save();
        return render(request, "login.html")
        
    else:
        return render(request  ,'register.html') 

    

