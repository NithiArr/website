from django.shortcuts import render
from base.models import crudst
from django.db.models import Q
from django.db.models import Sum


def home(request):

    return render(request, 'home.html')

def totalorder(request):
    status='Out for delivery'
    results=crudst.objects.all()
    if status:
            results = results.filter(Q(status__icontains = status))
            ordercount= results.count()
            total=results.aggregate(Sum('price'))
    return render(request,"home.html",{"crudst":results,'ordercount':ordercount,'total':total})

def orderdelivered(request):
        status = 'delivered'
        emps = crudst.objects.all()
         
        if status:
            
            emps = emps.filter(Q(status__icontains = status))
            cou= emps.count()
            sumof=emps.aggregate(Sum('price'))
        return render(request, 'home.html', {'detail': emps,'cou':cou,'sum':sumof})

def pending(request):
        status = 'pending'
        emps = crudst.objects.all()
        if status:
            emps = emps.filter(Q(status__icontains = status))
            cou= emps.count()
            suprice=emps.aggregate(Sum('price'))
        return render(request, 'home.html', {'details': emps,'ou':cou,'price':suprice})