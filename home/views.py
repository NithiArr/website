from django.shortcuts import render
from base.models import crudst
from django.db.models import Q


def home(request):

    return render(request, 'home.html')

def totalorder(request):
    status='Out for delivery'
    results=crudst.objects.all()
<<<<<<< HEAD
    if status:
            results = results.filter(Q(status__icontains = status))
            ordercount= results.count()
    return render(request,"home.html",{"crudst":results,'ordercount':ordercount})
=======
    return render(request,"home.html",{"crudst":results})
>>>>>>> 5babdfb4f7536e3ce2b0efc8392c7e418ed14582

def orderdelivered(request):
        status = 'delivered'
        emps = crudst.objects.all()
        
        
        if status:
            
            emps = emps.filter(Q(status__icontains = status))
            cou= emps.count()
        return render(request, 'home.html', {'detail': emps,'cou':cou})

def pending(request):
        status = 'pending'
        emps = crudst.objects.all()
        if status:
            emps = emps.filter(Q(status__icontains = status))
            cou= emps.count()
        return render(request, 'home.html', {'details': emps,'ou':cou})